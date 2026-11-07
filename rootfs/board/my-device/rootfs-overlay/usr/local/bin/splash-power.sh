#!/bin/sh
# splash-power.sh poweroff|reboot|noop : show the exit splash, then act.
# Runs as player (member of group video, so /dev/fb0 is writable);
# the privileged step goes through doas, which only allows /sbin/poweroff|reboot.
img=/home/player/.local/share/goodluckos/splash-exit.png
if [ -f "$img" ] && command -v fbv >/dev/null 2>&1; then
    fbv -f "$img" >/dev/null 2>&1 || true
    sleep 1
fi
case "$1" in
    noop)   echo "noop ok" ;;
    reboot) exec doas /sbin/reboot ;;
    *)      exec doas /sbin/poweroff ;;
esac
