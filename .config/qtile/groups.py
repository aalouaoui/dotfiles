from libqtile.config import Group, Match

groups = [
    Group(name="1", label="WEB", matches=[Match(wm_class=["chromium", "firefox"])]),
    Group(name="2", label="DEV"),
    Group(name="3", label="TERM", layout="monadtall"),
    Group(name="4", label="SYS"),
    Group(name="5", label="MUS", matches=[Match(wm_class=["spotify", "Spotify"])]),
]
