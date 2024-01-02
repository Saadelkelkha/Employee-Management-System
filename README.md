# Employee-Management-System
This program employs object-oriented programming to create an Employee Management System. It features an abstract base class, Employee, encompassing shared attributes and salary calculation methods. Three derived classes (Manager, Salesperson, Cashier) cater to distinct employee types.

# More Details :
This program implements an Employee Management System using object-oriented programming in Python. It defines an abstract base class <b color ="red">Employee</b> with common  attributes such as name, number, marital status, address, base salary, supervisor, and methods for salary calculation. The program also includes three inherited classes: <b color ="red">Manager</b>, <b color ="red">Salesperson</b>, and <b color ="red">Cashier</b>, each representing a specific type of employee with additional attributes and salary calculation methods.

The system allows the creation of instances for different employee types, setting custom values when needed. It provides methods to display information about the created employees and calculate their salaries based on their specific roles. Additionally, the program includes a custom equality method for comparing instances based on their salary and employee ID.

In the main part of the program, instances of different employee types are created and their information is displayed. The salaries for each employee are calculated and printed. Finally, instances are compared for equality using the custom __eq__ method.
