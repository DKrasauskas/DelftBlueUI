import os
import subprocess
import time
import platform
import sys
from python.utils import squeue as sq
import python.windows.windows as win
from python.asyncCP.update import FolderWatcher
from python.tables.tables import create_job_table, update_job_values, create_local_table, update_local_table_values
from python.utils.styles import *
from user import *


class Comm:
    def __init__(self):
        # initialize dpg and logo
        dpg.create_context()
        dpg.create_viewport(title="DelftBlue", width=1500, height=800)
        dpg.setup_dearpygui()
        self.width,  self.height,  self.channels,  self.data = dpg.load_image("backends/img.png")
        win.dblue_logo()

        #tables
        self.main_table = create_job_table()
        self.second_table = create_local_table()

        # create uplink/downlink table
        self.timer0, self.uplinkB, self.downlinkB, self.autosyncB = win.fetch_window()

        #setup sync
        if platform.system() == "Windows":
            self.func = self.sync_func_win
            self.downlink = sq.AsyncQueue(
                func=None,
                args=(
                    "powershell",
                    "-ExecutionPolicy", "Bypass",
                    "-File", "shell/windows/check_job_status.ps1",
                    "check2",
                    USER),
                interval=2
            )
        else:
            self.func = self.sync_func
            self.downlink = sq.AsyncQueue(
                func=None,
                args=("bash",
                      "shell/check_job_status.sh",
                      "check2",
                       USER),
                interval=2
            )
        self.downlink.start()
        self.status, self.sq1, self.sq2 = sq.get_queue() #get slurm queue
        self.cbtn,  self.cbtn1,  self.cbtn2 = win.console_window(self.second_table, self.status)
        self.watcher = FolderWatcher(os.getcwd(), self.func)

        # viewport and initialization times
        dpg.show_viewport()
        self.elapsed = time.time()

        # get the initial list of jobs
        self.jobfiles = self.get_jobfiles()
        update_local_table_values(self.second_table, self.jobfiles)
    def render(self):
        # main loop
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
            list, list2 = self.downlink.fetch()
            if list is not None:
                update_job_values(self.main_table, list, list2)
                print("fetched")
            dpg.set_value(self.timer0, f"Last fetch : {int(self.elapsed - win.FETCH_TIME)}s ago")
            self.elapsed = time.time()
        # destroy context
        dpg.destroy_context()

    def sync_func(self, caller, path):
        print(f"Syncing folder: {path}")
        print(f"{caller.sync_start_time}")
        subprocess.run(["bash", "shell/sync.sh", "send", USER])

    def sync_func_win(self, caller, path):
        print(f"Syncing folder: {path}")
        print(f"{caller.sync_start_time}")
        subprocess.run([
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "shell/windows/sync.ps1",
            "send",
            USER
        ])

    def get_jobfiles(self):
        subfolder_path = "remote"
        return os.listdir(subfolder_path)


