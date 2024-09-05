

import logging
import os 
from pathlib import Path
os.chdir(Path(__file__).parent)


# Create a Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(name)s - %(levelname)s - %(filename)s- %(asctime)s - %(message)s")


# File Handler
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)


# Stream Handler (Im Terminal)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


x = 10 
y = 20

logger.debug("Application is started")
logger.info(f"X:{x} - Y:{y}")

logger.debug("Application is finished")