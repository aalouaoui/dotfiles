from typing import List  # noqa: F401
from libqtile import layout, widget, bar, hook, extension
from libqtile.config import Click, Drag, Key, Group, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
import subprocess
import os.path
# from libqtile.log_utils import logger # to write into ~/.local/share/qtile/qtile.log

# Custom Imports
from spotify_controls import SpotifyControls
from brightness_controls import BrightnessControl
from volume_controls import VolumeControl

###############
### My Vars ###
###############
# Create a class instance containing spotify functions
mod = "mod4"
ctrl = "control"
alt = "mod1"
shift = "shift"
HOME = os.path.expanduser("~/")
terminal = "kitty"
launcher = HOME+"rofi/720p/bin/launcher_colorful"
powermenu = HOME+"rofi/720p/bin/powermenu"
file_manager = "thunar"
my_browser = "chromium --password-store=gnome"
code_editor = "code"
editor = "kitty nvim"
sys_mon = "kitty htop"
calculator = "qalculate-gtk"
meet_screenshot = HOME + "scripts/meet-screenshot.sh"
ent_screenshot = HOME + "scripts/ent-screenshot.sh"
# screenshot = HOME + "scripts/screenshot.sh"
screenshot = "xfce4-screenshooter -r"

# For Widgets
# ICON_DIR = HOME + ".config/qtile/icons/"
TELA_ICONS = "/usr/share/icons/Tela-blue-dark/"

#################
### My Colors ###
#################


def fake_border(color, base="#080808"):
    return [color]*6+[base]*50


colors = dict(
    # New Ones
    bg=fake_border("#232323"),
    layout_border='#232323',
    groups_hl=fake_border("#3F3FB5", "#0F0F0F"),
    groups_active="#ffffff",
    groups_inactive="#aaaaaa",
    tabs_bg=fake_border("#3F8EB5", "#0F0F0F"),
    spotify_bg=fake_border("#3FB53F"),
    lang_bg=fake_border("#B53F8E"),
    sensor_bg=fake_border("#B53F3F"),
    sensor_alert="#B53F3F",
    brightness_bg=fake_border("#8EB53F"),
    volume_bg=fake_border("#8E3FB5"),
    clock_bg=fake_border("#3FB58E"),
    clock_fg="#ffffff",
    tray_bg="#080808",
)


def wrap_icon(icon, color):
    pango = f"<span font_family='Fira Code Nerd Font' size='larger' foreground='{colors[color][0]}'>{icon} </span>" + "{}"
    return pango

spotify = SpotifyControls(color=colors["spotify_bg"][0])
brightness = BrightnessControl(color=colors["brightness_bg"][0])
volume = VolumeControl(color=colors["volume_bg"][0])


###############
### Groups ####
###############
groups = [
    Group(name="1", label="1",
          matches=[Match(wm_class=["chromium", "firefox"])]),
    Group(name="2", label="2"),
    Group(name="3", label="3", layout="monadtall"),
    Group(name="4", label="4"),
    Group(name="5", label="5",
          matches=[Match(wm_class=["spotify", "Spotify"])]),
]

######################
### Keys and Mouse ###
######################

keys = [
    # Window Controls
    Key([mod], "w", lazy.layout.shuffle_up(), desc="Move Window Up"),
    Key([mod], "a", lazy.layout.shuffle_up(), desc="Move Window Left"),
    Key([mod], "s", lazy.layout.shuffle_down(), desc="Move Window Down"),
    Key([mod], "d", lazy.layout.shuffle_down(), desc="Move Window Right"),

    Key([mod, shift], "w", lazy.layout.grow(), desc="Grow Window"),
    Key([mod, shift], "s", lazy.layout.shrink(), desc="Shrink Window"),
    Key([mod, shift], "d", lazy.layout.reset(), desc="Reset Layout"),
    Key([mod], "space", lazy.layout.maximize(), desc="Maximize Window"),

    Key([alt], "Tab", lazy.layout.next(), desc="Next Window"),
    Key([alt, shift], "Tab", lazy.layout.previous(), desc="Previous Window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Switch Layout"),
    Key([mod], 'f', lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod, shift], 'f', lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"),
    Key([mod, ctrl], 'f', lazy.window.bring_to_front(),
        desc="Bring Window To Front"),
    Key([mod], "q", lazy.window.kill(), desc="Quit Window"),

    # Launching Apps
    Key([mod], "t", lazy.spawn(terminal), desc="Run terminal"),
    Key([mod], "r", lazy.spawn(launcher), desc="Run Rofi"),
    Key([mod], "x", lazy.spawn(powermenu), desc="Run Powermenu"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Run File Manager"),
    Key([mod], "b", lazy.spawn(my_browser), desc="Run Browser"),
    Key([mod], "c", lazy.spawn(code_editor), desc="Run Code Editor"),
    Key([mod], "m", lazy.spawn(calculator), desc="Run Calculator"),
    Key([mod], "n", lazy.spawn(editor), desc="Run Editor"),
    Key([mod], "Escape", lazy.spawn(sys_mon), desc="Run System Monitor"),
    Key([shift], "Print", lazy.spawn(screenshot), desc="Take Full Screenshot"),
    Key([ctrl], "Print", lazy.spawn(ent_screenshot), desc="Take ENT Screenshot"),
    Key([], "Print", lazy.spawn(meet_screenshot), desc="Take Meet Screenshot"),
    Key([ctrl], "Escape", lazy.spawn("xkill"), desc="Run XKill"),

    # Qtile Controls
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    # Key([mod, ctrl], "q", lazy.shutdown(), desc="Quit Qtile"),
    Key([ctrl, alt], "Delete", lazy.shutdown(), desc="Quit Qtile"),

    # Brightness Controls
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10"),
        desc="Brightness+"),
    Key([mod, ctrl], "Up", lazy.spawn("xbacklight -inc 10"), desc="Brightness+"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10"),
        desc="Brightness-"),
    Key([mod, ctrl], "Down", lazy.spawn("xbacklight -dec 10"),
        desc="Brightness-"),

    # Volume Controls
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"),
        desc="Mute Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-"),
        desc="Volume-"),
    Key([mod, ctrl], "Left", lazy.spawn("amixer -q set Master 5%-"),
        desc="Volume-"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+"),
        desc="Volume+"),
    Key([mod, ctrl], "Right", lazy.spawn("amixer -q set Master 5%+"),
        desc="Volume+"),

    # Media Controls
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),
        desc="Media Play/Pause"),
    Key([mod, shift], "Down", lazy.spawn("playerctl play-pause"),
        desc="Media Play/Pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Media Next"),
    Key([mod, shift], "Right", lazy.spawn("playerctl next"), desc="Media Next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"),
        desc="Media Previous"),
    Key([mod, shift], "Left", lazy.spawn("playerctl previous"),
        desc="Media Previous"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Media Stop"),
]

for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc=f"Show Group {group.label}"),
        Key([mod, shift], group.name,
            lazy.window.togroup(group.name, switch_group=True),
            desc=f"Send Window To Group {group.label}"),
    ])


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position(), desc="Drag Window"),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size(), desc="Resize Window"),
    Click([mod], "Button2", lazy.window.bring_to_front(),
          desc="Bring Window to Front")
]

###############
### Layouts ###
###############
layout_defaults = dict(
    margin=2,
    border_width=3,
    border_focus=colors["layout_border"],
    grow_amount=3,
)

floating_layout_defaults = dict(
    margin=2,
    border_width=1,
    border_focus=colors["layout_border"],
    grow_amount=1,
)

layouts = [layout.Max(**layout_defaults), layout.MonadTall(**layout_defaults), layout.MonadWide(**layout_defaults)]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wname': 'Picture-in-picture'},  # Chrome Picture in Picture
    {'wname': 'Picture in picture'},  # Chrome Picture in Picture
    {'wmclass': 'Qalculate-gtk'},  # Qalculate-gtk
    {'wmclass': 'gcolor3'},  # GColor3
    {'wmclass': 'pick-colour-picker'},  # Pick Colour Picker
    {'wmclass': 'kvantummanager'},  # Kvantum Manager
], **floating_layout_defaults)

###############
### Screens ###
###############
separator_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=21,
)

widget_defaults = dict(
    font='Noto Sans',
    fontsize=12,
    padding=6,
    margin=10,
)

widgets = [
    widget.GroupBox(
        active=colors["groups_active"],
        highlight_color=colors["groups_hl"],
        highlight_method="line",
        borderwidth=0,
        rounded=False,
        disable_drag=True,
        inactive=colors["groups_inactive"],
        margin_y=3,
        margin_x=0,
        padding=8,
        spacing=0,
    ),
    widget.TaskList(
        borderwidth=3,
        margin_y=0,
        margin_x=0,
        padding=6,
        highlight_method="block",
        border=colors["tabs_bg"],
        icon_size=0,  # Hide the icons
        markup_floating="<u>{}</u>",
        markup_minimized="<s>{}</s>",
        markup_focused="{}",
        markup_normal="<i>{}</i>",
        max_title_width=200,
        title_width_method="uniform",
        rounded=False,
        spacing=0,

    ),
    widget.GenPollText(
        func=spotify.get_info,
        mouse_callbacks={
            'Button1': spotify.do_action,
            'Button2': spotify.rm_def_groups,
            'Button4': spotify.previous,
            'Button5': spotify.next,
        },
        update_interval=1,
        background=colors["spotify_bg"],
    ),
    widget.KeyboardLayout(
        background=colors["lang_bg"],
        configured_keyboards=["us", "ar"],
        display_map={"us": "EN", "ar": "AR"},
        # fmt="<span font_family='Fira Code Nerd Font' size='larger'>韛 </span>{}",
        fmt=wrap_icon("韛", "lang_bg")
    ),
    widget.ThermalSensor(
        background=colors["sensor_bg"],
        fmt=wrap_icon("", "sensor_bg"),
        tag_sensor="Package id 0",
        foreground_alert=colors["sensor_alert"],
        threshold=75,
    ),
    widget.GenPollText(
        func=brightness.get_info,
        background=colors["brightness_bg"],
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn('xbacklight -d :0 -set 100'),
            'Button4': lambda qtile: qtile.cmd_spawn('xbacklight -d :0 -inc 10'),
            'Button5': lambda qtile: qtile.cmd_spawn('xbacklight -d :0 -dec 10'),
        },
        update_interval=1,
    ),
    widget.GenPollText(
        func=volume.get_info,
        background=colors["volume_bg"],
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn('amixer -q set Master toggle'),
            'Button3': lambda qtile: qtile.cmd_spawn('pavucontrol'),
            'Button4': lambda qtile: qtile.cmd_spawn('amixer -q set Master 5%+'),
            'Button5': lambda qtile: qtile.cmd_spawn('amixer -q set Master 5%-'),
        },
        update_interval=1,
    ),
    widget.Clock(
        background=colors["clock_bg"],
        foreground=colors["clock_fg"],
        format='%d %B | %H:%M',
        fmt=wrap_icon("", "clock_bg"),
        padding=4,
    ),
    widget.Systray(
        padding=5,
        background=colors["tray_bg"],
    ),
]

screens = [
    Screen(
        top=bar.Bar(widgets, 28, margin=[0, 0, 0, 0], background=colors["bg"])
    )
]

#############
### Hooks ###
#############


@hook.subscribe.startup_once
def autostart():
    subprocess.call([HOME+".config/qtile/autostart.sh"])

# Float windows that has size hints


@hook.subscribe.client_new
def floating_size_hints(window):
    hints = window.window.get_wm_normal_hints()
    if hints and 0 < hints['max_width'] < 1000:
        window.floating = True


#################
### WM Config ###
#################
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"
wmname = "LG3D"
