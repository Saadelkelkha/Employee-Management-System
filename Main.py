# Import classes from the 'classes' module
from classes import Employee, Manager, Salesperson, Cashier

# Create instances of different employee types
p1 = Manager()  # Default values will be used
p2 = Manager("Zouhir", 345, 'single', "socoma", 20000, 'Saad', 2000)  # Custom values provided
v1 = Salesperson()  # Default values will be used
v2 = Salesperson("Ahmed", 345, 'single', "socoma", 10000, 'Saad', 15)  # Custom values provided
c1 = Cashier()  # Default values will be used
c2 = Cashier("Brahim", 345, 'single', "socoma", 5000, 'Saad')  # Custom values provided

# Display information about the created instances
print(p1)
print(v2)
print(c1)

# Calculate and display salaries for each employee type
print("Salary:", p2.salary())
print("Salary:", v2.salary(13))
print("Salary:", c2.salary())

# Compare instances for equality using custom __eq__ method
print(p1 == p2)
print(v1 == v2)
print(c1 == c2)
