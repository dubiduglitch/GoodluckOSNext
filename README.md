# goodluckOSNext

Personal fork of [goodluckOS](https://github.com/CodeZombie/goodluckOS) by [dubiduglitch](https://github.com/dubiduglitch).

This is **not** an official distribution. It is a personal fork for my own GA36-MB console. It is not affiliated with the original project and does not intend to replace it.

## Credits

| Component | Source | License |
|-----------|--------|---------|
| goodluckOS (base system) | [CodeZombie/goodluckOS](https://github.com/CodeZombie/goodluckOS) | GPL-2.0 |
| Mali-400 kernel driver & userspace | [nyakaspeter/goodluckOS-mali-driver](https://github.com/nyakaspeter/goodluckOS-mali-driver) | GPL-2.0 / ARM proprietary |
| GTA III port | [nyakaspeter/glOSports-gta3-pc](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| GTA Vice City port | [nyakaspeter/glOSports-gtavc-pc](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| GTA Liberty City Stories port | [nyakaspeter/glOSports-gtalcs-pc](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| GTA Vice City Stories port | [nyakaspeter/glOSports-gtavcs-psp](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| Hotline Miami port | [nyakaspeter/glOSports-hotlinemiami](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| Hotline Miami 2 port | [nyakaspeter/glOSports-hotlinemiami2](https://github.com/nyakaspeter/goodluckOS-mali-driver) | MIT |
| Kennel launcher | [rincewindcz/kennel](https://github.com/rincewindcz/kennel) | MIT |
| Stardew Valley (source) | [igol23/glOSports-stardew-valley](https://github.com/igol23/glOSports-stardew-valley) | GPL-2.0 |
| Stardew Valley (binary port) | [alvesmaicon/glOSports-stardew](https://github.com/alvesmaicon/goodluckOS-mali-driver) | MIT |
| Mediabox | [lw10a/Mediabox-goodluckOS](https://github.com/lw10a/Mediabox-goodluckOS) | AGPL-3.0 |
| Arcade & other ports | [rincewindcz/ga36-ports](https://github.com/rincewindcz/ga36-ports) | MIT |

## How to flash

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Replace `/dev/sdX` with your SD card device.

## Build

Requires Docker. See `BUILD.md`.

---

> ⚠️ This is a personal fork. Use at your own risk. Not affiliated with the original goodluckOS project.
