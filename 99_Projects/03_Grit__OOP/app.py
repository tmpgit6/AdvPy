class Employee:

    counter = 0

    def __init__(self, first_name, last_name, salary =0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary 
        self.project_list = []
        Employee.counter += 1

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def create_emp_from_string(cls,name):
        first_name, last_name = name.strip().split()
        return cls(first_name, last_name)
    
    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

    def assign_project(self, project_title):
        self.project_list.append(project_title)
    
    def revoke_project(self, project_title):
        if project_title in self.project_list:
            self.project_list.remove(project_title)

    def show_emp_card(self):
        message = f"Emp: {self.first_name} {self.last_name.upper()}\n"
        message += "=" * 20 + "\n"
        message += "Project List:\n"

        for project in self.project_list:
            message += f"- {project}\n"

        print(message)

thomas = Employee("Thomas", "Meier")
sven = Employee.create_emp_from_string("Sven Meier")
print(thomas)
print(sven)


thomas.assign_project("Project A")
thomas.assign_project("Project B")
sven.assign_project("Project B")

# thomas.revoke_project("Project B")

thomas.show_emp_card()

print(Employee.counter)
del thomas
print(Employee.counter)