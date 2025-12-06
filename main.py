import os
import subprocess
import time
from python.utils import squeue as sq
import python.windows.windows as win
from python.asyncCP.update import FolderWatcher
from python.tables.tables import create_job_table, update_job_values, create_local_table, update_local_table_values
from python.utils.styles import *
from user import *

def get_jobfiles():
    subfolder_path = "remote"
    return os.listdir(subfolder_path)

def sync_func(self, path):
    print(f"Syncing folder: {path}")
    print(f"{self.sync_start_time}")
    subprocess.run(["bash", "shell/sync.sh", "send", USER])

dpg.create_context()
dpg.create_viewport(title="DelftBlue", width=1500, height=800)
dpg.setup_dearpygui()
width, height, channels, data = dpg.load_image("backends/img.png")

#initialize logo
win.dblue_logo()

#create remote job table
main_table = create_job_table()

#create local job table
second_table = create_local_table()

#create uplink/downlink table
timer0, uplinkB, downlinkB, autosyncB = win.fetch_window()

#asyncCP downlink / uplink for job squeue fetching from remote
downlink = sq.AsyncQueue(func=None, args=("bash", "shell/check_job_status.sh", "check2", USER), interval=2)
downlink.start()
sts, sq1, sq2 = sq.get_queue()

cbtn, cbtn1, cbtn2 = win.console_window(second_table, sts)
watcher = FolderWatcher(os.getcwd(), sync_func)

#viewport and initialization times
dpg.show_viewport()
elapsed = time.time()


#get the initial list of jobs
jobfiles = get_jobfiles()
update_local_table_values(second_table, jobfiles)

#main loop
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    list, list2 = downlink.fetch()
    if list is not None:
        update_job_values(main_table, list, list2)
        print("fetched")
    dpg.set_value(timer0,f"Last fetch : {int(elapsed- win.FETCH_TIME)}s ago" )
    elapsed = time.time()

#destroy context
dpg.destroy_context()





