from dearpygui.dearpygui import *
import os
class batchjob:
    def __init__(self, job):
        self.job = job

    def _generate_jobfile(self):
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        mode = mode = 0o644
        if self.TYPE == "gpu":
            file = os.open(f"job_data/{self.NAME}", flags, mode)
            buffer = (
              f"#SBATCH --job-name=\"{self.NAME}\" \n"
              f"#SBATCH --partition={self.TYPE}\n"
              f"#SBATCH --cpus-per-task={self.NUM_OF_CPUS} \n"
              f"#SBATCH --gpus-per-task={self.NUM_OF_GPUS}\n"
              f"#SBATCH --ntasks=1\n"
              f"#SBATCH --mem=100G\n"
            )
            os.write(file, buffer.encode('utf8'))
            os.close(file)



def _handle_job_creation(source, app_data, user_data):
    job = batchjob(source)
    job.NUM_OF_CPUS = get_value(f"{user_data}_NUM_OF_CPUS")
    job.NUM_OF_GPUS = get_value(f"{user_data}_NUM_OF_GPUS")
    job.NAME = get_value(f"{user_data}_job_name")
    job.TYPE = f"{user_data}"
    job._generate_jobfile()
    hide_item(user_data)

def slider_callback(sender, app_data):
    set_value("message", f"Slider value: {app_data:.2f}")


def knob_callback(sender, app_data):
    set_value("message", f"{sender} set to {app_data:.2f}")


create_context()
def dropdown_callback(sender, app_data):
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
        with window(label="CPU Configuration", tag=f"{window_tag}", width=300, height=200):
            add_input_text(label="Job Name", tag=f"{window_tag}_job_name", default_value="MyJob", width=200)
            add_input_int(label="CPUs", tag=f"{window_tag}_NUM_OF_CPUS", width=100)
            add_input_int(label="GPUs", tag=f"{window_tag}_NUM_OF_GPUS", width=100)
            add_input_float(label="Max Runtime (mins)", source=f"{window_tag}_float", width=100)
            add_button(label="Create", callback=_handle_job_creation, user_data=f"{window_tag}")

with window(label="Main Window", width=400, height=200):
    add_text("Select an option to open a new window:")
    add_combo(["GPU", "CPU"], label="Choose", callback=dropdown_callback)

create_viewport(title="Dropdown New Window Example", width=400, height=200)
setup_dearpygui()
show_viewport()
start_dearpygui()
destroy_context()