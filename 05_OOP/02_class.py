class Employee:
    bonus = 500 # class based attribute

    def __init__(self, first_name) -> None:
        self.first_name = first_name # Instance based attribute
        
    
    def get_emp_info(self):
        print(f"FN:{self.first_name}" )


# Create Instances
thomas = Employee("Thomas")
frank = Employee("Frank")


print(thomas.bonus)
print(frank.bonus)


print(thomas.__dict__)
print(frank.__dict__)

##################################
thomas.bonus = 700

print(thomas.bonus)
print(frank.bonus)

print(thomas.__dict__)
print(frank.__dict__)

###############################
Employee.bonus = 1200 

print(thomas.bonus)
print(frank.bonus)


print(thomas.__dict__)
print(frank.__dict__)
