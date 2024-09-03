
import os 
import json
from pathlib import Path 
os.chdir(Path(__file__).parent)



# Load Config from JSON
with open("./config.json", mode = "r", encoding="UTF-8") as file:
    config = json.load(file)


# Load Cars from JSON
with open("./files/cars.json", mode = "r", encoding="UTF-8") as file:
    cars = json.load(file)

CORRECT_CASE = config["app"]["correct_case"]
PRINT_IN_TERMINAL = config["app"]["print_in_terminal"]
SAVE_IN_FILE = config["app"]["save_in_file"]
CARS_LIST = config["cars"]
EXPORT_FOLDER = config["app"]["export_dir"]