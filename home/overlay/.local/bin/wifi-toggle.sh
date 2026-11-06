#!/bin/sh
# goodluckOS Wi-Fi toggle (Option B equivalent)
# Toggles wlan0 for 350b:9101 dongle; uses wpa_supplicant if config exists.
WIFI_CONF="/home/player/.config/wpa_supplicant.conf"
LOG="/home/player/wifi-toggle.log"
echo "$(date -Iseconds) toggling wifi" >> "$LOG"
if ip link show wlan0 >/dev/null 2>&1 && ip link show wlan0 2>/dev/null | grep -q "<UP"; then
    echo "disabling wlan0" >> "$LOG"
    doas ip link set wlan0 down 2>/dev/null || ip link set wlan0 down
    doas killall wpa_supplicant 2>/dev/null || killall wpa_supplicant 2>/dev/null || true
else
    echo "enabling wlan0" >> "$LOG"
    doas ip link set wlan0 up 2>/dev/null || ip link set wlan0 up
    if [ -f "$WIFI_CONF="/home/player/.config/wpa_supplicant.conf"
        doas wpa_supplicant -B -i wlan0 -c "$WIFI_CONF="/home/player/.config/wpa_supplicant.conf"
    else
        echo "no $WIFI_CONF="/home/player/.config/wpa_supplicant.conf"
        doas iw wlan0 scan 2>/dev/null | head -20 >> "$LOG" || true
    fi
fi
echo "done" >> "$LOG"
