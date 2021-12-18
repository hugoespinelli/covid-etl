import argparse
import logging
import time

from watchdog.observers import Observer

from covid_etl.file_system_sync import FileSystemSync

logger = logging.getLogger()


def main(args) -> None:
    logger.info(args)
    event_hander = FileSystemSync(args.destination, args.listening)
    observer = Observer()
    observer.schedule(event_hander, args.listening, recursive=True)
    observer.start()

    logger.info("Starting watching proccess...")
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Programa sincronização de pastas utilizando ssh"
    )
    parser.add_argument(
        "-l",
        "--listening",
        type=str,
        required=True,
        help="O path de onde deseja escutar os " "eventos de criação dos arquivos",
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        default="",
        help="O path da onde deseja depositar os arquivos extraidos",
    )
    args = parser.parse_args()
    main(args)
