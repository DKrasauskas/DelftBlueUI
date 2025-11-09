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
import jobConfigMenu as jcreate
from python.tables.tables import create_job_table, update_job_values, create_local_table, update_local_table_values
from python.windows.windows import dblue_logo
from update import FolderWatcher

status, result = sq.get_queue()
dpg.create_context()
dpg.create_viewport(title="DelftBlue", width=1500, height=800)
dpg.setup_dearpygui()
width, height, channels, data = dpg.load_image("backends/img.png")

from styles import *
from python.windows import *
from python.tables import *

def get_jobfiles():
    subfolder_path = "job_data"
    return [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]


def submit_handle(source, app_data, user_data):
    print(f"cancelling {user_data}")
    dpg.configure_item(source, label="TERMINATED")
    dpg.bind_item_theme(source, theme=red_button_theme)
    subprocess.run(
        ["bash", "shell/cancel.sh", "terminate", user_data]
    )


def console_open_handle(source, app_data, user_data):
    subprocess.Popen(["konsole",  "-e", "/home/dominykas/PycharmProjects/PythonProject/DBinterface/shell/connect.sh", "A"])

def job_creator_open_handle(source, app_data, user_data):
    jcreate.create_window()

dblue_logo()

main_table = create_job_table()
second_table = create_local_table()

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
    cbtn3 = dpg.add_button(
        label="New Job",
        width=160,
        height=30,
        callback=job_creator_open_handle,
        pos=(-1, 59)
    )
    dpg.bind_item_theme(cbtn2, theme=red_button_theme)

with dpg.window(label="SyncTime", no_title_bar=True, no_resize=True, no_move=True,
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
    cbtn3 = dpg.add_button(
        label="New Job",
        width=160,
        height=30,
        callback=job_creator_open_handle,
        pos=(-1, 59)
    )
    dpg.bind_item_theme(cbtn2, theme=red_button_theme)


def send_directory(self, path):
    subprocess.run(["bash", "shell/sync.sh", "send"])

def receive_directory(self, path):
    subprocess.run(["bash", "shell/sync.sh", "retrieve"])

with dpg.window(label="FloatAdjuster", no_title_bar=True, no_resize=True, no_move=True,
                no_scrollbar=True, width=300, height=200, pos=(300, 500)):
    # Float value display
    timer0 = dpg.add_text(f"Last fetch : {1}", tag="float_display", pos=(0, 0))

    # Increase button
    up_btn = dpg.add_button(label="->", width=40, height=30, pos=(0, 40),
                            callback=send_directory, user_data=0)

    # Decrease button
    down_btn = dpg.add_button(label="<-", width=40, height=30, pos=(0, 80),
                              callback=receive_directory, user_data=0)

# main loop
dpg.show_viewport()
elapsed = time.time()
downlink = sq.AsyncQueue(func=None, args=("bash", "shell/check_job_status.sh", "check"))
downlink.start()
folder = os.getcwd()
def my_sync(self, path):
    print(f"Syncing folder: {path}")
    print(f"{self.sync_start_time}")
    subprocess.run(["bash", "shell/sync.sh", "send"])

watcher = FolderWatcher(folder, my_sync)
#watcher.start()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    list = downlink.fetch()
    if list is not None:
        update_job_values(main_table, list)
        #time_downlink = time.time() - watcher.event_handler.sync_start_time
        #dpg.set_value(timer0, f"Last fetched {int(time_downlink)} s ago")


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




