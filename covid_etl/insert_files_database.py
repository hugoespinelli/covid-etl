import logging
from pathlib import Path
from typing import Any

from mysql.connector import connect, Error
from watchdog.events import FileSystemEventHandler


from covid_etl.consts import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
)

logger = logging.getLogger()


def get_connection():
    try:
        connection = connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
        )
        logger.info(f"Connected on {DB_HOST}...")
        return connection
    except Error as e:
        logger.info(e)


def insert_file(filepath: str, nome: str):
    with get_connection() as connection:
        insert_query = """
        INSERT INTO covid.arquivo
        (caminho_salvo_servidor, nome)
        VALUES(%s, %s);
        """
        cursor = connection.cursor()
        cursor.execute(insert_query, (filepath, nome))
        connection.commit()
        logger.info(f"Rows inserted: {cursor.rowcount}")


class FileSystemInsert(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()

    def on_created(self, event):
        if event.is_directory:
            logger.info("Directory was created. Starting inserting process...")
            src_path = event.src_path
            filename = Path(src_path).name
            insert_file(src_path, filename)
