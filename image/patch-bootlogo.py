#!/usr/bin/env python3
"""Replace BOOTLOGO.BMP inside the Allwinner bootlogo FAT partition.

The stock image keeps a small FAT16 filesystem at byte offset 36 MiB
(37748736). U-Boot reads BOOTLOGO.BMP from it and shows it as the very first
boot splash. The partition survives in both the base image and the combined
image (the combiner copies the stock's first 84 MiB over the base), so the
logo can be replaced in place.

A 640x480 24-bit BMP is 921654 bytes, exactly the size of the stock logo, so
the file can be overwritten without touching the FAT. The script verifies
that the layout matches and that the cluster chain is contiguous.

usage: patch-bootlogo.py IMAGE LOGO.bmp
"""
import struct
import sys

FAT_OFFSET = 36 * 1024 * 1024
LOGO_NAME = (b"BOOTLOGO", b"BMP")


def fail(msg):
    print("patch-bootlogo: " + msg, file=sys.stderr)
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("usage: %s IMAGE LOGO.bmp" % sys.argv[0], file=sys.stderr)
        return 2

    img_path, bmp_path = sys.argv[1], sys.argv[2]
    bmp = open(bmp_path, "rb").read()
    if bmp[:2] != b"BM":
        fail("%s is not a BMP file" % bmp_path)

    with open(img_path, "r+b") as img:
        img.seek(FAT_OFFSET)
        boot = img.read(512)
        if len(boot) < 512 or boot[54:62] != b"FAT16   ":
            fail("no FAT16 boot sector at offset %d" % FAT_OFFSET)
        bps, spc, rsvd, nfats, rootent, _tot16, _media, fatsz16 = \
            struct.unpack_from("<HBHBHHBH", boot, 11)
        if bps != 512 or fatsz16 == 0 or rootent == 0:
            fail("unsupported BPB (bytes/sector=%d fatsz16=%d rootent=%d)"
                 % (bps, fatsz16, rootent))

        root_off = FAT_OFFSET + (rsvd + nfats * fatsz16) * bps
        entry = None
        for i in range(rootent):
            img.seek(root_off + i * 32)
            e = img.read(32)
            if len(e) < 32 or e[0] == 0:
                break
            if e[0] == 0xE5 or (e[11] & 0x3F) == 0x0F:
                continue
            name = e[0:8].rstrip(b" ").upper()
            ext = e[8:11].rstrip(b" ").upper()
            if (name, ext) == LOGO_NAME:
                entry = e
                break
        if entry is None:
            fail("BOOTLOGO.BMP not found in the bootlogo FAT")

        size = struct.unpack_from("<I", entry, 28)[0]
        first = struct.unpack_from("<H", entry, 26)[0]
        if size != len(bmp):
            fail("size mismatch: BOOTLOGO.BMP is %d bytes, %s is %d; "
                 "convert with: convert start.png -type truecolor "
                 "-depth 8 BMP3:start.bmp" % (size, bmp_path, len(bmp)))

        fat_off = FAT_OFFSET + rsvd * bps
        img.seek(fat_off)
        fat = img.read(fatsz16 * bps)
        cluster_bytes = spc * bps
        needed = (size + cluster_bytes - 1) // cluster_bytes

        chain, c = [], first
        while c < 0xFFF7 and len(chain) <= needed:
            chain.append(c)
            c = struct.unpack_from("<H", fat, c * 2)[0]
        if len(chain) < needed:
            fail("cluster chain too short (%d < %d)" % (len(chain), needed))
        for a, b in zip(chain, chain[1:needed]):
            if b != a + 1:
                fail("cluster chain is fragmented; refusing in-place write")

        data_sec = rsvd + nfats * fatsz16 + rootent * 32 // bps
        data_off = FAT_OFFSET + (data_sec + (first - 2) * spc) * bps
        img.seek(data_off)
        img.write(bmp)
        img.flush()

    print("patched BOOTLOGO.BMP at offset %d (%d bytes)" % (data_off, len(bmp)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
