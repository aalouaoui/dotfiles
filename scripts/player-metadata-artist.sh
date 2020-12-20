#!/bin/bash
Status=$(playerctl status -f "{{lc(status)}}")
Artist=$(playerctl metadata artist)
ArtistIcon="/home/khalid/.local/share/icons/Tela-dark/16/actions/view-media-artist.svg"

ArtistShort=${Artist%%,*}

if [[ (($Status == "playing" || $Status == "paused")) && (( -n $ArtistShort )) ]]
then
	echo "<txt>  ${ArtistShort::20}</txt>"
	echo "<tool>$Artist</tool>"
	echo "<img>$ArtistIcon</img>"
else
	echo "<txt></txt>"
fi

