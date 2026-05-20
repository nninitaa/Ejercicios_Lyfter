class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def name (self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value  
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value
    
    def promote(self):
        self.salary *= 1.10
        print(f"{self.name} has been promoted. New salary: {self.salary}")

employee = Employee("Alice", 50000)
print(employee.name)

employee.promote()

#Exercise 2

from abc import ABC, abstractmethod

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class User(ABC):
    def __init__(self, username):
        self.username = username
    @abstractmethod
    def get_role(self):
        pass
    def has_permission(self, permission):
        return permission in self.get_role().permissions

class AdminUser(User):
    def get_role(self):
        return Role("Admin", ["read", "write", "delete"])
    
class RegularUser(User):
    def get_role(self):
        return Role("Regular", ["read"])
    
user1 = AdminUser("Bob")
user2 = RegularUser("Charlie")

print(user1.has_permission("delete"))  
print(user2.has_permission("delete"))  

#Exercise 3
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def get_info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
        
    def get_info(self):
        return f"{super().get_info()} - {self.num_doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
        
    def get_info(self):
        sidecar_info = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{super().get_info()} - {sidecar_info}"
    
Vehicle = Car("Toyota", 2020, 4)
print(Vehicle.get_info())
Vehicle = Motorcycle("Harley-Davidson", 2018, True)
print(Vehicle.get_info())
