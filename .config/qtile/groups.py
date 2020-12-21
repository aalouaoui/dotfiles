from libqtile.config import Group, Match

groups = [
    Group("WEB", matches=[Match(wm_class=["chromium", "firefox"])]),
    Group("DEV"),
    Group("TERM", layout="monadtall"),
    Group("SYS"),
    Group("MUS", matches=[Match(wm_class=["spotify", "Spotify"])]),
]
