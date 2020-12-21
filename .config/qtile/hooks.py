from libqtile import hook
# from libqtile.log_utils import logger # to write into ~/.local/share/qtile/qtile.log
import subprocess
from keys import HOME

@hook.subscribe.startup_once
def autostart():
    subprocess.call([HOME+".config/qtile/autostart.sh"])
