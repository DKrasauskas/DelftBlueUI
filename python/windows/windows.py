import time
import subprocess
from python.utils.styles import*
from python.tables import jobConfigMenu as jcreate
from user import *

FETCH_TIME = time.time()
AUTOSYNC = False


def send_directory(self, path):
    global FETCH_TIME
    FETCH_TIME = time.time()
    subprocess.run(["bash", "shell/sync.sh", "send", USER])

def receive_directory(self, path):
    global FETCH_TIME
    FETCH_TIME = time.time()
    subprocess.run(["bash", "shell/sync.sh", "retrieve", USER])

def autosync(sender, app_data):
    global AUTOSYNC
    AUTOSYNC = app_data

def dblue_logo():
    width, height, channels, data = dpg.load_image("backends/img.png")
    #register texture
    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    #register fonts
    with dpg.font_registry():
        title_font = dpg.add_font("backends/Freedom-10eM.ttf", 34)

    with dpg.window(label="", no_title_bar=True, no_resize=True, no_move=True,
                no_scrollbar=True, width=width, height=height, pos=(100, 100)):
        dpg.add_image(texture_id, pos=(-1, -1))
        #dpg.bind_font(title_font)
    with dpg.window(label="T", no_title_bar=True, no_resize=True, no_move=True,
                    no_scrollbar=True, width=width, height=100, pos=(100, height + 100), no_background=True):
        title = dpg.add_text("Delft Blue", tag="custom_text")
        dpg.bind_item_font(title, title_font)
    return texture_id, width, height, channels, data

def fetch_window():
    # Define color themes (optional)
    with dpg.theme(tag="button_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 125, 245, 200))     # soft blue
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (65, 145, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (35, 105, 235, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme(tag="checkbox_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (45, 125, 245, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    # --- Main window ---
    with dpg.window(label="FloatAdjuster",
                    no_title_bar=True,
                    no_resize=True,
                    no_move=True,
                    no_scrollbar=True,
                    width=280,
                    height=250,
                    pos=(190, 500),
                    tag="float_adjust_window"):
        dpg.add_spacer(height=8)

        # Section title
        dpg.add_text("Data Synchronization", bullet=False)
        dpg.add_separator()
        dpg.add_spacer(height=4)

        # Last fetch display
        timer0 = dpg.add_text("Last fetch: 1", tag="float_display")
        dpg.bind_item_theme(timer0, theme="checkbox_theme")

        dpg.add_spacer(height=8)

        # Buttons laid out horizontally
        with dpg.group(horizontal=True):
            up_btn = dpg.add_button(label="Uplink", width=130, height=35,
                                    callback=send_directory, user_data=0)
            down_btn = dpg.add_button(label="Downlink", width=130, height=35,
                                      callback=receive_directory, user_data=0)

        dpg.bind_item_theme(up_btn, theme="button_theme")
        dpg.bind_item_theme(down_btn, theme="button_theme")

        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_spacer(height=8)

        # AutoSync checkbox centered
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=80)
            autosync_button = dpg.add_checkbox(label="Enable AutoSync",
                                               default_value=False,
                                               callback=autosync)
            dpg.bind_item_theme(autosync_button, theme="checkbox_theme")

        dpg.add_spacer(height=6)
        dpg.add_text("Status: Waiting...", tag="sync_status", color=(180, 180, 180))

    return timer0, up_btn, down_btn, autosync_button


def console_open_handle(source, app_data, user_data):
    subprocess.Popen(["konsole",  "-e", "/home/dominykas/PycharmProjects/PythonProject/DBinterface/shell/connect.sh", "A", USER])

def console_open_handle_local(source, app_data, user_data):
    subprocess.Popen(["konsole"])



def job_creator_open_handle(source, app_data, user_data):
    jcreate.create_window()

def console_window(table, status):
    # --- Optional: local button themes ---
    with dpg.theme(tag="blue_button_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (40, 100, 220, 230))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (60, 130, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (25, 90, 200, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme(tag="red_button_theme_local"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (180, 40, 40, 230))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (200, 60, 60, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (150, 30, 30, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme(tag="green_button_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (40, 160, 90, 230))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (60, 190, 120, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (30, 140, 80, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 6, category=dpg.mvThemeCat_Core)

    with dpg.window(label="SyncTime",
                    no_title_bar=True,
                    no_resize=True,
                    no_move=True,
                    no_scrollbar=True,
                    width=180,
                    height=250,
                    pos=(10, 500),
                    tag="console_window"):
        if status:
            cbtn3 = dpg.add_button(label="Connected",
                                   width=-1, height=35,
                                   callback=None, user_data=table)
            dpg.bind_item_theme(cbtn3, theme="green_button_theme")
        else:
            cbtn3 = dpg.add_button(label="Not Connected",
                                   width=-1, height=35,
                                   callback=None, user_data=table)
            dpg.bind_item_theme(cbtn3, theme="red_button_theme_local")

        dpg.add_spacer(height=6)
        dpg.add_text("Console Control", bullet=False)
        dpg.add_separator()
        dpg.add_spacer(height=6)

        # Group buttons vertically with padding
        with dpg.group(horizontal=False):
            cbtn = dpg.add_button(label="Open Remote Console",
                                  width=-1, height=35,
                                  callback=console_open_handle)
            dpg.bind_item_theme(cbtn, theme="blue_button_theme")

            cbtn2 = dpg.add_button(label="Open Local Console",
                                   width=-1, height=35,
                                   callback=console_open_handle_local)
            dpg.bind_item_theme(cbtn2, theme="red_button_theme_local")

        dpg.add_spacer(height=6)
        dpg.add_separator()

    return cbtn, cbtn2, cbtn3
