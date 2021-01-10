function fish_greeting
    echo ""
end

abbr --add --global p "paru"
abbr --add --global g "git"
abbr --add --global ls "lsd"
abbr --add --global la "lsd -a"
abbr --add --global ll "lsd -la"
abbr --add --global bat "bat -P"
abbr --add --global grep 'grep --color=auto'
abbr --add --global fgrep 'fgrep --color=auto'
abbr --add --global egrep 'egrep --color=auto'
abbr --add --global diff 'diff --color=auto'
abbr --add --global colorscript "/opt/shell-color-scripts/colorscript.sh"
abbr --add --global xephyr "Xephyr -br -ac -noreset -screen 1360x700 :1 &"
abbr --add --global ctl "sudo systemctl"
abbr --add --global n "nvim"
abbr --add --global icat "kitty +kitten icat --align=left"

