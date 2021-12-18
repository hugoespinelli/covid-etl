import logging
import subprocess

from watchdog.events import FileSystemEventHandler

from covid_etl.ssh_connect import put

logger = logging.getLogger()


class FileSystemSync(FileSystemEventHandler):
    def __init__(self, destination, listen) -> None:
        super().__init__()
        self._destination = destination
        self._listen_folder = listen

    def on_any_event(self, event):
        logger.info(f"Event detected {event.event_type }. Starting transfer process...")
        # put(event.src_path, self._destination)
        output = subprocess.run(
            f"rsync -avz --rsh='ssh -p799' {self._listen_folder} alunos_uerj@157.86.153.23:{self._destination}",
            shell=True,
            capture_output=True    
        )
        logger.info(output)
        
