#!/bin/sh
# splash-power.sh poweroff|reboot : show the exit splash, then act
img=/home/player/.local/share/goodluckos/splash-exit.png
if [ -f "$img" ] && command -v fbv >/dev/null 2>&1; then
    fbv -f "$img" >/dev/null 2>&1 || true
    sleep 1
fi
case "$1" in
    reboot) exec /sbin/reboot ;;
    *)      exec /sbin/poweroff ;;
esac
