#class method
class Employee:
    raise_amount = 1.04
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def raise_pay(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount      #we need class method because we want to change the raise amount for all the instances of the class

emp1 = Employee("Prateek", 20, 1000)
emp2 = Employee("John", 25, 2000)

print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amount(1.05) #here we chnaged the raise amount for all the instances of the class using the class method
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.raise_amount)

#in real world example of class method usage is

#Here are three "Pro-Level" examples formatted for your practice file. These show how **Class Methods** act as the "Entry Doors" (Factories) and **Instance Methods** act as the "Workers" (Logic).

### **Example 1: The User Factory (Multi-Format Input)**
#**Scenario:** You need to create a `User` object, but the data comes from different places (a manual form, a Database dictionary, or an API JSON).

from calendar import c
import json
from operator import length_hint

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # --- CLASS METHODS (The Factories) ---
    @classmethod
    def from_dict(cls, data):
        """Creates user from a dictionary (e.g., Database result)"""
        return cls(data['name'], data['email'])

    @classmethod
    def from_json(cls, json_str):
        """Creates user from a JSON string (e.g., API response)"""
        data = json.loads(json_str)
        return cls(data['name'], data['email'])

    # --- INSTANCE METHOD (The Worker) ---
    def send_alert(self, message):
        print(f"Sending alert to {self.email}: {message}")

# Usage
u1 = User.from_dict({"name": "Alice", "email": "alice@dev.com"})
u2 = User.from_json('{"name": "Bob", "email": "bob@api.com"}')

u1.send_alert("System Maintenance")


### **Example 2: The Config Manager (Environment Control)**
#**Scenario:** A real app needs to load settings. A class method can determine if we are in "Production" or "Development" mode and set the object up accordingly.

class AppConfig:
    def __init__(self, debug_mode, db_url):
        self.debug_mode = debug_mode
        self.db_url = db_url

    # --- CLASS METHODS (The Factories) ---
    @classmethod
    def dev_mode(cls):
        """Shortcut to create a safe local setup"""
        return cls(debug_mode=True, db_url="localhost:5432")

    @classmethod
    def prod_mode(cls):
        """Shortcut to create a strict production setup"""
        return cls(debug_mode=False, db_url="production-db-01.aws.com")

    # --- INSTANCE METHOD (The Worker) ---
    def show_status(self):
        status = "ON" if self.debug_mode else "OFF"
        print(f"App running on {self.db_url}. Debug: {status}")

# Usage
current_app = AppConfig.prod_mode()
current_app.show_status()


### **Example 3: The Time Converter (Input Normalization)**
#**Scenario:** You have a `Timer` class that expects seconds, but sometimes your input is in Minutes or Hours.
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    # --- CLASS METHODS (The Factories) ---
    @classmethod
    def from_minutes(cls, mins):
        """Converts minutes to seconds and returns object"""
        return cls(mins * 60)

    @classmethod
    def from_hours(cls, hrs):
        """Converts hours to seconds and returns object"""
        return cls(hrs * 3600)

    # --- INSTANCE METHOD (The Worker) ---
    def start(self):
        print(f"Timer set for {self.seconds} seconds. Counting down...")

# Usage
t1 = Timer.from_minutes(5)
t2 = Timer.from_hours(1)

t1.start()

### **Quick Note for your Practice File:**
#* **Instance Methods (`self`)**: Use these for actions that happen **after** the object is alive (like `send_alert`, `start`, `show_status`).
#* **Class Methods (`cls`)**: Use these as **Specialized Constructors**. They do the math or parsing *before* the object is created, then return a "ready-to-use" instance.

#**Since these patterns are used in almost every Python library (like Pandas or Django)

#writing a Factory method for a 'Rectangle' class that creates a Square?

class Rectangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    @classmethod
    def check_square(cls, side):
        return cls(side,side)
    
    def area_rectangle(self):
        return self.length*self.breadth


#Static Methods

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    @staticmethod
    def check_square(length, breadth): #static methods are used as an helper function for the class
        if length == breadth:
            return True
        else:
            return False
    
    def area_rectangle(self):
        return self.length*self.breadth


length = 40
breadth = 20

print(Rectangle.check_square(length,breadth))
