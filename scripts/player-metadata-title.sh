#!/bin/bash
Status=$(playerctl status -f "{{lc(status)}}")
Title=$(playerctl metadata title)
TitleIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/tools-rip-audio-cd.svg"

TitleShort=${Title%(*}
#TitleShort=${TitleShort%·*}

if [[ (($Status == "playing" || $Status == "paused")) && (( -n $TitleShort )) ]]
then
	echo "<txt>  ${TitleShort::50}  </txt>"
	echo "<tool>$Title</tool>"
	echo "<img>$TitleIcon</img>"
else
	echo "<txt></txt>"
fi

