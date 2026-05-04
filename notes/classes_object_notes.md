#classes and objects in python - easy understanding like corey schafer explains

#why do we need classes? imagine you want to create many employees
#without class you would do this manually for each employee:
# emp1_name = "John"
# emp1_age = 25
# emp1_salary = 50000
# emp2_name = "Sarah"  
# emp2_age = 30
# emp2_salary = 60000
#this gets messy very quickly!

###############################################################

#basic class without __init__ (the hard way)
class Employee:
    pass

#creating objects the manual way - you have to set everything yourself
emp1 = Employee()
emp1.name = "John"      #manually assign name
emp1.age = 25           #manually assign age
emp1.salary = 50000     #manually assign salary

emp2 = Employee()
emp2.name = "Sarah"     #manually assign name again
emp2.age = 30           #manually assign age again
emp2.salary = 60000     #manually assign salary again

print(f"{emp1.name} is {emp1.age} years old and earns ${emp1.salary}")
print(f"{emp2.name} is {emp2.age} years old and earns ${emp2.salary}")

###############################################################

#better way - using __init__ (constructor) - automatic assignment!
class BetterEmployee:
    def __init__(self, name, age, salary):
        #self refers to the specific instance being created
        self.name = name        #self.name creates an attribute on THIS instance
        self.age = age          #self.age creates an attribute on THIS instance  
        self.salary = salary    #self.salary creates an attribute on THIS instance

#now creating objects is much easier - values assigned automatically!
emp3 = BetterEmployee("Mike", 28, 55000)  #__init__ runs automatically
emp4 = BetterEmployee("Lisa", 32, 65000)  #__init__ runs automatically

print(f"{emp3.name} is {emp3.age} years old and earns ${emp3.salary}")
print(f"{emp4.name} is {emp4.age} years old and earns ${emp4.salary}")

###############################################################

#what is self? - it's the instance that's calling the method
#when you do emp3 = BetterEmployee("Mike", 28, 55000)
#python automatically does this: BetterEmployee.__init__(emp3, "Mike", 28, 55000)
#so self = emp3 (the object we just created)

class ExplainSelf:
    def __init__(self, name):
        print(f"self is: {self}")  #shows memory address of the object
        print(f"id of self: {id(self)}")
        self.name = name
        
obj1 = ExplainSelf("Test1")
print(f"obj1 is: {obj1}")
print(f"id of obj1: {id(obj1)}")
print("See? self and obj1 are the same object!")
print()

###############################################################

#why self.name and not just name?
class WrongWay:
    def __init__(self, name, age):
        name = name        #this just creates a local variable
        age = age          #this just creates a local variable
        #these variables disappear when __init__ finishes!
        
class RightWay:  
    def __init__(self, name, age):
        self.name = name   #this creates an attribute on the object
        self.age = age     #this creates an attribute on the object
        #these attributes stay with the object forever!

wrong_emp = WrongWay("John", 25)
# print(wrong_emp.name)  #this would give AttributeError!

right_emp = RightWay("John", 25) 
print(right_emp.name)  #this works! prints "John"

###############################################################

#self.name vs self._name - what's the difference?
class NamingConventions:
    def __init__(self, public_name, private_info):
        self.name = public_name           #public attribute - anyone can access
        self._internal_id = private_info  #"private" attribute - convention says don't touch
        
emp = NamingConventions("Alice", "EMP001")
print(emp.name)        #this is fine - public attribute
print(emp._internal_id) #this works but convention says you shouldn't do it

#the underscore _ is just a convention - it means "this is internal, don't use it"
#python doesn't actually stop you from accessing _private attributes

###############################################################

#adding methods to classes
class EmployeeWithMethods:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age  
        self.salary = salary
        
    def introduce(self):  #self is needed here too!
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
        
    def give_raise(self, amount):
        self.salary += amount  #modifying the object's attribute
        return f"{self.name} got a raise! New salary: ${self.salary}"

emp5 = EmployeeWithMethods("Bob", 27, 45000)
print(emp5.introduce())  #python automatically passes emp5 as self
print(emp5.give_raise(5000))

###############################################################

#class vs instance attributes
class Company:
    company_name = "TechCorp"  #class attribute - shared by all instances
    
    def __init__(self, employee_name):
        self.name = employee_name  #instance attribute - unique to each instance

emp_a = Company("John")
emp_b = Company("Sarah")

print(f"emp_a works at {emp_a.company_name}")  #TechCorp
print(f"emp_b works at {emp_b.company_name}")  #TechCorp (same for all)
print(f"emp_a name: {emp_a.name}")             #John (different for each)
print(f"emp_b name: {emp_b.name}")             #Sarah (different for each)

#changing class attribute affects everyone
Company.company_name = "NewTech"
print(f"emp_a now works at {emp_a.company_name}")  #NewTech
print(f"emp_b now works at {emp_b.company_name}")  #NewTech

###############################################################

#summary:
# - __init__ runs automatically when you create an object
# - self refers to the specific instance being created/used
# - self.attribute creates an attribute that stays with the object
# - without self, variables are just local and disappear
# - self._name is a convention for "private" (internal use only)
# - self.name is public (anyone can use)
# - python automatically passes the instance as self when calling methods