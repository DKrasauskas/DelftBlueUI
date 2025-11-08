from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
        # You can call any function here
        my_function(event.src_path)

    def on_created(self, event):
        print(f"Created: {event.src_path}")
        my_function(event.src_path)

def my_function(path):
    print(f"Folder changed: {path}")


current_folder = os.getcwd()
event_handler = ChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=current_folder, recursive=True)  # recursive=True watches subfolders
observer.start()

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()