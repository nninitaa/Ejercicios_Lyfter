#Ejercicio 1: Crear una clase llamada "Circle" que tenga un atributo de radio y un método para calcular el área del círculo.
class Circle: 
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
circle = Circle(5)
print(circle.area())  # Output: 78.5
    
#Ejercicio 2: Crear una clase llamada "Bus" que tenga un atributo de capacidad y un método para calcular el número de pasajeros que pueden viajar en el bus.
class Person:
    def __init__(self, name):
        self.name = name
        
class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, person):
        if len(self.passengers) < self.capacity:
            self.passengers.append(person)
            return f"{person.name} is in the bus."
        else:
            return "The bus is full."
        
    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            return f"{person.name} has left the bus."
        else:
            return f"{person.name} is not in the bus."
        
p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")              
bus = Bus(2)
print(bus.add_passenger(p1))  # Output: Alice is in the bus.
print(bus.add_passenger(p2))  # Output: Bob is  in the bus.
print(bus.add_passenger(p3))  # Output: The bus is full.
print(bus.remove_passenger(p1))  # Output: Alice has left the bus.
print(bus.add_passenger(p3))  # Output: Charlie is in the bus.
        
#Ejercicio 3: Crear una clase "Human"
class Head:
    def __init__(self):
        self.eyes = 2
        self.nose = 1
        self.mouth = 1

class Torso:
    def __init__(self):
        self.heart = True
        
class Hand:
    def __init__(self, side):
        self.side = side

class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand(side)  

class Feet:
    def __init__(self, side):
        self.side = side
        
class Leg:
    def __init__(self, side):
        self.side = side
        self.feet = Feet(side)
        
class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("left")
        self.right_arm = Arm("right")
        self.left_leg = Leg("left")
        self.right_leg = Leg("right")
        
human = Human("Nina")
print(human.name)
print(human.head.eyes)
print(human.torso.heart)