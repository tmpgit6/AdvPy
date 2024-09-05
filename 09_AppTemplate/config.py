import os 
from pathlib import Path
import logging
import json 
from logging.config import fileConfig


os.chdir(Path(__file__).parent) 

# Load Logger
fileConfig("./logging.conf", disable_existing_loggers=False)
logger = logging.getLogger()



# Load Config


# Load Config from JSON
with open("./config.json", mode = "r", encoding="UTF-8") as file:
    config = json.load(file)

#