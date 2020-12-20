#!/usr/bin/bash
# mogrify -crop 1053x591+47+177 "*.jpg"
# scrot -a x,y,w,h
mkdir ~/Desktop/meet-screenshots/
scrot -a 47,177,1053,591 ~/Desktop/meet-screenshots/%Y-%m-%d-%H:%M:%S.png
notify-send "Meet Screenshot saved" --icon=zoom-best-fit
