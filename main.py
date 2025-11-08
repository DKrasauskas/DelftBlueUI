import datetime

import dearpygui.dearpygui as dpg
from PIL import Image
import os
import paramiko
import select
import sys
import subprocess
import time
import squeue as sq

list = sq.get_queue()
result = subprocess.run(
    ["bash", "shell/check_job_status.sh", "check"],
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)

dpg.create_context()
dpg.create_viewport(title="DelftBlue", width=1500, height=800)
dpg.setup_dearpygui()
width, height, channels, data = dpg.load_image("backends/img.png")



with dpg.theme() as teal_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 150, 150, 255])        # button background
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 100, 100, 255])  # active/pressed
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])

with dpg.theme() as red_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [200, 0, 0, 255])       # button background
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [150, 0, 0, 255])
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])      # text color

with dpg.theme() as green_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 180, 100, 255])         # normal
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 130, 80, 255])    # active
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])

with dpg.theme() as delftblue_theme:
    with dpg.theme_component(dpg.mvButton):
        # Using RGBA approximation from the uploaded image
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 180, 255, 255])        # normal
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [50, 210, 255, 255]) # hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 150, 220, 255])   # active
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])         # text


def cancel_handle(source, app_data, user_data):
    print(f"cancelling {user_data}")
    dpg.configure_item(source, label="TERMINATED")
    dpg.bind_item_theme(source, theme=red_button_theme)
    subprocess.run(
        ["bash", "shell/cancel.sh", "terminate", user_data]
    )

def console_open_handle(source, app_data, user_data):
    subprocess.Popen(["konsole",  "-e", "/home/dominykas/PycharmProjects/PythonProject/DBinterface/shell/connect.sh"])


with dpg.texture_registry():
    texture_id = dpg.add_static_texture(width, height, data)


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

with dpg.window(label="A", no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, width=800, height=height, pos=(500, 100)):
    main_table = dpg.add_table(tag="main_table", header_row=True,
                               policy=dpg.mvTable_SizingFixedFit,
                               row_background=True,
                               reorderable=True,
                               resizable=True,
                               no_host_extendX=False,
                               hideable=True,
                               borders_innerV=True,
                               delay_search=True,
                               borders_outerV=True,
                               borders_innerH=True,
                               borders_outerH=True)



with dpg.window(label="Console", no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, width=160, height=80, pos=(100, 500)):
    cbtn = dpg.add_button(
        label="Open Remote Console",
        width=160,
        height=30,
        callback=console_open_handle,
        pos=(-1, -1)
    )
    dpg.bind_item_theme(cbtn, theme=delftblue_theme)
    cbtn2 = dpg.add_button(
        label="Open Local Console",
        width=160,
        height=30,
        callback=console_open_handle,
        pos=(-1, 29)
    )
    dpg.bind_item_theme(cbtn2, theme=red_button_theme)


def update_table_values():
    dpg.delete_item(main_table, children_only=True)
    for i in range(len(list[0]) + 1):
        if i == 0:
            dpg.add_table_column(label="Status", width_fixed=True, parent=main_table)
        dpg.add_table_column(label=list[0][i - 1], width_fixed=True, parent=main_table)

    for i in range(0, len(list)):
        with dpg.table_row(parent=main_table):
            for j in range(0, len(list[i]) + 1):
                status = "AWAIT"
                theme = teal_button_theme
                try:
                    exec_time = list[i][5]
                    state = list[i][4]
                    if state == "CG":
                        status = "TERMINATED"
                        theme = red_button_theme
                    elif state == "PD":
                        theme = teal_button_theme
                    else:
                        datetime.datetime.strptime(exec_time, "%M:%S")
                        theme = green_button_theme
                        status = "RUNNING"

                except ValueError:
                    theme = teal_button_theme

                if j == 0:
                    cbtn = dpg.add_button(
                        label=status,
                        width=80,
                        height=30,
                        callback=cancel_handle,
                        user_data=f"{list[i][j]}",
                    )
                    dpg.bind_item_theme(cbtn, theme=theme)
                else:
                    dpg.add_text(f"{list[i][j - 1]}", tag=f"{j + i * len(list[i])}")
# main loop
dpg.show_viewport()
elapsed = time.time()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    if int(elapsed) % 5 == 0:
        list = sq.get_queue()
        update_table_values()

    elapsed = time.time()

dpg.destroy_context()

# private_key_path = '/home/dominykas/.ssh/id_ed25519'
# pkey =  paramiko.Ed25519Key.from_private_key_file(private_key_path)
# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
#
# ssh.connect.sh(
#     hostname='login.delftblue.tudelft.nl',
#     port=22,
#     username='dkrasauskas',
#     pkey=pkey
# )
# chan = ssh.invoke_shell(term='xterm')




