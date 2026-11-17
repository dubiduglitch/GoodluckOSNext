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
- [Troubleshooting](#troubleshooting)
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
| Puppy (default launcher) | CodeZombie | GPL-2.0 | https://github.com/CodeZombie/goodluckOS |
| SDL | libsdl | zlib | https://www.libsdl.org/ |
| Mesa / lima | Mesa3D | MIT | https://mesa3d.org/ |

---

## Installation

Flash the compressed image to your SD card:

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Replace `/dev/sdX` with your SD card device. Double-check it with `lsblk` first: `dd` will overwrite whatever you point it at.

Then:

1. Put the card in **TF-1 (the OS slot)**.
2. Power on. Boot takes about 10 seconds.
3. If the screen stays black or garbled, the panel may be the other supported type. Upstream notes there is currently no way to tell panels apart in advance, so try both images from the Firmware Builder.

Windows users can flash with [balenaEtcher](https://etcher.balena.io/) or [Rufus](https://rufus.ie/) instead of `dd` (decompress the `.zst` first with [7-Zip](https://www.7-zip.org/) or `zstd`).

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

### USB serial console

Plug into a Linux PC via the OTG port, then:

```bash
sudo screen /dev/ttyACM* 115200
```

Default login: `root` / `root`. Change the password if you expose the device to anything beyond your own desk.

### Ports (games)

Download a port from [GA36 Ports](https://ga36.genserek.net/), unzip it, and copy the `ports` and `.local` folders into the root of `HOME` (`.local` is hidden on Linux and macOS). Ports appear in the **Ports** category of Kennel or Puppy. Updating means unzipping over the old version (saves are kept). Removing means deleting `ports/<port>`, `.local/share/applications/<port>.puppy` and `.local/share/icons/<port>.png`.

Ports marked "needs your own game files" do not include commercial game data. Bring your own legal copy.

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| Black screen / no reaction | Card in TF-1? Image built for your board revision? Try the other panel build. |
| Port not in the menu | Make sure `.local` was copied, then restart the console. |
| Port quits immediately | Read `ports/<port>/run.log`. It is usually missing game files. |
| Emulators crash or show a black screen after many game launches | The display memory pool fragments over time (a known lima leak, roughly 60-80 launches per boot). Reboot. |
| exFAT second card not detected | Reformat the card as FAT32. |
| Anything else | Open an issue with your board ID, the goodluckOS version and any logs. |

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
| Negal75/goodluckOS | AI-assisted community fork for the Gaminja R36S (Allwinner A33) | https://github.com/Negal75/goodluckOS |

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
| balenaEtcher | Cross-platform SD card flasher | https://etcher.balena.io/ |

---

## Disclaimer

The GNU GPL v2 covers this in more detail, but to reiterate: this software can permanently damage your hardware. You alone are responsible for all damages and their consequences resulting from using, or attempting to use, this software.

> This is a personal fork. No warranty. Use at your own risk. Not affiliated with the official goodluckOS project.
