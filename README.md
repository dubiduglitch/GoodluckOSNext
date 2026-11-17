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
