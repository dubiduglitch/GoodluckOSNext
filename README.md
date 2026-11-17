# goodluckOSNext

Personal fork of [goodluckOS](https://github.com/CodeZombie/goodluckOS) by [dubiduglitch](https://github.com/dubiduglitch).

This repository is a **personal fork**. It is not affiliated with the official goodluckOS project and does not aim to replace it.

## History: from goodluckOS to goodluckOSNext

The starting point is [goodluckOS](https://github.com/CodeZombie/goodluckOS), a custom firmware for GA36-MB (Allwinner A23/A33) handhelds running Linux 7.2, RetroArch, Puppy launcher, and Mali-400 GPU driver.

On top of that base, this fork adds:

| Component | Author | License | Link |
|-----------|--------|---------|------|
| goodluckOS (base) | [CodeZombie](https://github.com/CodeZombie) | GPL-2.0 | [goodluckOS](https://github.com/CodeZombie/goodluckOS) |
| Mali-400 driver (kernel + userspace) | [nyakaspeter](https://github.com/nyakaspeter) | GPL-2.0 / ARM proprietary | [goodluckOS-mali-driver](https://github.com/nyakaspeter/goodluckOS-mali-driver) |
| GTA III port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gta3-pc](https://github.com/nyakaspeter/glOSports-gta3-pc) |
| GTA Vice City port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavc-pc](https://github.com/nyakaspeter/glOSports-gtavc-pc) |
| GTA Liberty City Stories port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtalcs-pc](https://github.com/nyakaspeter/glOSports-gtalcs-pc) |
| GTA Vice City Stories port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavcs-psp](https://github.com/nyakaspeter/glOSports-gtavcs-psp) |
| Hotline Miami port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami](https://github.com/nyakaspeter/glOSports-hotlinemiami) |
| Hotline Miami 2 port | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami2](https://github.com/nyakaspeter/glOSports-hotlinemiami2) |
| Stardew Valley (source) | [igol23](https://github.com/igol23) | GPL-2.0 | [glOSports-stardew-valley](https://github.com/igol23/glOSports-stardew-valley) |
| Stardew Valley (port) | [alvesmaicon](https://github.com/alvesmaicon) | MIT | [glOSports-stardew](https://github.com/alvesmaicon/goodluckOS-mali-driver) |
| Mediabox | [lw10a](https://github.com/lw10a) | AGPL-3.0 | [Mediabox-goodluckOS](https://github.com/lw10a/Mediabox-goodluckOS) |
| Arcade & emulators (30+) | [rincewindcz](https://github.com/rincewindcz) | MIT | [ga36-ports](https://github.com/rincewindcz/ga36-ports) |

### Launcher & system

| Project | Author | License | Link |
|---------|--------|---------|------|
| Kennel (launcher) | [rincewindcz](https://github.com/rincewindcz) | MIT | [kennel](https://github.com/rincewindcz/kennel) |
| SDL | [libsdl](https://github.com/libsdl) | zlib | [libsdl.org](https://www.libsdl.org/) |
| Mesa / lima | [Mesa3D](https://mesa3d.org/) | MIT | [mesa3d.org](https://mesa3d.org/) |

## 📦 How to flash

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Replace `/dev/sdX` with your SD card device.

## 🏗️ Build

Requires Docker. See `BUILD.md`.

---

> ⚠️ This is a **personal fork**. No warranty. Use at your own risk. Not affiliated with the official goodluckOS project.
