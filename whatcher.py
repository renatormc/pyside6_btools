from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class EventHandler(FileSystemEventHandler):
    def catch_all_handler(self, event):
        print(event)
 
    def on_moved(self, event):
        self.catch_all_handler(event)
 
    def on_created(self, event):
        self.catch_all_handler(event)
 
    def on_deleted(self, event):
        self.catch_all_handler(event)
 
    def on_modified(self, event):
        self.catch_all_handler(event)


def start_watching(folder, recursive: bool):
    events = EventHandler()
    observer = Observer()
    observer.schedule(events, folder, recursive=recursive)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.unschedule(events)
        observer.stop()
    observer.join()