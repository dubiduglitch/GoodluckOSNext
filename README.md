# goodluckOSNext

Fork personnel de [goodluckOS](https://github.com/CodeZombie/goodluckOS) par [dubiduglitch](https://github.com/dubiduglitch).

Ce repo est un **fork personnel**. Il n'est pas affilié au projet officiel goodluckOS et n'a pas vocation à le remplacer.

---

## Console cible

Ce firmware est destiné aux consoles portables **GA36-MB V1.2-20260416** (souvent vendues comme clones "R36S").

| Caractéristique | Détail |
|-----------------|--------|
| SoC | Allwinner A23 (ARM Cortex-A7) |
| GPU | Mali-400 MP2 |
| RAM | 512 MB |
| Écran | 640 × 480 |
| Stockage | Carte microSD (TF-1 principale, TF-2 optionnelle selon les modèles) |
| Connectivité | USB OTG (gadget : série, MTP, réseau) |

Ce matériel est vendu sous diverses marques (R36S clone, Zekko, Tekko, etc.). Aucun pilote officiel n'est fourni par le constructeur pour ce matériel.

---

## Composants

| Composant | Auteur | Licence | Lien |
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

## Awesome goodluckOS

Ressources communautaires et ressources officielles :

- [goodluckOS official docs](https://github.com/CodeZombie/goodluckOS/blob/main/README.md) — documentation officielle du projet goodluckOS
- [goodluckOS SOFTWARE.md](https://github.com/CodeZombie/goodluckOS/blob/main/SOFTWARE.md) — liste des ports et logiciels disponibles
- [goodluckOS-mali-driver README](https://github.com/nyakaspeter/goodluckOS-mali-driver/blob/main/README.md) — documentation du pilote Mali-400 et des ports de jeux
- [ga36.genserek.net](https://ga36.genserek.net/) — ports et applications pour goodluckOS par rincewindcz

---

> This is a **personal fork**. No warranty. Use at your own risk. Not affiliated with the official goodluckOS project.
EOF
echo "README overwritten in clean English"