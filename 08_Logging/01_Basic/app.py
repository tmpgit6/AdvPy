

import logging
import os 
from pathlib import Path
os.chdir(Path(__file__).parent)


logging.basicConfig(filename= "./app.log", level= logging.DEBUG,
                    format="%(name)s - %(levelname)s - %(filename)s - %(message)s")



def addieren(x, y):
    logging.debug(f"X:{x}, Y:{y}")

    result = x + y 

    return result 

logging.debug("Application3 is started")
print(addieren(7,8))



logging.debug("This is a DEBUG message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")




logging.debug("Application3 is finished")