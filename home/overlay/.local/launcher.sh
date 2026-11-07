#!/bin/sh
# Full-screen boot splash (start.png) before Kennel, then Kennel or Puppy fallback.
SPLASH=/home/player/.local/share/goodluckos/splash-boot.png

# Hide the VT cursor so no blinking caret shows through the splash.
printf '\033[2J\033[H\033[?25l' >/dev/tty1 2>/dev/null

if [ -f "$SPLASH" ] && command -v fbv >/dev/null 2>&1; then
    # -c: keep the image on screen after fbv exits (no black flash)
    # -f: shrink only if the image is larger than the panel
    fbv -u -c -f "$SPLASH" </dev/null >/dev/null 2>&1
fi

if [ -x /home/player/ports/kennel/kennel ]; then
    exec /home/player/ports/kennel/kennel
fi
exec /usr/bin/puppy
