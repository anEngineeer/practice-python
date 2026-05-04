#property decorators - making attributes smart and dynamic

#problem - static attributes get out of sync
class Employee_Problem:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"  #set once, never updates!

    def full_name(self):
        return f"{self.first} {self.last}"

emp1 = Employee_Problem("Prateek", "Mishra")
print("Before name change:")
print(f"Full name: {emp1.full_name()}")
print(f"Email: {emp1.email}")

emp1.first = 'Arpita'  #changed first name
print("\nAfter changing first name to Arpita:")
print(f"Full name: {emp1.full_name()}")  #updated
print(f"Email: {emp1.email}")  #still old email! out of sync

###############################################################

#solution - using @property decorator for dynamic attributes
class Employee_Fixed:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def full_name(self):  #calculated every time it's accessed
        return f"{self.first} {self.last}"

    @full_name.setter  #allows setting full_name like an attribute
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @property
    def email(self):  #calculated every time - always current!
        return f"{self.first}.{self.last}@company.com"

emp2 = Employee_Fixed("Prateek", "Mishra")
print("\n=== With @property decorator ===")
print("Original:")
print(f"Full name: {emp2.full_name}")  #no () needed - acts like attribute
print(f"Email: {emp2.email}")

emp2.first = 'Arpita'  #change first name
print("\nAfter changing first name:")
print(f"Full name: {emp2.full_name}")  #automatically updated
print(f"Email: {emp2.email}")  #automatically updated too!

#can set full name like an attribute thanks to @setter
emp2.full_name = "John Smith"  #no () needed
print("\nAfter setting full_name = 'John Smith':")
print(f"First: {emp2.first}")  #John
print(f"Last: {emp2.last}")   #Smith
print(f"Full name: {emp2.full_name}")  #John Smith
print(f"Email: {emp2.email}")  #john.smith@company.com

###############################################################

#real-world example - temperature converter
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  #absolute zero validation
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):  #calculated property
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9  #converts and validates
    
    @property
    def kelvin(self):  #calculated property
        return self._celsius + 273.15

temp = Temperature(25)  #25 celsius
print(f"\n=== Temperature Converter ===")
print(f"Celsius: {temp.celsius}")     #25
print(f"Fahrenheit: {temp.fahrenheit}")  #77.0
print(f"Kelvin: {temp.kelvin}")       #298.15

temp.fahrenheit = 100  #set fahrenheit, celsius updates automatically
print(f"\nAfter setting fahrenheit = 100:")
print(f"Celsius: {temp.celsius}")     #37.77...
print(f"Fahrenheit: {temp.fahrenheit}")  #100
print(f"Kelvin: {temp.kelvin}")       #310.92...

#properties provide validation
# temp.celsius = -300  #would raise ValueError