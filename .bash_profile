#
# ~/.bash_profile
#
export PAGER=most
[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ -n "$DESKTOP_SESSION" ];then
    eval $(gnome-keyring-daemon --start)
    export SSH_AUTH_SOCK
fi
