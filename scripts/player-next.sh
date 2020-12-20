#!/bin/bash
Status=$(playerctl status -f "{{lc(status)}}")
NextIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/media-skip-forward.svg"

if [[ $Status == "playing" || $Status == "paused" ]]; then
	echo "<txt> </txt>"
	echo "<img>$NextIcon</img>"
	echo "<tool>Next</tool>"
	echo "<click>playerctl next</click>"
else
	echo "<txt></txt>"
fi
