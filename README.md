# goodluckOSNext

Personal fork of [goodluckOS](https://github.com/CodeZombie/goodluckOS) by [dubiduglitch](https://github.com/dubiduglitch).

This repo is a personal fork. It is not affiliated with the official goodluckOS project and does not aim to replace it.

---

## Target Console

This firmware is designed for portable **GA36-MB V1.2-20260416** consoles (often sold as "R36S" clones).

| Feature | Detail |
|---------|--------|
| SoC | Allwinner A23 (ARM Cortex-A7) |
| GPU | Mali-400 MP2 |
| RAM | 512 MB |
| Screen | 640 × 480 |
| Storage | microSD card (TF-1 primary, TF-2 optional on some models) |
| Connectivity | USB OTG (gadget: serial, MTP, network) |

This hardware is sold under various brands (R36S clone, Zekko, Tekko, etc.). No official driver is provided by the manufacturer for this hardware.

More info: [R36S Clones - handhelds.wiki](https://handhelds.wiki/R36S_Clones)

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
| SDL | libsdl | zlib | https://www.libsdl.org/ |
| Mesa / lima | Mesa3D | MIT | https://mesa3d.org/ |

## Installation

Flash the compressed image to your SD card:

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Replace `/dev/sdX` with your SD card device.

## Build

Requires Docker. See `BUILD.md`.

---

> This is a personal fork. No warranty. Use at your own risk. Not affiliated with the official goodluckOS project.
EOF
echo "README overwritten in English"