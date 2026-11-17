# goodluckOSNext

Fork personnel de [goodluckOS](https://github.com/CodeZombie/goodluckOS) par [dubiduglitch](https://github.com/dubiduglitch).

Ce n'est **pas** une distribution officielle. C'est un fork personnel contenant des modifications, des ports de jeux et des expérimentations faites par moi-même. Il n'est pas affilié au projet original et n'a pas vocation à le remplacer.

## Ce qui est inclus

- **goodluckOS** (base système) — sous licence GPL-2.0, provenant de [nyakaspeter/goodluckOS](https://github.com/nyakaspeter/goodluckOS) / [CodeZombie/goodluckOS](https://github.com/CodeZombie/goodluckOS)
- **Patches kernel** : Mali-400, framebuffer, CPU OPP jusqu'à 1,008 GHz, détection casque, etc.
- **Ports de jeux** : N64, PSP, GBA, SNES, PSX, Dreamcast, NES, GB, GBA, MegaDrive, Arcade, et bien d'autres (via [ga36-ports](https://github.com/rincewindcz/ga36-ports))
- **Stardew Valley** (version binaire de [nyakaspeter/glOSports-stardew](https://github.com/alvesmaicon/goodluckOS-mali-driver) / source de [nyakaspeter/glOSports-stardew-valley](https://github.com/nyakaspeter/goodluckOS-mali-driver))
- **Mediabox** (musique, livres, vidéos)

## Comment flasher

L'image finale se trouve dans les releases GitHub ou dans le dossier `out/` après build :

```bash
zstd -d -c goodluckOSNext.img.zst | sudo dd of=/dev/sdX bs=4M status=progress
```

Remplacez `/dev/sdX` par votre carte SD.

## Build

Nécessite Docker. Voir `BUILD.md`.

---

> ⚠️ Ce projet est un fork personnel. Aucune garantie de fonctionnement. Utilisez à vos propres risques.
