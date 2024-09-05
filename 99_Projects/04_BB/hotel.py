import json 
from room import Room

class Hotel:
    def __init__(self) -> None:
        self.list_of_rooms:list = [] 


    def load_rooms_from_json(self):
        
        # Load JSON
        with open("./rooms.json", mode = "r", encoding="UTF-8") as file:
            rooms:dict = json.load(file)
            rooms:list = rooms["rooms"]

        # Convert Dict to a List of Room()
        for room in rooms:
            self.list_of_rooms.append(Room(room["id"], room["roomtype"], room["price"]))
        
    def show_rooms(self):
        print("\nRooms")
        print("=" * 10)
        for room in self.list_of_rooms:
            print(room)


if __name__ == "__main__":

    import os 
    from pathlib import Path 
    os.chdir(Path(__file__).parent)


    hotel1 = Hotel()

    hotel1.load_rooms_from_json() 
    hotel1.show_rooms()




