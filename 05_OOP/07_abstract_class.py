from abc import ABC, abstractmethod

class Car(ABC):    
    def __init__(self, model, kz) -> None:
        self.model = model 
        self.kz = kz 

    @abstractmethod
    def engine_start(self):
        raise NotImplementedError

    def drive(self):
        print("I am driving" , self.kz)
    

    def park(self):
        print("I am Parking")

   
class VW(Car):
    def __init__(self, model, kz, ble) -> None:
        super().__init__(model, kz)
        self.ble = ble


    def ble_pair(self):
        print("Pairing")

    def engine_start(self):
        print("Öl warming")

class Audi(Car):
    def __init__(self, model, kz, gps) -> None:
        super().__init__(model, kz)
        self.gps = gps
  
    def gps_pair(self):
        print("GPS positioning")

    def engine_start(self):
        print("Benzin warming")

class Tesla(Car):
    def __init__(self, model, kz, radio) -> None:
        super().__init__(model, kz)
        self.radio = radio 

  
    def search_channel(self):
        print("Searching Channel")

    def engine_start(self):
        print("E warming")

class Mercedes(Car):
    def __init__(self, model, kz) -> None:
        super().__init__(model, kz)

    def engine_start(self):
        return super().engine_start()


# car1 = Car("Spagetti", "Nudeln")
vw1 = VW("Passat", "AA12345", True)
audi1 = Audi("Q3", "BB12354", False)
tesla1 = Tesla("T3", "CC12345", False)

mer1 = Mercedes("Mer", "DD1234")

for car in [vw1, audi1, tesla1]:
    car.drive()
    car.engine_start()

vw1.ble_pair()

# car1.drive()