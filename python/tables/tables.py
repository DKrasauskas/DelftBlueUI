import datetime
import subprocess

import dearpygui.dearpygui as dpg
from styles import *
import time
import squeue as sq
"""
Job Table (fetched from the remote device) :
"""
def cancel_handle(source, app_data, user_data):
    print(f"cancelling {user_data}")
    dpg.configure_item(source, label="TERMINATED")
    dpg.bind_item_theme(source, theme=red_button_theme)
    uplink = sq.AsyncQueue(func=None, args=("bash", "shell/cancel.sh", "terminate", user_data))
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

def update_job_values(main_table, list):
    print("fetched")
    dpg.delete_item(main_table, children_only=True)
    dpg.add_table_column(label="Status", init_width_or_weight=80, parent=main_table)
    dpg.add_table_column(label=list[0][0], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][1], init_width_or_weight=80, parent=main_table)
    dpg.add_table_column(label=list[0][2], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][3], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][4], init_width_or_weight=50, parent=main_table)
    dpg.add_table_column(label=list[0][5], init_width_or_weight=50, parent=main_table)
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
"""
Job Table (from local job files) :
"""
def create_local_table():
    height = 400
    with dpg.window(label="B", no_title_bar=True, no_resize=True, no_move=True,
                    no_scrollbar=True, width=800, height=height, pos=(500, 400)):
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

def update_local_table_values(second_table, list):
    dpg.delete_item(second_table, children_only=True)
    dpg.add_table_column(label="Job", init_width_or_weight=80, parent=second_table)
    dpg.add_table_column(label="Status", init_width_or_weight=80, parent=second_table)

    for i in range(0, len(list)):
        with dpg.table_row(parent=second_table):
            dpg.add_text(list[i])
            cbtn3 = dpg.add_button(
                label="status",
                width=80,
                height=30,
                callback=None,
            )