class Employee:
    bonus = 500 # class based attribute

    def __init__(self, first_name, salary, weight) -> None:
        self.first_name = first_name # Instance based attribute
        self.salary = salary
        self.weight = weight
    
    def get_emp_info(self):
        print(f"FN:{self.first_name}" )

    def __repr__(self):
        return f"{self.first_name} - {self.salary}"
    
    def __add__(self, other):
        return self.salary + other.salary
    
    def __gt__(self, other):
        return self.salary > other.salary
    
    def __len__(self):
        return len(self.first_name)
    


    


# Create Instances
thomas = Employee("Thomas", 5000, 1.8)
frank = Employee("Frank", 3000 , 1.9)

x = 10 
y = 20 


print(thomas)
print(thomas + frank)
print(thomas > frank)

print(len(thomas))



