#!/bin/bash
Status=$(playerctl status -f "{{lc(status)}}")
PauseIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/media-pause.svg"
PlayIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/media-play.svg"

if [[ $Status == "playing" ]]; then
	echo "<txt> </txt>"
	echo "<img>$PauseIcon</img>"
	echo "<tool>Pause</tool>"
	echo "<click>playerctl play-pause</click>"
elif [[ $Status == "paused" ]]; then
	echo "<txt> </txt>"
	echo "<img>$PlayIcon</img>"
	echo "<tool>Play</tool>"
	echo "<click>playerctl play-pause</click>"
else
	echo "<txt></txt>"
fi

