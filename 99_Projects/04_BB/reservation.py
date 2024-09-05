from customer import Customer 
from hotel import Hotel

class Reservation:

    def __init__(self) -> None:
        self.hotel = Hotel()
        self.customer = Customer() 
        self.wished_room = None
        self.period = 0

    def get_show_rooms(self):
         

        self.hotel.load_rooms_from_json() 
        self.hotel.show_rooms()

    def start_reservation(self):
        # Get and show rooms
        self.get_show_rooms()

        # Get Customer Information
        self.customer.get_customer_info()

        # Get the wished Room
        self.get_wished_room()

        # How Long ?
        self.get_period()


    def get_wished_room(self):
        self.wished_room_id = int(input("Which Room? ")) 
    
    def get_period(self):
        self.period = int(input("For how Long? ")) 
    
    def find_wished_room(self):
        for room in self.hotel.list_of_rooms:
            if room.roomid == self.wished_room_id:
                return room

    def export_receipt(self):
        room = self.find_wished_room()

        # Build receipt text
        receipt_text = f"Quittung für {self.customer.first_name} {self.customer.last_name}\n"
        receipt_text += "=" * 10 + "\n"
        receipt_text += f"{str(room)}\n"
        receipt_text += f"Summe: {room.price * self.period}€"


        print(receipt_text)



        