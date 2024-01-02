from abc import ABCMeta, abstractmethod

# Define an abstract base class (ABC) named Employee with an abstract method Salary
class Employee(metaclass=ABCMeta):
    _count = 0

    def __init__(self, name='Saad', number=0, marital_status='single', address='ISGI', base_salary=0, supervisor="Saad"):
        # Constructor method to initialize attributes
        self._name = name
        self._number = number
        self._marital_status = marital_status
        self._address = address
        self._base_salary = base_salary
        Employee._count += 1
        self._employee_id = Employee._count
        self._supervisor = supervisor

    # Property getters for various attributes
    @property
    def get_name(self):
        return self._name

    @property
    def get_number(self):
        return self._number

    @property
    def get_marital_status(self):
        return self._marital_status

    @property
    def get_address(self):
        return self._address

    @classmethod
    def get_count(cls):
        return Employee._count

    @property
    def get_employee_id(self):
        return self._employee_id

    @property
    def get_supervisor(self):
        return self._supervisor

    @property
    def get_base_salary(self):
        return self._base_salary

    # Setter methods for various attributes
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number

    def set_marital_status(self, status):
        self._marital_status = status

    def set_address(self, address):
        self._address = address

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_base_salary(self, base_salary):
        self._base_salary = base_salary

    def set_supervisor(self, supervisor):
        self._supervisor = supervisor

    # Abstract method representing the salary calculation
    @abstractmethod
    def salary(self, sales=0):
        pass

    # Custom equality method for comparing instances
    def __eq__(self, other, sales=0):
        if type(self) == type(other):
            return (self.salary(sales) == other.salary(sales)) and (self.get_employee_id == other.get_employee_id)
        else:
            return "Not the same type"

    # Custom string representation method
    def __str__(self):
        return f'Name: {self.get_name}, Number: {self.get_number}, Marital Status: {self.get_marital_status}, Address: {self.get_address}, Employee ID: {self.get_employee_id}, Base Salary: {self.get_base_salary}'


# Inherited class Manager from Employee
class Manager(Employee):
    def __init__(self, name='Saad', number=0, marital_status='single', address='ISGI', base_salary=0, supervisor="Saad", bonus=0):
        # Constructor method for Manager, calling the constructor of the base class (Employee)
        super().__init__(name, number, marital_status, address, base_salary, supervisor)
        self._bonus = bonus

    # Getter method for bonus attribute
    @property
    def get_bonus(self):
        return self._bonus

    # Setter method for bonus attribute
    def set_bonus(self, bonus):
        self._bonus = bonus

    # Implementation of abstract method Salary for Manager
    def salary(self, sales=0):
        return self.get_base_salary + self.get_bonus


# Inherited class Salesperson from Employee
class Salesperson(Employee):
    def __init__(self, name='Saad', number=0, marital_status='single', address='ISGI', base_salary=0, supervisor="Saad", commission=15):
        # Constructor method for Salesperson, calling the constructor of the base class (Employee)
        super().__init__(name, number, marital_status, address, base_salary, supervisor)
        self._commission = commission

    # Getter method for commission attribute
    @property
    def get_commission(self):
        return self._commission

    # Setter method for commission attribute
    def set_commission(self, commission):
        self._commission = commission

    # Implementation of abstract method Salary for Salesperson
    def salary(self, sales):
        return self.get_base_salary + (self.get_commission * sales)


# Inherited class Cashier from Employee
class Cashier(Employee):
    def __init__(self, name='Saad', number=0, marital_status='single', address='ISGI', base_salary=0, supervisor="Saad"):
        # Constructor method for Cashier, calling the constructor of the base class (Employee)
        super().__init__(name, number, marital_status, address, base_salary, supervisor)

    # Implementation of abstract method Salary for Cashier
    def salary(self, sales=0):
        return self.get_base_salary
