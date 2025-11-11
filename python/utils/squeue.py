import subprocess
import asyncio
import threading
import dearpygui as dpg
import time
import queue
from user import *

def get_queue():

        result = subprocess.run(
            ["bash", "shell/check_job_status.sh", "check", USER],
            capture_output=True,
            text=True,
            check=True
        )
        return 1, [x.split() for x in result.stdout.split("\n") if len(x) != 0]


class AsyncQueue:

    def __init__(self, func, args, interval=60):
        self.interval = interval
        self._stop_event = threading.Event()
        self._data_lock = threading.Lock()
        self.data_queue = queue.Queue()  # Thread-safe queue for passing data
        self.fetch_rule = func
        self.args = args
        self._data = None
        self.flag = 0

    def start(self):
        """Start the background thread to fetch SSH data."""
        threading.Thread(target=self._worker, daemon=True).start()

    def stop(self):
        """Stop the background thread."""
        self._stop_event.set()

    def _worker(self):
        while not self._stop_event.is_set():
            try:
                result = subprocess.run(
                    [*self.args],
                    capture_output=True,
                    text=True,
                    check=True
                )
                parsed_result =  [x.split() for x in result.stdout.split("\n") if len(x) != 0]
                with self._data_lock:
                    self._data = parsed_result
                    self.flag = True

            except subprocess.CalledProcessError as e:
                print("SSH job check failed:", e)
                with self._data_lock:
                    self._data = None
                    self.flag = True
            time.sleep(1)

    def fetch(self):
        with self._data_lock:
            if self.flag:
                self.flag = False
                return self._data
        return None


