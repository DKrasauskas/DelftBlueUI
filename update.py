import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import threading

SYNC_INTERVAL = 6  # seconds

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, folder_to_watch, sync_function):
        super().__init__()
        self.folder = folder_to_watch
        self.sync_function = sync_function
        self.sync_timer = None
        self.lock = threading.Lock()
        self.sync_start_time = 0

    def schedule_sync(self):
        with self.lock:
            if self.sync_timer is not None:
                self.sync_timer.cancel()
            self.sync_timer = threading.Timer(SYNC_INTERVAL, self.sync)
            self.sync_timer.start()
            self.sync_start_time = time.time()
        return self.sync_start_time

    def sync(self):
        print("Running sync in a separate thread")
        self.sync_start_time = time.time()
        self.sync_function(self, self.folder)
        self.schedule_sync()

    def on_modified(self, event):
        self.schedule_sync()

    def on_created(self, event):
        self.schedule_sync()

class FolderWatcher:
    def __init__(self, folder, sync_function):
        self.update_time = time.time()
        self.folder = folder
        self.sync_function = sync_function
        self.event_handler = ChangeHandler(folder, sync_function, )
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=folder, recursive=True)
        self.start_time = 0

    def _log_sync(self, sync_start):
        self.start_time = sync_start
    def start(self):
        """Start watching asynchronously."""
        self.observer.start()
        self.start_time = self.event_handler.schedule_sync()

    def stop(self):
        """Stop watching and syncing."""
        self.observer.stop()
        self.observer.join()

# Example usage in another script
def my_sync(path):
    print(f"Syncing folder: {path}")
    # Your syncing logic here

if __name__ == "__main__":
    folder = os.getcwd()
    watcher = FolderWatcher(folder, my_sync)
    watcher.start()
    print("Watcher started. Main thread can continue doing other work.")
