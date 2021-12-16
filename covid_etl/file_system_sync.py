import logging

from watchdog.events import FileSystemEventHandler

from covid_etl.ssh_connect import put

logger = logging.getLogger()


class FileSystemSync(FileSystemEventHandler):
    def __init__(self, destination) -> None:
        super().__init__()
        self._destination = destination

    def on_any_event(self, event):
        logger.info(f"Event detected {event.event_type }. Starting transfer process...")
        put(event.src_path, self._destination)
