#composition - "has-a" relationship instead of "is-a" (inheritance)

#composition vs inheritance - when to use what?
# Inheritance: "IS-A" relationship (Dog IS an Animal)
# Composition: "HAS-A" relationship (Car HAS an Engine)

#example 1 - car has engine, wheels, etc.
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.horsepower}hp {self.fuel_type} engine started"
        return "Engine already running"
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Engine stopped"
        return "Engine already stopped"

class Wheel:
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand
        self.pressure = 32  #psi
    
    def inflate(self, psi):
        self.pressure = psi
        return f"Wheel inflated to {psi} psi"

class GPS:
    def __init__(self):
        self.current_location = "Unknown"
    
    def navigate_to(self, destination):
        return f"Navigating from {self.current_location} to {destination}"

#car HAS engine, wheels, gps - composition
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Composition - Car HAS these components
        self.engine = Engine(300, "gasoline")  #car owns an engine
        self.wheels = [Wheel(18, "Michelin") for _ in range(4)]  #car owns 4 wheels
        self.gps = GPS()  #car owns a gps system
        self.is_moving = False
    
    def start_car(self):
        result = self.engine.start()
        return f"{self.make} {self.model}: {result}"
    
    def drive(self, destination):
        if not self.engine.is_running:
            return "Cannot drive - engine not running"
        
        navigation = self.gps.navigate_to(destination)
        self.is_moving = True
        return f"Driving to {destination}. {navigation}"
    
    def check_tires(self):
        tire_status = []
        for i, wheel in enumerate(self.wheels, 1):
            tire_status.append(f"Tire {i}: {wheel.size}\" {wheel.brand} at {wheel.pressure} psi")
        return tire_status

#usage
my_car = Car("Toyota", "Camry")
print(my_car.start_car())  #Toyota Camry: 300hp gasoline engine started
print(my_car.drive("Mall"))  #Driving to Mall. Navigating from Unknown to Mall

for tire in my_car.check_tires():
    print(tire)

#accessing composed objects directly
print(my_car.engine.horsepower)  #300
my_car.wheels[0].inflate(35)  #Wheel inflated to 35 psi

###############################################################

#real-world example - company has employees (composition vs inheritance)
class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city  
        self.state = state
        self.zip_code = zip_code
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"

class Department:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.employees = []  #composition - department HAS employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self  #back reference
    
    def get_total_salaries(self):
        return sum(emp.salary for emp in self.employees)

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address  #composition - employee HAS address
        self.department = None  #will be set when added to department
    
    def get_contact_info(self):
        return f"{self.name} at {self.address}"
    
    def relocate(self, new_address):
        old_address = self.address
        self.address = new_address
        return f"{self.name} moved from {old_address} to {new_address}"

#company HAS departments, departments HAVE employees, employees HAVE addresses
class Company:
    def __init__(self, name):
        self.name = name
        self.headquarters = None
        self.departments = []  #composition - company HAS departments
    
    def add_department(self, department):
        self.departments.append(department)
    
    def set_headquarters(self, address):
        self.headquarters = address
    
    def get_total_employees(self):
        return sum(len(dept.employees) for dept in self.departments)
    
    def get_company_payroll(self):
        return sum(dept.get_total_salaries() for dept in self.departments)

#building the company structure with composition
company = Company("TechCorp")
company.set_headquarters(Address("123 Tech St", "San Francisco", "CA", "94105"))

#create departments
engineering = Department("Engineering", 2000000)
marketing = Department("Marketing", 500000)

#create employees with addresses
emp1 = Employee("Alice Johnson", 120000, Address("456 Code Ave", "Palo Alto", "CA", "94301"))
emp2 = Employee("Bob Smith", 110000, Address("789 Debug Dr", "Mountain View", "CA", "94041"))
emp3 = Employee("Carol Wilson", 80000, Address("321 Brand Blvd", "San Jose", "CA", "95110"))

#compose the structure
engineering.add_employee(emp1)
engineering.add_employee(emp2)
marketing.add_employee(emp3)

company.add_department(engineering)
company.add_department(marketing)

#usage - accessing nested composed objects
print(f"Company: {company.name}")
print(f"HQ: {company.headquarters}")
print(f"Total employees: {company.get_total_employees()}")
print(f"Total payroll: ${company.get_company_payroll():,}")

print(f"\n{emp1.name} works in {emp1.department.name}")
print(f"{emp1.name}'s contact: {emp1.get_contact_info()}")

#employee relocates
new_address = Address("999 New St", "Berkeley", "CA", "94702")
print(emp1.relocate(new_address))

###############################################################

#composition vs inheritance example - shapes
#inheritance approach (can be limiting)
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):  #Circle IS-A Shape
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

#composition approach (more flexible)
class Color:
    def __init__(self, name, hex_code):
        self.name = name
        self.hex_code = hex_code
    
    def __str__(self):
        return f"{self.name} ({self.hex_code})"

class Border:
    def __init__(self, width, style):
        self.width = width
        self.style = style  #solid, dashed, dotted
    
    def __str__(self):
        return f"{self.width}px {self.style}"

class FlexibleCircle:
    def __init__(self, radius):
        self.radius = radius
        self.fill_color = None  #composition - circle HAS color
        self.border = None      #composition - circle HAS border
    
    def set_fill_color(self, color):
        self.fill_color = color
    
    def set_border(self, border):
        self.border = border
    
    def describe(self):
        desc = f"Circle with radius {self.radius}"
        if self.fill_color:
            desc += f", filled with {self.fill_color}"
        if self.border:
            desc += f", border: {self.border}"
        return desc

#usage - much more flexible with composition
red = Color("Red", "#FF0000")
blue = Color("Blue", "#0000FF")
thick_border = Border(5, "solid")
dashed_border = Border(2, "dashed")

circle1 = FlexibleCircle(10)
circle1.set_fill_color(red)
circle1.set_border(thick_border)

circle2 = FlexibleCircle(15)
circle2.set_fill_color(blue)
circle2.set_border(dashed_border)

print(circle1.describe())  #Circle with radius 10, filled with Red (#FF0000), border: 5px solid
print(circle2.describe())  #Circle with radius 15, filled with Blue (#0000FF), border: 2px dashed

###############################################################

#real-world example - order system with composition
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    
    def __str__(self):
        return f"{self.name} (${self.price})"

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product  #composition - order item HAS product
        self.quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} = ${self.get_total_price():.2f}"

class ShippingAddress:
    def __init__(self, recipient, street, city, state, zip_code):
        self.recipient = recipient
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def __str__(self):
        return f"{self.recipient}\n{self.street}\n{self.city}, {self.state} {self.zip_code}"

class PaymentMethod:
    def __init__(self, type, last_four_digits):
        self.type = type  #credit, debit, paypal
        self.last_four_digits = last_four_digits
    
    def __str__(self):
        return f"{self.type} ending in {self.last_four_digits}"

class Order:
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.items = []  #composition - order HAS items
        self.shipping_address = None  #composition - order HAS shipping address
        self.payment_method = None    #composition - order HAS payment method
        self.status = "pending"
    
    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)
    
    def set_shipping_address(self, address):
        self.shipping_address = address
    
    def set_payment_method(self, payment):
        self.payment_method = payment
    
    def get_total_amount(self):
        return sum(item.get_total_price() for item in self.items)
    
    def get_order_summary(self):
        summary = f"Order #{self.order_id} for {self.customer_email}\n"
        summary += "Items:\n"
        for item in self.items:
            summary += f"  {item}\n"
        summary += f"Total: ${self.get_total_amount():.2f}\n"
        if self.shipping_address:
            summary += f"Ship to:\n{self.shipping_address}\n"
        if self.payment_method:
            summary += f"Payment: {self.payment_method}\n"
        summary += f"Status: {self.status}"
        return summary

#building an order with composition
laptop = Product("Gaming Laptop", 1299.99, "LAP001")
mouse = Product("Wireless Mouse", 79.99, "MOU001")

order = Order("ORD-12345", "customer@example.com")
order.add_item(laptop, 1)
order.add_item(mouse, 2)

shipping = ShippingAddress("John Doe", "123 Main St", "Anytown", "CA", "12345")
payment = PaymentMethod("Credit Card", "4567")

order.set_shipping_address(shipping)
order.set_payment_method(payment)
order.status = "confirmed"

print(order.get_order_summary())

###############################################################

#when to use composition vs inheritance:
# INHERITANCE (IS-A): Dog IS-A Animal, Manager IS-A Employee
# COMPOSITION (HAS-A): Car HAS-A Engine, Order HAS-A ShippingAddress

# Use COMPOSITION when:
# - Objects can exist independently (Engine can exist without Car)
# - You want flexibility to swap components (different payment methods)
# - Avoiding deep inheritance hierarchies
# - Components are reusable across different classes

# Use INHERITANCE when:
# - Clear "is-a" relationship (Developer is an Employee)
# - Shared behavior and attributes
# - Polymorphism needed (treat all Animals the same way)