import logging
from datetime import datetime

logging = logging.basicConfig(
    filename=f"application_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

__version__ = "0.1.0"
