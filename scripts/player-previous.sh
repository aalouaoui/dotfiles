#!/bin/bash
Status=$(playerctl status -f "{{lc(status)}}")
PreviousIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/media-skip-backward.svg"

if [[ $Status == "playing" || $Status == "paused" ]]; then
	echo "<txt> </txt>"
	echo "<img>$PreviousIcon</img>"
	echo "<tool>Previous</tool>"
	echo "<click>playerctl previous</click>"
else
	echo "<txt></txt>"
fi

