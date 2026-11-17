# goodluckOSNext

Personal fork of [goodluckOS](https://github.com/CodeZombie/goodluckOS) by [dubiduglitch](https://github.com/dubiduglitch).

This is a personal fork. It is not affiliated with the official goodluckOS project and is not meant to replace it.

> **Beta software.** goodluckOS can permanently damage your hardware. No warranty, use at your own risk. See the [Disclaimer](#disclaimer).

---

## Table of contents

- [Target console](#target-console)
- [New here? Start with this](#new-here-start-with-this)
- [Components](#components)
- [Installation](#installation)
- [Daily use](#daily-use)
- [Known limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Reporting a new or unsupported board](#reporting-a-new-or-unsupported-board)
- [Legal notes](#legal-notes)
- [Build](#build)
- [Awesome goodluckOS](#awesome-goodluckos)
- [Disclaimer](#disclaimer)

---

## Target console

This firmware targets **GA36-MB V1.2-20260416** handhelds, often sold as "R36S" clones.

| Feature | Detail |
|---------|--------|
| SoC | Allwinner A23 (ARM Cortex-A7, 32-bit) |
| GPU | Mali-400 MP2 |
| RAM | 512 MB |
| Screen | 640 × 480 (at least two different panels exist) |
| Storage | microSD (TF-1 is the main slot, TF-2 is optional depending on the model) |
| Connectivity | USB OTG (gadget mode: serial, MTP, networking) |

The hardware is sold under many brands (R36S clone, Zekko, Tekko, R36MAX clone, etc.). The manufacturer provides no official drivers.

> **Specs vary by revision.** The table above describes the V1.2-20260416 board. One user reports a "GA36 MB V1.1" with a 64-bit Mali-G31 and 1 GB of RAM ([issue #164](https://github.com/CodeZombie/goodluckOS/issues/164)). Check your own board ID and CPU info before assuming anything.

More info: [R36S Clones, handhelds.wiki](https://handhelds.wiki/R36S_Clones)

---

## New here? Start with this

**1. This is not a "real" R36S.** The genuine R36S uses a Rockchip RK3326. Your GA36-MB uses an **Allwinner A23/A33**. Firmware for the real R36S (ArkOS, dArkOS, dArkOSRE, ROCKNIX, etc.) **will not boot** on it. The handhelds.wiki clone page lists the GA36 under "Fakes" and names goodluckOS, Kennel and Debianator as the custom firmware options.

**2. Identify your board.** The board ID is printed on the PCB (for example `GA36-MB V1.2-20260416`). Known revisions: V1.0-20250730, V1.1-20251025 and V1.2-20260416. Stock units run a custom EmuELEC 4.7 build and use roughly 480 MB of swap on the SD card.

**3. Back up your original SD card before anything else.** The goodluckOS Firmware Builder needs a backup of at least the **first 128 MB** of the card that came with the console. If you have lost it, open an issue on the upstream repo: maintainers keep microSD dumps for several hardware variants.

**4. Use the Firmware Builder** to confirm your unit is compatible and to build a flashable image: <https://codezombie.github.io/goodluckOS/download.html>

**5. Everything is 32-bit (armhf).** 64-bit-only software, including many Android and PortMaster aarch64 ports, will never run. With 512 MB of RAM, unoptimized games also struggle.

**6. Know the open issues.** Some boards (for example a "Tekko" branded V1.2-20260416 unit, [issue #30](https://github.com/CodeZombie/goodluckOS/issues/30)) reportedly show no reaction to the goodluckOS image, and some users report a garbled screen ([issue #112](https://github.com/CodeZombie/goodluckOS/issues/112)). Search the [issue tracker](https://github.com/CodeZombie/goodluckOS/issues) for your board ID before flashing, and report your results.

---

## Components

> Authors, licenses and links below come from the fork maintainer and have not been independently re-verified. GTA, Hotline Miami and Stardew Valley ports contain only port code: **you must supply your own legally obtained game files.** The licenses listed cover the port code, not the games' assets.

| Component | Author | License | Link |
|-----------|--------|---------|------|
| goodluckOS (base) | CodeZombie | GPL-2.0 | https://github.com/CodeZombie/goodluckOS |
| Mali-400 driver (kernel + user-space) | nyakaspeter | GPL-2.0 / ARM proprietary | https://github.com/nyakaspeter/goodluckOS-mali-driver |
| GTA III | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-gta3-pc |
| GTA Vice City | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-gtavc-pc |
| GTA Liberty City Stories | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-gtalcs-pc |
| GTA Vice City Stories | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-gtavcs-psp |
| Hotline Miami | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-hotlinemiami |
| Hotline Miami 2 | nyakaspeter | MIT | https://github.com/nyakaspeter/glOSports-hotlinemiami2 |
| Stardew Valley (source) | igol23 | GPL-2.0 | https://github.com/igol23/glOSports-stardew-valley |
| Stardew Valley (port) | alvesmaicon | MIT | https://github.com/alvesmaicon/glOSports-stardew |
| Mediabox | lw10a | AGPL-3.0 | https://github.com/lw10a/Mediabox-goodluckOS |
| Arcade & emulators (30+) | rincewindcz | MIT | https://github.com/rincewindcz/ga36-ports |

### Launcher & system

| Project | Author | License | Link |
|---------|--------|---------|------|
| Kennel (launcher) | rincewindcz | MIT | https://github.com/rincewindcz/kennel |
| Puppy (default launcher) | CodeZombie | see upstream repo | https://github.com/CodeZombie/goodluckOS |
| SDL | libsdl | zlib | https://www.libsdl.org/ |
| Mesa / lima | Mesa3D | MIT | https://mesa3d.org/ |

---

## Installation

Flash the compressed image to your SD card:

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M conv=fsync status=progress
sync
```

Replace `/dev/sdX` with your SD card device. Double-check it with `lsblk` first: `dd` will overwrite whatever you point it at. `conv=fsync` and `sync` make sure everything is written before you remove the card.

Then:

1. Put the card in **TF-1 (the OS slot)**.
2. Power on. Boot takes about 10 seconds.
3. To go back to stock, re-flash your original SD card backup (see the FAQ).
4. If the screen stays black or garbled, the panel may be the other supported type. Upstream notes there is currently no way to tell panels apart in advance, so try both images from the Firmware Builder.

On Windows, decompress the image with `zstd -d goodluckOSNext.img.zst` first, then write the resulting `.img` with your usual imaging tool.

---

## Daily use

### Adding games

- **USB (MTP):** connect the console's OTG port to your PC. It appears as `GA36MB`, storage `HOME`. A direct USB-C to USB-C cable does not work. macOS needs an MTP app such as [OpenMTP](https://openmtp.ganeshrvel.com/). If the console was on a charger when it booted, restart it before plugging into the PC.
- **Card reader:** open the `HOME` partition on the SD card. If your PC offers to format or repair another partition, say no.
- Put ROMs in `roms/<system>`. Custom art goes in `roms/<system>/icons/<romname>.png`.
- **Second card (TF-2):** games go in `roms/<system>` on the second card. Format it **FAT32**: exFAT is not read yet.

### Hotkeys

| Buttons | Action |
|---------|--------|
| FN + VOL UP/DOWN | Adjust screen brightness |
| FN + DOWN | Toggle speaker / headphone output |
| FN + UP | Show live CPU/FPS stats |
| START + SELECT | Gracefully exit the current app |
| FN + START + SELECT | Kill (-9) the current app |
| POWER (short press) | Turn the screen off |

> The Mali driver documentation mentions a Mode+Start+Select kill combo for ports. Hotkeys can differ between builds, so verify on your image.

### USB serial console

Plug into a Linux PC via the OTG port, then:

```bash
sudo screen /dev/ttyACM* 115200
```

Default login: `root` / `root`. Change the password if you expose the device to anything beyond your own desk.

**USB networking:** upstream still lists it as unfinished. Kennel exposes a USB mode setting (Settings > System > USB mode) and the GA36 Ports docs mention `scp` to `/home/player`, so behavior depends on your launcher and build. Test it before relying on it.

### Ports (games)

Download a port from [GA36 Ports](https://ga36.genserek.net/), unzip it, and copy the `ports` and `.local` folders into the root of `HOME` (`.local` is hidden on Linux and macOS). Ports appear in the **Ports** category of Kennel or Puppy. Updating means unzipping over the old version (saves are kept). Removing means deleting `ports/<port>`, `.local/share/applications/<port>.puppy` and `.local/share/icons/<port>.png`.

Ports marked "needs your own game files" do not include commercial game data. Bring your own legal copy.

---

## Known limitations

- 32-bit (armhf) only. aarch64-only software will never run.
- 512 MB of RAM: unoptimized games may need patching.
- exFAT cards are not read yet. Use FAT32.
- Headphone auto-detection may be missing on some boards. Switch output manually with FN + DOWN (the speaker returns at boot).
- No PortMaster or EmulationStation yet (both on upstream's to-do list).
- No CPU overclocking yet.
- Two display panel types exist and cannot yet be told apart in advance.

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| Black screen / no reaction | Card in TF-1? Image built for your board revision? Try the other panel build. |
| Port not in the menu | Make sure `.local` was copied, then restart the console. |
| Port quits immediately | Read `ports/<port>/run.log`. It is usually missing game files. |
| Emulators or Chocolate Doom fail after many game launches | Applies to builds using the ARM Mali driver. Each launch that switches from lima to ARM's driver leaks a little display memory, and after roughly 60-80 launches in one boot buffers can no longer be allocated. Reboot. |
| exFAT second card not detected | Reformat the card as FAT32. |
| Anything else | Open an issue with your board ID, the goodluckOS version and any logs. |

---

## FAQ

**Does goodluckOS overwrite my original firmware?** It replaces what is on the card you flash. Keep your original SD card, or a backup image of it (at least the first 128 MB, ideally the whole card), and you can go back to stock by re-flashing it.

**How do I back up the original card?** Image the whole card to a file, for example `sudo dd if=/dev/sdX of=stock-backup.img bs=4M status=progress` on Linux, or use a disk-imaging tool on Windows. See the [Retro Handhelds setup guide](https://retrohandhelds.gg/r36s-setup-guide/) for a Windows walkthrough.

**Does my board have a TF-2 slot?** It depends on the model. Upstream says TF-2 works "on supported hardware".

**Can I run PortMaster games?** Only 32-bit ones, and only if they are ported to goodluckOS. Use [GA36 Ports](https://ga36.genserek.net/) first.

**Which card size do I need?** Upstream says a minimum of 512 MB and no maximum limit. The Resize Home app (in some builds) grows the HOME partition to fill the card.

---

## Reporting a new or unsupported board

If the Firmware Builder says your unit is not supported, or the image does not boot:

1. Note your exact board ID (printed on the PCB) and which store or brand sold it.
2. Keep your original card's contents. Upstream asks for the `script.bin` file from the stock firmware so maintainers can verify goodluckOS is safe for your device.
3. Search the [issue tracker](https://github.com/CodeZombie/goodluckOS/issues) for your board ID, then open an issue with the details above, your panel behavior (black, garbled, working) and anything shown over USB serial.

---

## Legal notes

- **Mali driver:** ARM's user-space `libMali.so` is proprietary and is deliberately not in the driver repo. If you redistribute images that bundle it, check ARM's license terms (Bootlin publishes the blobs with ARM's license).
- **Game ports:** projects like GTA ports are reverse-engineered engines. Their legal status can change, so check the current state of the upstream repos you rely on.
- **ROMs and game data:** nothing here distributes commercial game data. Use legally obtained files.

---

## Build

Requires Docker (or Podman). See `BUILD.md`.

---

## Awesome goodluckOS

### Official and core projects

| Resource | Description | Link |
|----------|-------------|------|
| goodluckOS | Custom firmware for A23/A33 handhelds (upstream) | https://github.com/CodeZombie/goodluckOS |
| Firmware Builder | Hardware identifier plus flashable image builder | https://codezombie.github.io/goodluckOS/download.html |
| goodluckOS issues | Bug reports, board support requests, SD dumps | https://github.com/CodeZombie/goodluckOS/issues |
| goodluckOS BUILD.md | Containerized Buildroot build instructions | https://github.com/CodeZombie/goodluckOS/blob/main/BUILD.md |
| goodluckOS CHANGELOG | Release history | https://github.com/CodeZombie/goodluckOS/blob/main/CHANGELOG.md |
| goodluckOS Device Fund | Help buy new consoles to port the OS to | https://ko-fi.com/jeremyclark |
| goodluckOS-mali-driver | ARM Mali driver for goodluckOS (2-3x faster than lima in 3D ports) | https://github.com/nyakaspeter/goodluckOS-mali-driver |

### Ports, apps and launchers

| Resource | Description | Link |
|----------|-------------|------|
| GA36 Ports | Download site for ports (Quake, Half-Life, Diablo, Undertale, Descent, Tomb Raider and more) | https://ga36.genserek.net/ |
| GA36 Ports help | Copying, updating and removing ports | https://ga36.genserek.net/help/ |
| ga36-ports source | Port sources and issue tracker | https://github.com/rincewindcz/ga36-ports |
| Kennel | Alternative launcher for goodluckOS | https://github.com/rincewindcz/kennel |
| glOSports-half-life | Half-Life 1 port | https://github.com/CodeZombie/glOSports-half-life |
| Support the port author | Buy rincewindcz a coffee | https://buymeacoffee.com/rcwnd |

### Other firmware for the GA36

| Resource | Description | Link |
|----------|-------------|------|
| Debianator | Debian 13 firmware for the GA36 | https://github.com/Bepok/Debianator |
| Negal75/goodluckOS | AI-assisted community fork for the Gaminja R36S (Allwinner A33). Not reviewed by this project. | https://github.com/Negal75/goodluckOS |

### Hardware identification and buying advice

| Resource | Description | Link |
|----------|-------------|------|
| R36S Clones (handhelds.wiki) | Clone families, how to identify a GA36 "fake", firmware per clone | https://handhelds.wiki/R36S_Clones |
| R36S models explained (TechTactician) | R36S vs R36XX, R36Plus, Max, Ultra and other clones | https://techtactician.com/r36s-vs-r36xx-r36plus-max-ultra-explained/ |
| R36S setup guide (Retro Handhelds) | SD card backup with Win32DiskImager, general clone advice | https://retrohandhelds.gg/r36s-setup-guide/ |
| r/R36S | Main community subreddit for R36S and clones | https://www.reddit.com/r/R36S/ |

> Note: older posts on r/R36S still say "no custom firmware exists for the GA36". That is outdated, goodluckOS now exists for it.

### Don't confuse with (different hardware)

These are for the Rockchip RK3326 R36S and clones. They do **not** run on the GA36-MB, but you will see them mentioned everywhere:

| Project | Link |
|---------|------|
| dArkOSRE-R36 | https://github.com/southoz/dArkOSRE-R36 |
| ArkOS4Clone | See the "Custom Firmware" section of https://handhelds.wiki/R36S_Clones |

### Tools and references

| Resource | Description | Link |
|----------|-------------|------|
| sunxi-tools | Allwinner tooling (FEL, script.bin utilities) | https://github.com/linux-sunxi/sunxi-tools |
| bootlin/mali-blobs | ARM's r6p2 Mali user-space builds (used by the Mali driver) | https://github.com/bootlin/mali-blobs |
| OpenMTP | MTP file transfer for macOS | https://openmtp.ganeshrvel.com/ |

---

## Disclaimer

The GNU GPL v2 covers this in more detail, but to reiterate: this software can permanently damage your hardware. You alone are responsible for all damages and their consequences resulting from using, or attempting to use, this software.

> This is a personal fork. No warranty. Use at your own risk. Not affiliated with the official goodluckOS project.

