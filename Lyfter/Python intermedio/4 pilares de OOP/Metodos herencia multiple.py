#Basic example of multiple inheritance in Python. 
class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is turned on.")

    def turn_off(self):
        print(f"{self.name} is turned off.")
        
class Portability:
    def __init__(self, weight, battery_life):
        self.weight = weight
        self.battery_life = battery_life
        
    def is_lightweight(self):
        return self.weight < 1.5
    
    def show_battery_life(self):
        print(f"Battery life: {self.battery_life} hours")
        
class Smartphone(Device, Portability):
    def __init__(self, name, weight, battery_life):
        Device.__init__(self, name)
        Portability.__init__(self, weight, battery_life)
        
    def make_call(self, number):
        print(f"Calling {number} from {self.name}...")
        
#We can also use super() to call the parent class methods, but in this case we have two parent classes, so we need to specify which one we want to call.
class Laptop(Device, Portability):
    def __init__(self, name, weight, battery_life):
        super().__init__(name)
        Portability.__init__(self, weight, battery_life)
        
    def run_program(self, program_name):
        print(f"Running {program_name} on {self.name}...")  
        
#Conflict resolution: If both parent classes have a method with the same name, the method from the first parent class in the inheritance list will be called.
class HybridDevice(Device, Portability):
    def __init__(self, name, weight, battery_life):
        super().__init__(name)
        Portability.__init__(self, weight, battery_life)
        
    def turn_on(self):
        print(f"{self.name} is booting up...")          