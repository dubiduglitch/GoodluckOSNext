# goodluckOSNext

Fork personnel de [goodluckOS](https://github.com/CodeZombie/goodluckOS) par [dubiduglitch](https://github.com/dubiduglitch).

Ce repo est un **fork personnel**. Il n'est pas affilié au projet officiel goodluckOS et n'a pas vocation à le remplacer.

## 📦 Comptes & crédits

Tous les projets ci-dessous sont sous leurs licences respectives.

### Système d'exploitation (base)

| Projet | Auteur | Licence | Lien |
|--------|--------|---------|
| goodluckOS (base) | [CodeZombie](https://github.com/CodeZombie) | GPL-2.0 |
| Nouveaux noyaux (kernel) | [nyakaspeter](https://github.com/nyakaspeter) | GPL-2.0 |
| Buildroot | [Buildroot](https://buildroot.org/) | GPL-2.0 |

### Jeux & ports

| Projet | Auteur | Licence | Lien |
|--------|--------|---------|
| GTA III | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gta3-pc](https://github.com/nyakaspeter/glOSports-gta3-pc) |
| GTA Vice City | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavc-pc](https://github.com/nyakaspeter/glOSports-gtavc-pc) |
| GTA Liberty City Stories | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtalcs-pc](https://github.com/nyakaspeter/glOSports-gtalcs-pc) |
| GTA Vice City Stories | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-gtavcs-psp](https://github.com/nyakaspeter/glOSports-gtavcs-psp) |
| Hotline Miami | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami](https://github.com/nyakaspeter/glOSports-hotlinemiami) |
| Hotline Miami 2 | [nyakaspeter](https://github.com/nyakaspeter) | MIT | [glOSports-hotlinemiami2](https://github.com/nyakaspeter/glOSports-hotlinemiami2) |
| Stardew Valley (source) | [igol23](https://github.com/igol23) | GPL-2.0 | [glOSports-stardew-valley](https://github.com/igol23/glOSports-stardew-valley) |
| Stardew Valley (port) | [alvesmaicon](https://github.com/alvesmaicon) | MIT | [glOSports-stardew](https://github.com/alvesmaicon/goodluckOS-mali-driver) |
| Mediabox | [lw10a](https://github.com/lw10a) | AGPL-3.0 | [goodluckOS-mali-driver](https://github.com/lw10a/Mediabox-goodluckOS) |
| Arcade & émulateurs (30+) | [rincewindcz](https://github.com/rincewindcz) | MIT | [ga36-ports](https://github.com/rincewindcz/ga36-ports) |

### Lanceur & système

| Projet | Auteur | Licence | Lien |
|--------|--------|---------|
| Kennel (launcher) | [rincewindcz](https://github.com/rincewindcz) | MIT | [kennel](https://github.com/rincewindcz/kennel) |
| SDL | [libsdl](https://github.com/libsdl) | zlib | [libsdl.org](https://www.libsdl.org/) |
| Mesa / lima | [Mesa3D](https://mesa3d.org/) | MIT | [mesa3d.org](https://mesa3d.org/) |

## 📦 Comment flasher

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Remplacez `/dev/sdX` par votre carte SD.

## 🏗️ Build

Nécessite Docker. Voir `BUILD.md`.

---

> ⚠️ Ce projet est un **fork personnel**. Aucune garantie de fonctionnement. Utilisez à vos propres risques. Non affilié au projet goodluckOS officiel.
