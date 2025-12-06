from dearpygui.dearpygui import *
import os
import shutil



create_context()

class batchjob:
    def __init__(self, job):
        self.job = job

    def generate_jobfile(self):
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        mode = 0o644
        os.mkdir(f"remote/{self.NAME}")
        file = os.open(f"remote/{self.NAME}/request.sh", flags, mode)
        buffer = (
          f"#!/bin/bash\n"
          f"#SBATCH --job-name=\"{self.NAME}\" \n"
          f"#SBATCH --partition=gpu\n"
          f"#SBATCH --cpus-per-task={self.NUM_OF_CPUS} \n"
          f"#SBATCH --gpus-per-task={self.NUM_OF_GPUS}\n"
          f"#SBATCH --time=00:{1}:00\n"
          f"#SBATCH --ntasks=1\n"
          f"#SBATCH --mem-per-cpu=1G\n\n"
          f"srun job.sh"
        )
        os.write(file, buffer.encode('utf8'))
        os.close(file)
        shutil.copy2("../../templates/generic_job/job.sh", f"remote/{self.NAME}")



def _handle_job_creation(source, app_data, user_data):
    job = batchjob(source)
    job.NUM_OF_CPUS = get_value(f"{user_data}_NUM_OF_CPUS")
    job.NUM_OF_GPUS = get_value(f"{user_data}_NUM_OF_GPUS")
    job.NAME = get_value(f"{user_data}_job_name")
    print(job.NAME)
    job.TYPE = f"{user_data}"
    job.generate_jobfile()
    hide_item(user_data)

def slider_callback(sender, app_data):
    set_value("message", f"Slider value: {app_data:.2f}")


def knob_callback(sender, app_data):
    set_value("message", f"{sender} set to {app_data:.2f}")

# def get_jobfiles():
#     subfolder_path = "remote"
#     return os.listdir(subfolder_path)

def dropdown_callback(sender, app_data):
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
        with window(label="CPU Configuration", tag=f"{window_tag}", width=300, height=200, pos=(400, 400)):
            add_input_text(label="Job Name", tag=f"{window_tag}_job_name", default_value="MyJob.sh", width=200)
            add_input_int(label="CPUs", tag=f"{window_tag}_NUM_OF_CPUS", width=100)
            add_input_int(label="GPUs", tag=f"{window_tag}_NUM_OF_GPUS", width=100)
            add_input_float(label="Max Runtime (mins)", source=f"{window_tag}_float", width=100)
            add_button(label="Create", callback=_handle_job_creation, user_data=f"{window_tag}")

def create_window():
    dropdown_callback("CPU", "CPU")


# create_viewport(title="Dropdown New Window Example", width=400, height=200)
# setup_dearpygui()
# show_viewport()
# start_dearpygui()
# destroy_context()