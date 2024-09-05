class Customer:
    def __init__(self, first_name="", last_name="") -> None:
        self.first_name = first_name
        self.last_name = last_name        
        

    def __repr__(self) -> str:
        return f"{self.first_name}. {self.last_name}"

    def get_customer_info(self):
        self.first_name,self.last_name = input("Wie heißen Sie?").strip().split()
        
        
        
if __name__ == "__main__":
    customer1 = Customer("Thomas", "Meier")


    print(customer1)