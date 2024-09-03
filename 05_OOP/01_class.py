class Employee:
    def __init__(self, first_name,car = "") -> None:
        self.first_name = first_name # Instance based attribute
        self.car = car
    
    def get_emp_info(self):
        print(f"FN:{self.first_name} - Car:{self.car}")


# Create Instances
thomas = Employee("Thomas")
frank = Employee("Frank")


employee_list = [thomas, frank]


for emp in employee_list:
    emp.get_emp_info()