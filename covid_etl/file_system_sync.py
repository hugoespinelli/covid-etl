import logging

from watchdog.events import FileSystemEventHandler

from covid_etl.ssh_connect import put

logger = logging.getLogger()


class FileSystemSync(FileSystemEventHandler):
    def __init__(self, destination) -> None:
        super().__init__()
        self._destionation = destination

    def on_created(self, event):
        if event.is_directory:
            logger.info("Directory was created. Starting transfer process...")
            put(event.src_path, self._destination)
