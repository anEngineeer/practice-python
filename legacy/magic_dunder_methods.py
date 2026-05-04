#magic methods (dunder methods) - make your objects work like built-ins

class Employee:
    raise_amount = 2

    def __init__(self, name,age,pay):
        self.name = name
        self.age = age
        self.pay = pay


    def raise_pay(self):
        self.pay = (self.pay*self.raise_amount)

    def __repr__(self): #for developers/debugging - shows how to recreate object
        return f"Employee('{self.name}', '{self.age}', '{self.pay}')"
    
    def __str__(self): #for users - friendly display  
        return f"{self.name} (age {self.age}) earns ${self.pay}"

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.name)

emp1 = Employee("prateek", 31, 2000)
emp2 = Employee("John", 25, 5000)

print("Original pay:", emp1.pay)
emp1.raise_pay()
print("After raise:", emp1.pay)

print(repr(emp1)) #for debugging - shows constructor format
print(str(emp1))  #for users - friendly display
print(emp1)       #automatically uses __str__ when printing 

print(emp1 + emp2) #this will use the __add__ method
print(len(emp1)) #this will use the __len__ method