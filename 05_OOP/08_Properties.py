class Employee:    

    def __init__(self, first_name, last_name, salary =0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary 
              
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} "
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            raise ValueError("Salary should be more than zero €")


    
# Consumer
thomas = Employee("Thomas", "Meier")


print(thomas.salary )
thomas.salary = 6000

print(thomas.salary )

thomas.salary = -4000
# print(thomas._Employee__salary)



