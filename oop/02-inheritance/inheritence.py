class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

dev_1 = Employee('Prateek', 'Singh', 50000)
dev_2 = Employee('John', 'Doe', 60000)

print(dev_1.email)
print(dev_2.email)

print(dev_1.full_name())
print(dev_2.full_name())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

#Inheritance
#we are making a developer class that inherits from the employee class because a developer is a type of employee

class Developer(Employee):
    raise_amt = 2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay) #here super is used to call the init method of the parent class
        self.prog_lang = prog_lang

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

dev_3 = Developer('Jane', 'Doe', 70000, 'Python')
dev_4 = Developer('John', 'Smith', 80000, 'Java')

print(dev_3.email)
print(dev_4.email)

print(dev_3.prog_lang)

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay) #here super is used to call the init method of the parent class
        if employees is None:
            self.employees = []
        else:
            self.employees = employees #we did no set employee directly list in paramtere because immuntable datab types not to be used as default values
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.full_name())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_3])
print(mgr_1.email)

mgr_1.add_employee(dev_4)
mgr_1.print_employees()


#isinstance and issubclass
print(isinstance(mgr_1, Manager)) #print True because mgr_1 is an instance of Manager
print(isinstance(mgr_1, Employee)) #print True because mgr_1 is an instance of Employee
print(isinstance(mgr_1, Developer)) #print False because mgr_1 is NOT an instance of Developer

print(issubclass(Developer, Employee)) #print True because Developer is a subclass of Employee
print(issubclass(Manager, Employee)) #print True because Manager is a subclass of Employee
print(issubclass(Manager, Developer)) #print False because Manager is NOT a subclass of Developer    
