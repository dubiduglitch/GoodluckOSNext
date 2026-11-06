#!/bin/sh
# Boot the Kennel launcher by default; fall back to Puppy if it is missing.
if [ -x /home/player/ports/kennel/kennel ]; then
    exec /home/player/ports/kennel/kennel
fi
exec /usr/bin/puppy
