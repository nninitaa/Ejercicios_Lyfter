# Exercise 1
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, min_balance=0):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            raise ValueError(f"Withdrawal denied. Balance cannot be below {self.min_balance}.")
        return super().withdraw(amount)
    
account = BankAccount("12345", 1000)
account.deposit(1000)
account.withdraw(200)

# Exercise 2
from abc import ABC, abstractmethod 
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)

figures = [circle, square, rectangle]

for figure in figures:
    print
    print(f"Area: {figure.calculate_area():.2f}")
    print(f"Perimeter: {figure.calculate_perimeter():.2f}")
    
