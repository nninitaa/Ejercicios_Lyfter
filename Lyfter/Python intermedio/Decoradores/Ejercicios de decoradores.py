#Exercise 1
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling the function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_function
def sum(a, b):
    return a + b

add_result = sum(5, 3)

#Exercise 2
def log_function_2(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise ValueError("All parameters must be numbers")
            
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("All parameters must be numbers")
            
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_function_2
def multiply(a, b):
    return a * b

print(multiply(4, 5))

#Exercise 3
from datetime import date

class User:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    def adult_only(func):
        def wrapper(self, *args, **kwargs):
            if self.age < 18:
                raise ValueError("User must be at least 18 years old to see this movie")
            return func(self, *args, **kwargs)
        return wrapper
    
    @adult_only
    def access_restricted_content(self):
        return "Access to the movie function granted"
    
user1 = User("Nina", date(2008, 10, 23))
user2 = User("Evan", date(2001, 10, 15))

print(user1.age)  
print(user2.age)  