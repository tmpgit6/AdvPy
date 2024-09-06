import os 
from pathlib import Path
import pandas as pd
os.chdir(Path(__file__).parent)

from processor import Processor


def main():
    INPUT_FILE = "./my_data.csv"
    OUTPUT_FILE = "./my_data_processed.csv"

    COL_DEL = ["Purchase Address", "Order Date"]
    NUM_COL = ["Order ID","Quantity Ordered", "Quantity Ordered"]
    
    myfile = Processor(INPUT_FILE,OUTPUT_FILE, COL_DEL, NUM_COL)
    myfile.clean()


    myfiles = ["file1.csv","file2.csv", "file3.csv"]

    for file in myfiles:
        cleaner = Processor(file)
        cleaner.clean()




if __name__ == "__main__":
    main()