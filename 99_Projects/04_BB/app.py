import os 
from pathlib import Path 
from reservation import Reservation

os.chdir(Path(__file__).parent)


reservation1 = Reservation()
reservation1.start_reservation()
reservation1.export_receipt()

