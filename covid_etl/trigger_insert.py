import argparse
import logging
import time

from watchdog.observers import Observer

from covid_etl.insert_files_database import FileSystemInsert

logger = logging.getLogger()


def main(args) -> None:
    logger.info(args)
    event_hander = FileSystemInsert()
    observer = Observer()
    observer.schedule(event_hander, args.listening, recursive=True)
    observer.start()

    logger.info(f"Listening created events on {args.listening}...")
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Programa que escuta diretorio e insere arquivos no banco"
    )
    parser.add_argument(
        "-l",
        "--listening",
        type=str,
        required=True,
        help="O path de onde deseja escutar os eventos de criação dos arquivos",
    )
    args = parser.parse_args()
    main(args)
