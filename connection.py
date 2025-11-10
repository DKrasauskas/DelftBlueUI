import subprocess
import threading
import time
import dearpygui.dearpygui as dpg


dpg.create_context()
WIDTH = 1200
HEIGHT = 800
dpg.create_viewport(title="SSH Progress Bar", width=WIDTH, height=HEIGHT)
progress = 0
uplink_status = False

def ssh_connect_task():
    global uplink_status
    print("start")
    subprocess.run(
        ["bash", "shell/connect.sh", "A"],
        capture_output=True,
        text=True,
        check=True,
        timeout=10
    )
    print("done")
    uplink_status = True


def start_ssh_callback(sender, app_data):
    global progress, uplink_status
    progress = 0.0
    uplink_status = False
    threading.Thread(target=ssh_connect_task, daemon=True).start()


def  update_progress(pbar):
    global progress
    if uplink_status:
        progress = 1.0
    else:
        progress = min(progress + 0.01, 0.99)
    dpg.set_value(pbar, progress)
    dpg.configure_item(pbar, overlay=f"{progress}")
    dpg.set_frame_callback(dpg.get_frame_count() + 3, callback=lambda: update_progress(pbar))

width, height, channels, data = dpg.load_image("backends/img.png")
with dpg.texture_registry():
    texture_id = dpg.add_static_texture(width, height, data)


with dpg.font_registry():
    title_font = dpg.add_font("backends/Freedom-10eM.ttf", 34)


with dpg.window(label="", no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, width=width, height=height, pos=(WIDTH / 2 - width/2, HEIGHT/ 3 - height/2)):
    dpg.add_image(texture_id, pos=(-1, -1))
    #dpg.bind_font(title_font)

with dpg.window(label="SSH Checker", no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, no_background=True, pos=(WIDTH / 3 - width/2, HEIGHT/ 3 + height )):
    pbar = dpg.add_progress_bar(label="progress_bar", default_value=0.0, overlay="0%",width=WIDTH / 2, height=20)
    update_progress(pbar)
    start_ssh_callback(None, None)

with dpg.window(label="T", no_title_bar=True, no_resize=True, no_move=True,
            no_scrollbar=True, width=width, height=100, pos=(WIDTH / 2 - width/2, HEIGHT/ 3 + height / 2), no_background=True):
    title = dpg.add_text("Delft Blue", tag="custom_text")
    dpg.bind_item_font(title, title_font)

#subprocess.Popen(["konsole", "-e", "/home/dominykas/PycharmProjects/PythonProject/DBinterface/shell/connect.sh", "A"])
#print(result)
dpg.set_frame_callback(1, callback=lambda: update_progress(pbar))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
