import logging
from logging.config import fileConfig
import os
from algorithmen import Algorithmen 

from pathlib import Path
os.chdir(Path(__file__).parent)



fileConfig("./logging.conf", disable_existing_loggers=False)


logger = logging.getLogger()


logger.info("Application is started")

process1 = Algorithmen()
process1.encrypt_msg1()
process1.encrypt_msg2()


logger.info("Application is finished")