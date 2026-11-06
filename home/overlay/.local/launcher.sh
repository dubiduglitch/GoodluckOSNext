#!/bin/sh
# Clean loading splash (640x480) before Kennel, then boot Kennel or Puppy fallback
if [ -f /home/player/.local/share/goodluckos/splash-launch.png ] && command -v fbv >/dev/null 2>&1; then
    fbv -f /home/player/.local/share/goodluckos/splash-launch.png >/dev/null 2>&1 &
fi
if [ -x /home/player/ports/kennel/kennel ]; then
    exec /home/player/ports/kennel/kennel
fi
exec /usr/bin/puppy
