# goodluckOSNext

Fork personnel de [goodluckOS](https://github.com/CodeZombie/goodluckOS) par [dubiduglitch](https://github.com/dubiduglitch).

Ce repo est un fork personnel. Il n'est pas affilié au projet officiel goodluckOS et n'a pas vocation à le remplacer.

---

## Composants

| Composant | Auteur | Licence | Lien |
|-----------|--------|---------|------|
| goodluckOS (base) | [CodeZombie](https://github.com/CodeZombie) | GPL-2.0 | [goodluckOS](https://github.com/CodeZombie/goodluckOS) |
| Mali-400 driver (kernel + userspace) | [nyakaspeter](https://github.com/nyakaspeter) | GPL-2.0 / ARM proprietary | [goodluckOS-mali-driver](https://github.com/nyakaspeter/goodluckOS-mali-driver) |
| GTA III | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gta3-pc](https://github.com/nyakaspeter/glOSports-gta3-pc) |
| GTA Vice City | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavc-pc](https://github.com/nyakaspeter/glOSports-gtavc-pc) |
| GTA Liberty City Stories | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtalcs-pc](https://github.com/nyakaspeter/glOSports-gtalcs-pc) |
| GTA Vice City Stories | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavcs-psp](https://github.com/nyakaspeter/glOSports-gtavcs-psp) |
| Hotline Miami | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami](https://github.com/nyakaspeter/glOSports-hotlinemiami) |
| Hotline Miami 2 | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami2](https://github.com/nyakaspeter/glOSports-hotlinemiami2) |
| Stardew Valley (source) | [igol23](https://github.com/igol23) | GPL-2.0 | [glOSports-stardew-valley](https://github.com/igol23/glOSports-stardew-valley) |
| Stardew Valley (port) | [alvesmaicon](https://github.com/alvesmaicon) | MIT | [glOSports-stardew](https://github.com/alvesmaicon/glOSports-stardew) |
| Mediabox | [lw10a](https://github.com/lw10a) | AGPL-3.0 | [Mediabox-goodluckOS](https://github.com/lw10a/Mediabox-goodluckOS) |
| Arcade & emulators (30+) | [rincewindcz](https://github.com/rincewindcz) | MIT | [ga36-ports](https://github.com/rincewindcz/ga36-ports) |

### Launcher et système

| Projet | Auteur | Licence | Lien |
|--------|--------|---------|------|
| Kennel (launcher) | [rincewindcz](https://github.com/rincewindcz) | MIT | [kennel](https://github.com/rincewindcz/kennel) |
| SDL | [libsdl](https://github.com/libsdl) | zlib | [libsdl.org](https://www.libsdl.org/) |
| Mesa / lima | [Mesa3D](https://mesa3d.org/) | MIT | [mesa3d.org](https://mesa3d.org/) |

---

## Installation

L'image est fournie au format compressé zstd. Pour la flasher sur une carte SD :

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Remplacez `/dev/sdX` par le périphérique de votre carte SD.

---

## Build

Le système se construit avec Docker. Voir le fichier `BUILD.md` à la racine du dépôt.

---

> Ce dépôt est un fork personnel. Il n'est pas affilié au projet goodluckOS officiel. Aucune garantie de fonctionnement. Utilisez à vos propres risques.
EOF
echo "README mis à jour"