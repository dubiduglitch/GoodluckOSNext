# goodluckOSNext

Fork personnel de [goodluckOS](https://github.com/CodeZombie/goodluckOS) par [dubiduglitch](https://github.com/dubiduglitch).

Ce repo est un fork personnel. Il n'est pas affilié au projet officiel goodluckOS et n'a pas vocation à le remplacer.

---

## Target Console

This firmware targets the **GA36-MB V1.2-20260416** handheld console (often sold as "R36S" clone).

| Feature | Detail |
|---------|--------|
| SoC | Allwinner A23 (ARM Cortex-A7) |
| GPU | Mali-400 MP2 |
| RAM | 512 MB |
| Screen | 640 x 480 |
| Storage | microSD card (TF-1 primary, TF-2 optional on some models) |
| Connectivity | USB OTG (gadget: serial, MTP, network) |

This hardware is sold under various brands (R36S clone, Zekko, Tekko, etc.). No official driver is provided by the manufacturer for this hardware.

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