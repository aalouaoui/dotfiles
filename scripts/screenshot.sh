#!/usr/bin/bash
# mogrify -crop 1053x591+47+177 "*.jpg"
# scrot -a x,y,w,h
mkdir ~/Desktop/screenshots/
scrot ~/Desktop/screenshots/%Y-%m-%d-%H:%M:%S.png
notify-send "Screenshot saved" --icon=zoom-best-fit
