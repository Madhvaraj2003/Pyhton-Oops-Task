class Employee:      # Created a Base class called Employee.
    def __init__(self, name, salary):      # Created a function with attributes name, salary.
        self.name = name
        self.salary = salary
    def calculate_salary(self):  # Calculating salary using function.
        return f"{self.name} earns {self.salary}"  # Return's salary.

class Contract_Employee(Employee):   # Created a child class using Base class Employee.
    def __init__(self, name, salary):
        super().__init__(name, salary)  # super init() used refer to its parent class Employee.
    def calculate_salary(self):
            return f"{self.name} Is a Contracted Employee He Earns {self.salary}"

class Regular_Employee(Employee):    # Created a child class using Base class Employee.
    def __init__(self, name, salary):
        super().__init__(name, salary)  # This is a method used refer to its parent class attributes.
    def calculate_salary(self):
            return f"{self.name} Is a Regular Employee and He Earns {self.salary * 2}"

class Manager(Employee):        # Created a child class Manager which inherited from base class employee.
    def __init__(self, name, salary):
        super().__init__(name, salary)    # Used to access the parent class attributes.
    def calculate_salary(self):
            return f"{self.name}  Is a Manager and He Earns {self.salary * 5}"

Regular_employee = Regular_Employee("Raj", 10000)           # Assigning values to return the expected outcomes.
Contract_employee = Contract_Employee("Ganesh", 5000)
Manager = Manager("Swami rao", 100000)
print(Regular_employee.calculate_salary())
print(Contract_employee.calculate_salary())
print(Manager.calculate_salary())