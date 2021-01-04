from typing import List  # noqa: F401
from libqtile import layout, widget, bar, hook
from libqtile.config import Click, Drag, Key, Group, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
import subprocess
import os.path
# from libqtile.log_utils import logger # to write into ~/.local/share/qtile/qtile.log

# Custom Imports
from scripts import Spotify

###############
### My Vars ###
###############
spotify = Spotify()  # Create a class instance containing spotify functions
mod = "mod4"
ctrl = "control"
alt = "mod1"
shift = "shift"
HOME = os.path.expanduser("~/")
terminal = "alacritty"
launcher = HOME+"rofi/720p/bin/launcher_colorful"
powermenu = HOME+"rofi/720p/bin/powermenu"
file_manager = "thunar"
my_browser = "chromium --password-store=gnome"
code_editor = "code"
calculator = "qalculate-gtk"
meet_screenshot = HOME + "scripts/meet-screenshot.sh"
# screenshot = HOME + "scripts/screenshot.sh"
screenshot = "xfce4-screenshooter -r"

# For Widgets
ICON_DIR = HOME + ".config/qtile/icons/"
TELA_ICONS = "/usr/share/icons/Tela-blue-dark/"
left_sep = ""
sep = ""
right_sep = ""

#################
### My Colors ###
#################
colors = dict(
    layout_border="#3F51B5",
    bg="#080808",
    rofi="#ffffff",

    groups_bg="#3F51B5",
    groups_active="#ffffff",
    groups_highlight="#2D3A82",
    groups_highlight_color="#ffffff",
    groups_inactive="#cecece",

    tasklist_bg="#080808",

    sep="#ffffff",
    player_bg="#3F51B5",
    sensor_bg="#3F51B5",
    sensor_alert="#FF5959",
    lang_bg="#3F51B5",
    battery_bg="#3F51B5",
    volume_bg="#3F51B5",

    clock_bg="#3F51B5",
    clock_fg="#ffffff",
    layout_icon_bg="#ffffff",
)

###############
### Groups ####
###############
groups = [
    Group(name="1", label="WEB",
          matches=[Match(wm_class=["chromium", "firefox"])]),
    Group(name="2", label="DEV"),
    Group(name="3", label="TERM", layout="monadtall"),
    Group(name="4", label="SYS"),
    Group(name="5", label="MUS",
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
    Key([shift], "Print", lazy.spawn(screenshot), desc="Take Full Screenshot"),
    Key([], "Print", lazy.spawn(meet_screenshot), desc="Take Meet Screenshot"),
    Key([ctrl], "Escape", lazy.spawn("xkill"), desc="Run XKill"),

    # Qtile Controls
    Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Quit Qtile"),
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

layouts = [layout.Max(**layout_defaults), layout.MonadTall(**layout_defaults)]

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
    padding=0,
    margin=0
)

widgets = [
    widget.Image(
        background=colors["rofi"],
        filename=f"{ICON_DIR}manjaro.svg",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(launcher)},
    ),
    widget.TextBox(
        **separator_defaults,
        text=right_sep,
        background=colors["groups_bg"],
        foreground=colors["rofi"]
    ),
    widget.GroupBox(
        background=colors["groups_bg"],
        active=colors["groups_active"],
        block_highlight_text_color=colors["groups_highlight_color"],
        highlight_color=colors["groups_highlight"],
        highlight_method="line",
        borderwidth=0,
        rounded=False,
        disable_drag=True,
        inactive=colors["groups_inactive"],
        margin_y=3,
        margin_x=2,
        padding_x=8,
        fmt="<b>{}</b>",
    ),
    widget.TextBox(
        **separator_defaults,
        text=right_sep,
        foreground=colors["groups_bg"]
    ),
    widget.TaskList(
        background=colors["tasklist_bg"],
        border=colors["tasklist_bg"],
        borderwidth=2,
        highlight_method="block",
        # icon_size=20,
        margin_y=3,
        margin_x=3,
        padding_x=3,
        padding_y=3,
        spacing=0,
        # max_title_width=24,
        markup_floating="",
        markup_focused="",
        markup_maximized="",
        markup_minimized="",
        markup_normal="",

    ),
    widget.Systray(
        padding=5,
    ),
    widget.TextBox(
        text="  ",
    ),
    widget.TextBox(
        **separator_defaults,
        text=left_sep,
        background=colors["bg"],
        foreground=colors["player_bg"],
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
        background=colors["player_bg"],
        padding=5,
    ),
    widget.TextBox(
        **separator_defaults,
        text=sep,
        foreground=colors["sep"],
        background=colors["player_bg"],
    ),
    widget.KeyboardLayout(
        background=colors["lang_bg"],
        configured_keyboards=["us", "ar"],
        display_map={"us": "EN", "ar": "AR"},
        padding=5,
        fmt="<span font_family='Fira Code Nerd Font' size='larger'>韛 </span> {}",
    ),
    widget.TextBox(
        **separator_defaults,
        text=sep,
        foreground=colors["sep"],
        background=colors["lang_bg"],
    ),
    widget.ThermalSensor(
        background=colors["sensor_bg"],
        padding=5,
        fmt="<span font_family='Fira Code Nerd Font' size='larger'> </span>{}",
        tag_sensor="Package id 0",
        foreground_alert=colors["sensor_alert"],
        threshold=70,
    ),
    widget.TextBox(
        **separator_defaults,
        text=sep,
        foreground=colors["sep"],
        background=colors["sensor_bg"],
    ),
    widget.BatteryIcon(
        theme_path=TELA_ICONS+"24/panel/",
        background=colors["battery_bg"],
        mouse_callbacks={
            'Button4': lambda qtile: qtile.cmd_spawn('xbacklight -inc 10'),
            'Button5': lambda qtile: qtile.cmd_spawn('xbacklight -dec 10'),
        },
        update_interval=1
    ),
    widget.Backlight(
        backlight_name="intel_backlight",
        brightness_file="brightness",
        max_brightness_file="max_brightness",
        format='{percent:2.0%}',
        background=colors["battery_bg"],
        step=10,
        change_command="xbacklight -set {0}",
        update_interval=0.2,
    ),
    widget.TextBox(
        **separator_defaults,
        text=sep,
        foreground=colors["sep"],
        background=colors["battery_bg"],
    ),
    widget.Volume(
        step=5,
        padding=0,
        margin=0,
        theme_path=TELA_ICONS+"24/panel/",
        volume_app="pavucontrol",
        background=colors["volume_bg"],
    ),
    widget.Volume(
        step=5,
        padding=0,
        margin=0,
        volume_app="pavucontrol",
        fmt=" {0} ",
        background=colors["volume_bg"],
    ),
    widget.TextBox(
        **separator_defaults,
        text=sep,
        foreground=colors["sep"],
        background=colors["volume_bg"],
    ),
    widget.Clock(
        background=colors["clock_bg"],
        foreground=colors["clock_fg"],
        format='%d %B | %H:%M',
        fmt="<span font_family='Fira Code Nerd Font' size='larger'> </span> {}",
        padding=4,
    ),
    widget.TextBox(
        **separator_defaults,
        text=left_sep,
        background=colors["clock_bg"],
        foreground=colors["layout_icon_bg"],
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[ICON_DIR],
        padding=0,
        scale=0.6,
        background=colors["layout_icon_bg"],
    ),
]

screens = [
    Screen(top=bar.Bar(widgets, 28, background=colors["bg"]))
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
