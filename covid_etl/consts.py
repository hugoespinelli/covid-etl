from os import getenv
from dotenv import load_dotenv

load_dotenv()

SERVER_MACHINE_IP = getenv("SERVER_MACHINE_IP")
SSH_USERNAME = getenv("SSH_USERNAME")
SSH_PASSWORD = getenv("SSH_PASSWORD")
SSH_PORT = getenv("SSH_PORT")
SAMPLES_COVID_FOLDER_PATH = getenv("SAMPLES_COVID_FOLDER_PATH")
