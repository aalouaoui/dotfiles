#! /bin/bash
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &# Polkit fix, you can use lxsession or polkitd as well
gnome-keyring-daemon --start &
thunar --daemon &
picom &
dunst &
xfce4-clipman &
udiskie -ant & # Automount Removable media
nm-applet &
# blueman-applet & # Bluetooth
python /home/khalid/scripts/wall.py
nitrogen --restore &
