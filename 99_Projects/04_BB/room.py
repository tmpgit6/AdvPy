class Room:
    def __init__(self, roomid, roomtype,price) -> None:
        self.roomid = roomid
        self.roomtype = roomtype        
        self.price = price
        

    def __repr__(self) -> str:
        return f"{self.roomid}. {self.roomtype} - {self.price}€"

if __name__ == "__main__":
    room1 = Room(1, "Single Room", 30)
    print(room1)