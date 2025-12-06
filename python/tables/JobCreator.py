import re
from dearpygui.dearpygui import *
import os

partitions = {
    "CPU 1" : "cpu-p1",
    "CPU 2" : "cpu-p2",
    "CPU_HIGH_MEM" : "memory",
    "GPU_SMALL" : "gpu-a100-small",
    "GPU A100" : "gpu-a100",
    "GPU V100S" : "gpu"
}
create_context()
class JobCreator:
    def __init__(self, source):
        self.source = "remote/" + source + "/request.sh"
        with open(self.source, "a+") as f:
            f.seek(0)
            file = f.read()
        self.name = re.search(r"--job-name=([^\n]*)", file)
        self.name = self.name.group(1) if self.name is not None else "Default"

        self.partition = re.search(r"--partition=([^\n]*)", file)
        self.partition = self.partition.group(1) if self.partition is not None else "Default"

        self.gpus = re.search(r"--gpus-per-task=([^\n]*)", file)
        self.gpus = self.gpus.group(1) if self.gpus is not None else "Default"

        self.cpus = re.search(r"--cpus-per-task=([^\n]*)", file)
        self.cpus = self.cpus.group(1) if self.cpus is not None else "Default"

        self.time = re.search(r"--time=([^\n]*)", file)
        self.time = self.time.group(1) if self.time is not None else "Default"

        self.ntasks = re.search(r"--ntasks=([^\n]*)", file)
        self.ntasks = self.ntasks.group(1) if self.ntasks is not None else "Default"

        self.cpu_mem = re.search(r"--mem-per-cpu=([^\n]*)", file)
        self.cpu_mem = self.cpu_mem.group(1) if self.cpu_mem is not None else "Default"

        if self.time != "Default":
            self.h, self.min, self.s = self.time.split(":")[0],  self.time.split(":")[1],  self.time.split(":")[2]
        else:
            self.h, self.min, self.s = "00", "00", "00"

    def callback_name(self, sender, app_data):
        self.name = app_data

    def callback_nodetype(self, sender, app_data):
        self.partition = partitions[app_data]

    def callback_nodes(self, sender, app_data):
        self.ntasks = app_data

    def callback_cpus(self, sender, app_data):
        self.cpus = app_data
    def callback_mem(self, sender, app_data):
        self.cpu_mem = app_data

    def callback_gpus(self, sender, app_data):
        self.gpus = app_data

    def callback_h(self, sender, app_data):
        self.h = app_data

    def callback_min(self, sender, app_data):
        self.min = app_data

    def callback_s(self, sender, app_data):
        self.s = app_data

    def save(self):
        file = open(self.source, "wb")
        job_properties = (
            f"#!/bin/bash\n"
            f"#SBATCH --job-name={self.name}\n"
            f"#SBATCH --partition={self.partition}\n"
            f"#SBATCH --ntasks={self.ntasks}\n"
            f"#SBATCH --gpus-per-task={self.cpus}\n"
            f"#SBATCH --cpus-per-task={self.gpus}\n"
            f"#SBATCH --mem-per-cpu={self.cpu_mem}G\n"
            f"#SBATCH --time={self.h}:{self.min}:{self.s}\n"
            f"chmod +x job.sh\n"
            f"srun job.sh\n"
        )
        file.write(
            job_properties.encode("utf-8")
        )
        return


    def dropdown_callback(self, sender, app_data):
        #jobfiles = get_jobfiles()
        #update_local_table_values(user_data, jobfiles)
        """Open a new window based on dropdown selection"""
        if app_data == "CPU":
            window_tag = "cpu"
            title = "Window 1"
        elif app_data == "GPU":
            window_tag = "gpu"
            title = "Window 2"
        else:
            return

        if does_item_exist(window_tag):
            show_item(window_tag)
        else:
            with window(label="Job", tag=f"{window_tag}", width=800, height=400, pos=(0, 0), on_close=self.save):
                add_input_text(label="Job Name", tag=f"job_name", default_value="template job", callback=self.callback_name)
                add_text("CPUs", pos=(0, 50))
                add_text("CPU MEM GB", pos=(120, 50))
                add_text("GPUs", pos=(240, 50))
                add_text("Nodes", pos=(360, 50))
                add_text("Node Type", pos=(480, 50))
                add_input_int(
                    label="",
                    tag=f"{window_tag}CPU",
                    default_value=0,
                    width=100,
                    pos=(0, 70),
                    callback = self.callback_nodes
                )
                add_input_int(
                    label="",
                    tag=f"{window_tag}GPU",
                    default_value=0,
                    width=100,
                    pos=(120, 70),
                    callback = self.callback_cpus
                )
                add_input_int(
                    label="",
                    tag=f"{window_tag}MEM",
                    default_value=0,
                    width=100,
                    pos=(240, 70),
                    callback=self.callback_mem
                )
                add_input_int(
                    label="",
                    tag=f"{window_tag}NODES",
                    default_value=0,
                    width=100,
                    pos=(360, 70),
                    callback=self.callback_gpus
                )
                add_combo(
                    items=["CPU 1", "CPU 2", "CPU_HIGH_MEM", "GPU_SMALL", "GPU A100", "GPU V100S"],
                    default_value="N/A",
                    width=150,
                    pos = (480, 70),
                    callback=self.callback_nodetype
                )
                add_text("Runtime", pos=(0, 90))
                add_text("h", pos=(0, 120))
                add_text("min", pos=(120, 120))
                add_text("s", pos=(240, 120))
                add_input_int(label="", source=f"{window_tag}_float", width=100, pos=(0, 150), callback=self.callback_h)
                add_input_int(label="", source=f"{window_tag}_float", width=100, pos=(120, 150), callback=self.callback_min)
                add_input_int(label="", source=f"{window_tag}_float", width=100, pos=(240, 150), callback=self.callback_s)


    def create_window(self):
        self.dropdown_callback("CPU", "CPU")

