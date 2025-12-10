import datetime
import os
import subprocess
import platform
from python.tables.jobConfigMenu import batchjob
from python.utils.styles import *
from python.utils import squeue as sq
from python.tables.JobCreator import *
from user import *

from zoneinfo import ZoneInfo
"""
Job Table (fetched from the remote device) :
"""
def cancel_handle(source, app_data, user_data):
    print(f"cancelling {user_data}")
    dpg.configure_item(source, label="TERMINATED")
    dpg.bind_item_theme(source, theme=red_button_theme)
    if platform.system() == "Windows":
        uplink = sq.AsyncQueue(func=None, args=( "powershell",
                "-ExecutionPolicy", "Bypass",
                "-File", "shell/windows/cancel.sh",
                "terminate",
                user_data,
                USER))
    else:
        uplink = sq.AsyncQueue(func=None, args=("bash", "shell/cancel.sh", "terminate", user_data, USER))
    uplink.start()


def create_job_table():
    height = 400
    with dpg.window(label="A", no_title_bar=True, no_resize=True, no_move=True,
                    no_scrollbar=True, width=800, height=height, pos=(500, 100)):
        main_table = dpg.add_table(
           tag="main_table", header_row=True,
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
           borders_outerH=True
        )
    return main_table

def update_job_values(main_table, list, list2):
    dpg.delete_item(main_table, children_only=True)
    dpg.add_table_column(label="Status", init_width_or_weight=80, parent=main_table)
    dpg.add_table_column(label=list[0][0], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][1], init_width_or_weight=80, parent=main_table)
    dpg.add_table_column(label=list[0][2], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][3], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][4], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][5], init_width_or_weight=225, parent=main_table)
    dpg.add_table_column(label=list[0][6], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][7], init_width_or_weight=160, parent=main_table)

    for i in range(1, len(list)):
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

                        datetime.datetime.strptime(exec_time, "%H:%M:%S")
                        theme = green_button_theme
                        status = "RUNNING"

                except ValueError:
                    status = "RUNNING"
                    theme = green_button_theme

                if j == 0:
                    cbtn = dpg.add_button(
                        label=status,
                        width=80,
                        height=30,
                        callback=cancel_handle,
                        user_data=f"{list[i][j]}",
                    )
                    dpg.bind_item_theme(cbtn, theme=theme)
                elif j == -1:
                    if status == "AWAIT":
                        now = datetime.datetime.now()
                        try:
                            time_start = datetime.datetime.fromisoformat(list2[i][j - 1])
                            waittime = time_start - now
                            dpg.add_text(f"Expected in {waittime.seconds}s ({int(waittime.seconds/ 60)} min)", tag=f"{j + i * len(list[i])}")
                        except ValueError:
                            dpg.add_text(f"Expected in N/A {len(list[i])} min)",
                                         tag=f"{j + i * len(list[i])}")
                    else:
                        dpg.add_text(f"{list[i][j - 1]}", tag=f"{j + i * len(list[i])}")
                else:
                    dpg.add_text(f"{list[i][j - 1]}", tag=f"{j + i * len(list[i])}")
"""
Job Table (from local job files) :
"""

def local_table_callback(source, appdata, user_data):
    path = user_data
    dpg.bind_item_theme(source, theme=downlink_theme)
    dpg.configure_item(source, label="SUBMITTED")
    if platform.system() == "Windows":
        subprocess.run(
            [
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-File", "shell/windows/run_job.sh",
            "run",
            f"remote/{user_data}",
            USER]
        )
    else:
        subprocess.run(
            ["bash", "shell/run_job.sh", "run", f"remote/{user_data}", USER]
        )

def job_editor_callback(source, appdata, user_data):
    path = user_data
    dpg.bind_item_theme(source, theme=downlink_theme)
    dpg.configure_item(source, label="ON")
    job = batchjob()

def create_local_table():
    height = 200
    with dpg.window(label="B", no_title_bar=True, no_resize=True, no_move=True,
                    no_scrollbar=True, width=800, height=height, pos=(500, 500)):
        second_table = dpg.add_table(
             tag="second_table", header_row=True,
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
             borders_outerH=True
        )
    return second_table

def request_modified_callback(source, appdata, user_data):
    print(user_data)
    job = JobCreator(user_data)
    job.dropdown_callback("CPU", "CPU")

def update_local_table_values(second_table, list):
    dpg.delete_item(second_table, children_only=True)
    dpg.add_table_column(label="Job", init_width_or_weight=80, parent=second_table)
    dpg.add_table_column(label="Status", init_width_or_weight=80, parent=second_table)
    dpg.add_table_column(label="Edit", init_width_or_weight=80, parent=second_table)

    for i in range(0, len(list)):
        with dpg.table_row(parent=second_table):
            dpg.add_text(list[i])
            if os.path.isfile(f"remote/{list[i]}/request.sh"):
                cbtn3 = dpg.add_button(
                    label="READY",
                    width=80,
                    height=30,
                    callback=local_table_callback,
                    user_data=f"{list[i]}"
                )
                dpg.bind_item_theme(cbtn3, theme=uplink_theme)
            else:
                cbtn3 = dpg.add_button(
                    label="NO CNF",
                    width=80,
                    height=30,
                    callback=local_table_callback,
                    user_data=f"{list[i]}"
                )
                dpg.bind_item_theme(cbtn3, theme=downlink_theme)
            cbtn4 = dpg.add_button(
                label="Configure",
                width=80,
                height=30,
                callback=request_modified_callback,
                user_data=f"{list[i]}"
            )
