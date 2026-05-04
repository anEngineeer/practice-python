class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, pay={self.pay})"

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age}, pay={self.pay})"
    def full_name(self):
        return (f"{self.name}")


emp1 = Employee("Prateek", 20, 1000)

print(emp1) #prints the string representation of the employee object
print(emp1.name)

emp1.full_name()
Employee.full_name(emp1) #these both are same but the difference is that the first one is called as instance method and the second one is called as class method, in instance method self was automatically passed as the first argument but in class method we need to pass it explicitly


############################################################

#class variables

class Employee:
    raise_amount = 1.04 #this is a class variable and it is shared by all the instances of the class, we needed it because if we want to change the raise amount for all the instances of the class then we can change it here and it will be reflected in all the instances of the class and we do not need to change it in each instance of the class
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def raise_pay(self):
        self.pay = self.pay * self.raise_amount #we have to use self.raise_amount because if we use raise_amount then it will be treated as a local variable and it will not be shared by all the instances of the class 
#if we just use raise_amount then it will be treated as a local variable and it will not be shared by all the instances of the class 
#either we can do self.raise_amount or Employee.raise_amount but we need to use self.raise_amount if we want to change the raise amount for a specific instance of the class and we need to use Employee.raise_amount if we want to change the raise amount for all the instances of the class
emp1 = Employee("Prateek", 20, 1000)
emp2 = Employee("John", 25, 2000)

print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)

print(emp2.pay)
emp2.raise_pay()
print(emp2.pay)
        
print("--------------------------------------------------------")
#the class variable is shared by all the instances of the class
print(Employee.raise_amount) #this will print 1.04
print(emp1.raise_amount) #this will print 1.04
print(emp2.raise_amount) #this will print 1.04

Employee.raise_amount = 1.05 #this will change the raise amount for all the instances of the class
print(Employee.raise_amount) #this will print 1.05
print(emp1.raise_amount) #this will print 1.05
print(emp2.raise_amount) #this will print 1.05

emp1.raise_amount = 1.06 #this will change the raise amount for the specific instance of the class
print(emp1.raise_amount) #this will print 1.06
print(emp2.raise_amount) #this will print 1.05

print("--------------------------------------------------------")

print(emp1.__dict__) #this will print the dictionary of the instance of the class
print(emp2.__dict__) #this will print the dictionary of the instance of the class
print(Employee.__dict__) #this will print the dictionary of the class

print("--------------------------------------------------------")
