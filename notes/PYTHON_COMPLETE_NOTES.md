# 🐍 Python Complete Notes - From Zero to Hero

*A practical notebook covering everything you need to know about Python - theory meets practice in one place!*

---

## 📚 Table of Contents

1. [Basic Concepts](#basic-concepts)
2. [Control Flow](#control-flow) 
3. [Data Structures](#data-structures)
4. [Functions](#functions)
5. [Classes & Objects](#classes--objects)
6. [Advanced Class Concepts](#advanced-class-concepts)
7. [Inheritance](#inheritance)
8. [Composition](#composition)
9. [Encapsulation](#encapsulation)
10. [Abstract Classes](#abstract-classes)
11. [Magic Methods (Dunder Methods)](#magic-methods-dunder-methods)
12. [Properties & Decorators](#properties--decorators)
13. [String Operations](#string-operations)
14. [File Operations](#file-operations)

---

## Basic Concepts

### Variables - Your Data Containers
**Real-world meaning:** Variables are like labeled boxes where you store stuff you need later.

```python
# In a real app, you'd have:
user_id = 12345           # Store who's logged in
cart_total = 99.99        # Track shopping cart price
is_premium = True         # Check if user has paid subscription
username = "prateek_dev"  # Display name on profile
```

**Why this matters:** Every app needs to remember data - user info, settings, calculations, etc.

### Booleans - Your Decision Makers
**Real-world meaning:** Booleans control what happens next - like traffic lights for your code.

```python
# Real scenarios:
if user_logged_in:
    show_dashboard()      # User sees their stuff
else:
    show_login_page()     # Redirect to sign in

# Combining conditions (like real business rules)
if is_premium and credits_remaining > 0:
    allow_download()      # Premium user with credits can download
```

**Why this matters:** Every app makes decisions - "Should I send this email?", "Can this user access this feature?"

---

## Control Flow - Making Your Code Smart

### If Statements - The Gatekeepers
**Real-world meaning:** Like a bouncer at a club - checking conditions before letting code execute.

```python
# Real API example
if request.method == "POST":
    create_new_user()         # Only create user on POST request
elif request.method == "GET":  
    return_user_list()        # Return data on GET request
else:
    return_error("Invalid method")  # Block everything else

# Real validation
if len(password) < 8:
    return "Password too short"
elif "@" not in email:
    return "Invalid email"
else:
    create_account()          # All checks passed!
```

### While Loops - The Workhorses  
**Real-world meaning:** Like a factory worker that keeps doing the same task until the job is done.

```python
# Real examples:
# 1. Processing a queue of emails to send
emails_to_send = get_pending_emails()
while emails_to_send:
    email = emails_to_send.pop()
    send_email(email)
    
# 2. Waiting for user input  
user_input = ""
while user_input != "quit":
    user_input = input("Enter command (or 'quit'): ")
    process_command(user_input)
```

**⚡ Pro Tip:** In real apps, while loops process batches, handle retries, or wait for external events!

---

## Data Structures - Your Data Organizers

### Lists - The Shopping Cart of Programming
**Real-world meaning:** Like a shopping cart - you can add items, remove items, and check what's inside.

```python
# Real scenarios:
shopping_cart = []                   # Start empty
shopping_cart.append("laptop")       # User adds item
shopping_cart.append("mouse")        # User adds another
shopping_cart.remove("mouse")        # User changes mind
total_items = len(shopping_cart)     # Show cart count

# Real API response processing:
user_ids = [101, 102, 103, 104]
for user_id in user_ids:
    user_data = fetch_user(user_id)  # Get each user's info
    send_notification(user_data)     # Send them a message

# Real data filtering:
all_orders = get_todays_orders()
pending_orders = [order for order in all_orders if order.status == "pending"]
process_pending_orders(pending_orders)
```

**🎯 Real-world truth:** Lists are everywhere - user lists, product catalogs, search results, form submissions!

---

## Functions - Your Code's Building Blocks

### What Functions Really Are
**Real-world meaning:** Functions are like kitchen appliances - give them ingredients (inputs), they do their job, and give you results (outputs).

```python
# Real-world function - like a microwave
def send_email(recipient, subject, body):    # Ingredients you put in
    email_service.send(recipient, subject, body)  # The work happens
    return "Email sent successfully"         # Result you get back

# Using it:
result = send_email("user@example.com", "Welcome!", "Thanks for signing up")
```

### Scope - Your Variable's Neighborhood  
**Real-world meaning:** Like your house address - variables can only be "delivered" to the right neighborhood.

```python
# Real scenario - app settings
APP_NAME = "MyApp"  # Global - everyone in the app can see this

def process_payment(amount):
    tax_rate = 0.08  # Local - only this function knows about tax
    total = amount + (amount * tax_rate)  # Uses local tax_rate
    return total

def calculate_shipping(weight):
    tax_rate = 0.05  # Different local tax_rate - won't conflict!
    return weight * 2.5

# Each function has its own "tax_rate" - they don't interfere
payment_total = process_payment(100)    # Uses 0.08 tax rate
shipping_cost = calculate_shipping(5)   # Uses 0.05 tax rate  
```

### Default Parameters - Smart Defaults for Lazy Developers
**Real-world meaning:** Like ordering a pizza - "large pepperoni" works, but you can customize if needed.

```python
# Real API function
def create_user_account(email, password, role="user", send_welcome=True):
    user = User(email=email, password=password, role=role)
    if send_welcome:
        send_welcome_email(email)
    return user

# Real usage:
create_user_account("john@example.com", "secret123")  # Gets default role + welcome email
create_user_account("admin@company.com", "admin123", role="admin")  # Custom role
create_user_account("test@test.com", "test", send_welcome=False)  # No welcome email

# Real configuration function  
def connect_database(host, port=5432, timeout=30, ssl=True):
    return Database.connect(host, port, timeout, ssl)
    
# Most of the time, defaults work:
db = connect_database("localhost")  # Uses port 5432, timeout 30, ssl True
```

### The Tricky Part - When Your Data Gets Modified Behind Your Back

**Real-world meaning:** Like lending your car vs. giving directions to your house - sometimes people modify your stuff, sometimes they don't.

#### Case 1: Function Makes a Copy (Your Original is Safe)
```python
def process_order_copy(items):
    items = items + ["receipt"]  # Makes NEW list, doesn't touch original
    print(f"Processing: {items}")

shopping_cart = ["laptop", "mouse"]
process_order_copy(shopping_cart)
print(f"Your cart: {shopping_cart}")  # Still ["laptop", "mouse"] - unchanged!
```

#### Case 2: Function Modifies Your Original (Surprise!)
```python
def add_taxes_to_cart(items):
    items.append("tax_charge")  # Modifies YOUR original list!

shopping_cart = ["laptop", "mouse"]  
add_taxes_to_cart(shopping_cart)
print(f"Your cart: {shopping_cart}")  # Now ["laptop", "mouse", "tax_charge"] - changed!
```

#### Case 3: The Sneaky += Operator
```python
# Real scenario - processing user uploads
def backup_files_wrong(file_list):
    file_list = file_list + ["backup.zip"]  # Creates new list - original safe

def backup_files_sneaky(file_list):  
    file_list += ["backup.zip"]  # Modifies original list - surprise!

user_files = ["photo1.jpg", "doc.pdf"]
backup_files_wrong(user_files)
print(user_files)  # ["photo1.jpg", "doc.pdf"] - unchanged

backup_files_sneaky(user_files)  
print(user_files)  # ["photo1.jpg", "doc.pdf", "backup.zip"] - changed!
```

**🔥 Real-world rule:** If you don't want your data modified, make copies inside functions. If you DO want modifications, use methods like `.append()`, `.extend()`, or `+=`.

---

## Classes & Objects - Your Data + Behavior Bundles

### Why Classes Exist - The Cookie Cutter Problem
**Real-world meaning:** Classes are like cookie cutters - one template that makes many similar things with different details.

**Without Classes (The Nightmare):**
```python
# Imagine managing 1000 users this way - pure chaos!
user1_id = 12345
user1_email = "john@example.com"  
user1_is_premium = False
user1_login_count = 5

user2_id = 12346
user2_email = "sarah@example.com"
user2_is_premium = True  
user2_login_count = 45

# How do you send an email to user1? Write separate function for each user? No way!
```

**With Classes (The Professional Way):**
```python
class User:
    def __init__(self, user_id, email, is_premium=False):
        self.user_id = user_id      # Store user's unique ID
        self.email = email          # Store their email 
        self.is_premium = is_premium # Store subscription status
        self.login_count = 0        # Track how often they login
        
    def send_email(self, subject, body):
        email_service.send(self.email, subject, body)
        
    def upgrade_to_premium(self):
        self.is_premium = True
        self.send_email("Welcome to Premium!", "You now have premium features!")

# Now managing 1000 users is easy:
user1 = User(12345, "john@example.com")
user2 = User(12346, "sarah@example.com", is_premium=True)

# Same method works for any user:
user1.send_email("Hi John!", "Check out our new features")
user2.upgrade_to_premium()  # Already premium, but method still works
```

### Understanding `self` - The "Which User Am I?" Problem

**Real-world meaning:** `self` is like a name tag that says "I'm working on THIS specific user right now."

```python
# Real scenario - you have 1000 users, method gets called:
user_john = User("john@example.com")  
user_sarah = User("sarah@example.com")

# When you call:
user_john.send_email("Hi!", "Welcome")

# Python internally does:
# User.send_email(user_john, "Hi!", "Welcome")
#                 ^^^^^^^^^ this becomes 'self'

# So inside send_email method:
def send_email(self, subject, body):
    # self = user_john (the specific user we're working with)
    email_service.send(self.email, subject, body)  # Uses john@example.com
    
# If Sarah calls it:
user_sarah.send_email("Hi!", "Welcome")  
# Now self = user_sarah, so it uses sarah@example.com

# The magic: same method, different user data!
```

**Real proof that self = the specific object:**
```python
class User:
    def __init__(self, email):
        print(f"Creating user, self is: {id(self)}")  # Memory location
        self.email = email
        
user1 = User("test@example.com")
print(f"user1 is: {id(user1)}")  # Same memory location!
# They're literally the same thing in memory
```

### Why `self.name` and Not Just `name`? - The Sticky Note Problem

**Real-world meaning:** `name = name` is like writing on a sticky note that gets thrown away. `self.name = name` is like writing in the user's permanent file.

```python
# Real scenario - user registration
class UserAccount:
    def __init__(self, email, password):
        # WRONG - just creates temporary variables that disappear:
        email = email      # Like writing on a sticky note
        password = password # Gets thrown away when __init__ ends
        
    def login(self):
        # ERROR! email doesn't exist here
        if check_password(email, password):  # NameError!
            return "Login successful"

# vs. 

class UserAccount:
    def __init__(self, email, password):
        # RIGHT - saves to the user's permanent record:
        self.email = email      # Writes to user's file
        self.password = password # Stays with user forever
        
    def login(self):
        # Works! email is in the user's permanent record
        if check_password(self.email, self.password):
            return "Login successful"

# Real usage:
user = UserAccount("john@example.com", "secret123")
# Later, maybe next week, user tries to login:
result = user.login()  # Still works because data was saved with 'self.'
```

**The technical truth:** Variables without `self` are like RAM - wiped clean when the function ends. Variables with `self` are like hard drive - saved permanently with the object.

### Naming Conventions - Quick Rule
```python
class User:
    def __init__(self, name, user_id):
        self.name = name           # Public - anyone can use
        self._user_id = user_id    # "Private" - don't touch (convention)

user = User("Alice", "12345")
print(user.name)      # ✅ Good - public
print(user._user_id)  # ⚠️  Bad style - private by convention
```

### Adding Methods - Actions Your Objects Can Do
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return f"${amount} withdrawn. Balance: ${self.balance}"
        
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. Balance: ${self.balance}"

account = BankAccount("John", 1000)
print(account.withdraw(100))  # $100 withdrawn. Balance: $900
print(account.deposit(50))    # $50 deposited. Balance: $950
```

### Class vs Instance Attributes - Shared vs Personal Data
```python
class User:
    app_name = "MyApp"  # Shared by ALL users
    
    def __init__(self, username):
        self.username = username  # Personal to each user

user1 = User("john")
user2 = User("sarah") 

print(user1.app_name)    # MyApp (same for everyone)
print(user1.username)    # john (personal)
print(user2.username)    # sarah (personal)

# Change shared data affects everyone
User.app_name = "MyApp 2.0"
print(user1.app_name)    # MyApp 2.0 (both users see it)
```

---

## Advanced Class Concepts - The Three Flavors of Methods

### The Real-World Method Types

| Feature | Instance Method (`self`) | Class Method (`cls`) | Static Method |
|---------|-------------------------|---------------------|---------------|
| **Real Purpose** | "Do something to THIS user" | "Create a user in a special way" | "Utility function related to users" |
| **Access** | Works with specific object data | Works with the class itself | Works with nothing - just helper |
| **Decorator** | None | `@classmethod` | `@staticmethod` |
| **When You Use It** | User actions, data modification | Alternative constructors, global settings | Validation, calculations, utilities |

### Instance Methods - The "Do Something to THIS Specific Thing" Methods
**Real-world meaning:** Like pressing "Send Message" on a specific user's profile - the action happens to THAT user.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount):  # Instance method - works on THIS account
        if amount <= self.balance:
            self.balance -= amount
            return f"{self.owner} withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds"
    
    def transfer_to(self, other_account, amount):  # Works with THIS account's data
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            return f"Transferred ${amount} from {self.owner} to {other_account.owner}"

# Real usage:
johns_account = BankAccount("John", 1000)
sarahs_account = BankAccount("Sarah", 500)

johns_account.withdraw(100)  # Works on John's account specifically
johns_account.transfer_to(sarahs_account, 200)  # John sends money to Sarah
```

### Class Methods - The "Alternative Constructor" and "Global Settings" Methods
**Real-world meaning:** Like having different ways to create the same thing, or changing settings that affect everyone.

```python
class User:
    premium_price = 9.99  # Global setting for all users
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_premium = False
    
    @classmethod
    def set_premium_price(cls, new_price):  # Change global setting
        cls.premium_price = new_price  # Affects ALL users
        print(f"Premium price changed to ${new_price} for everyone!")
    
    @classmethod 
    def from_google_login(cls, google_data):  # Alternative way to create user
        email = google_data['email']
        # No password needed for Google users
        user = cls(email, password=None)  
        user.auth_method = "google"
        return user
    
    @classmethod
    def from_facebook_login(cls, facebook_data):  # Another way to create user
        email = facebook_data['email']  
        user = cls(email, password=None)
        user.auth_method = "facebook"
        return user

# Real usage:
# Regular signup
user1 = User("john@example.com", "password123")

# Google login - different creation method
google_user_data = {"email": "sarah@gmail.com", "id": "12345"}
user2 = User.from_google_login(google_user_data)  

# Change pricing for everyone
User.set_premium_price(12.99)  # Now ALL users see new premium price
```

### Static Methods - The "Related Helper Functions" That Don't Need Data
**Real-world meaning:** Like a calculator app on your phone - related to the app but doesn't need your personal data.

```python
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    @staticmethod
    def is_valid_email(email):  # Doesn't need ANY user data
        return "@" in email and "." in email  # Simple validation
    
    @staticmethod  
    def generate_temp_password():  # Doesn't need user data
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    @staticmethod
    def hash_password(plain_password):  # Utility function
        import hashlib
        return hashlib.sha256(plain_password.encode()).hexdigest()

# Real usage - you can use these WITHOUT creating a user:
if User.is_valid_email("john@example.com"):  # Valid email check
    temp_pass = User.generate_temp_password()  # Get random password
    hashed = User.hash_password(temp_pass)     # Hash it for security
    user = User("john@example.com", hashed)   # Now create user

# These are just utility functions grouped with the User class for organization
```

### Real-World Factory Examples

#### 1. Multi-Format User Creation
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data):
        """Creates user from database result"""
        return cls(data['name'], data['email'])

    @classmethod  
    def from_json(cls, json_str):
        """Creates user from API response"""
        import json
        data = json.loads(json_str)
        return cls(data['name'], data['email'])

    def send_alert(self, message):  # Instance method
        print(f"Alert to {self.email}: {message}")

# Usage - multiple ways to create the same thing!
u1 = User.from_dict({"name": "Alice", "email": "alice@dev.com"})
u2 = User.from_json('{"name": "Bob", "email": "bob@api.com"}')
u1.send_alert("System down!")
```

#### 2. Environment Configuration
```python
class AppConfig:
    def __init__(self, debug_mode, db_url):
        self.debug_mode = debug_mode
        self.db_url = db_url

    @classmethod
    def dev_mode(cls):
        """Quick setup for development"""
        return cls(debug_mode=True, db_url="localhost:5432")

    @classmethod
    def prod_mode(cls):
        """Quick setup for production"""  
        return cls(debug_mode=False, db_url="production-db.aws.com")

    def show_status(self):  # Instance method
        status = "ON" if self.debug_mode else "OFF"
        print(f"Running on {self.db_url}. Debug: {status}")

# Usage - one line setup!
app = AppConfig.prod_mode()
app.show_status()
```

**🚀 Real-world pattern:** 
- **Instance Methods** = "Do something to THIS user/order/account"
- **Class Methods** = "Create a user/order/account in a special way" or "Change global settings"  
- **Static Methods** = "Helper functions that happen to be related to users/orders/accounts"

---

## Inheritance - Code Reuse Like a Pro

### What Inheritance Really Means
**Real-world meaning:** Like job roles in a company - a Developer IS an Employee but with extra skills.

```python
# Base class - common things ALL employees have
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last  
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay *= 1.04  # Standard 4% raise

# Specialized class - Developer IS an Employee + coding skills
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Get all Employee stuff
        self.prog_lang = prog_lang  # Add developer-specific data
    
    def apply_raise(self):  # Override - developers get bigger raises
        self.pay *= 1.10  # 10% raise for developers

# Another specialized class - Manager IS an Employee + team management
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees or []  # Manage a team
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def print_team(self):
        for emp in self.employees:
            print(f"  -> {emp.full_name()}")

# Real usage:
dev = Developer("John", "Doe", 70000, "Python")
mgr = Manager("Sarah", "Smith", 90000)

print(dev.email)      # Works - inherited from Employee  
print(dev.prog_lang)  # Works - specific to Developer
dev.apply_raise()     # Uses Developer's 10% raise, not Employee's 4%

mgr.add_employee(dev) # Manager-specific method
mgr.print_team()      # Shows John Doe
```

### Checking Types - isinstance() and issubclass()
```python
# Real validation scenarios:
print(isinstance(dev, Developer))  # True - dev is a Developer
print(isinstance(dev, Employee))   # True - dev is ALSO an Employee  
print(isinstance(mgr, Developer))  # False - mgr is not a Developer

print(issubclass(Developer, Employee))  # True - Developer extends Employee
print(issubclass(Manager, Employee))    # True - Manager extends Employee  
print(issubclass(Manager, Developer))   # False - Manager doesn't extend Developer
```

**🎯 Real-world uses:** User roles (AdminUser extends User), Product types (DigitalProduct extends Product), Vehicle types (Car extends Vehicle)

---

## Composition - Building Complex Objects from Simple Parts

### Inheritance vs Composition - The Key Difference
**Real-world meaning:** 
- **Inheritance (IS-A):** Dog IS an Animal (inherits all Animal traits)
- **Composition (HAS-A):** Car HAS an Engine (owns/contains an Engine object)

```python
# Inheritance - "IS-A" relationship
class Animal:
    def breathe(self):
        return "breathing..."

class Dog(Animal):  # Dog IS an Animal
    def bark(self):
        return "Woof!"

# Composition - "HAS-A" relationship  
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.horsepower}hp engine started"

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(300)  # Car HAS an Engine (composition)
    
    def start_car(self):
        return f"{self.make}: {self.engine.start()}"

# Usage:
dog = Dog()
print(dog.breathe())  # inherited method
print(dog.bark())     # own method

car = Car("Toyota", "Camry")  
print(car.start_car())  # Toyota: 300hp engine started
print(car.engine.horsepower)  # accessing composed object: 300
```

### Real Example - Company Structure with Composition
```python
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"

class Department:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.employees = []  # Department HAS employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address  # Employee HAS address
        self.department = None
    
    def get_contact_info(self):
        return f"{self.name} at {self.address}"

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Company HAS departments
        self.headquarters = None  # Company HAS headquarters
    
    def add_department(self, dept):
        self.departments.append(dept)
    
    def get_total_employees(self):
        return sum(len(dept.employees) for dept in self.departments)

# Building the structure with composition:
company = Company("TechCorp")
company.headquarters = Address("123 Tech St", "San Francisco", "CA")

engineering = Department("Engineering", 2000000)
marketing = Department("Marketing", 500000)

emp1 = Employee("Alice", 120000, Address("456 Code Ave", "Palo Alto", "CA"))
emp2 = Employee("Bob", 80000, Address("789 Brand Blvd", "San Jose", "CA"))

engineering.add_employee(emp1)
marketing.add_employee(emp2)

company.add_department(engineering)
company.add_department(marketing)

# Accessing nested composed objects:
print(f"Company: {company.name} at {company.headquarters}")
print(f"Total employees: {company.get_total_employees()}")
print(f"{emp1.name} works in {emp1.department.name}")
print(f"Contact: {emp1.get_contact_info()}")
```

### Real Example - E-commerce Order System
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product  # OrderItem HAS Product
        self.quantity = quantity
    
    def get_total(self):
        return self.product.price * self.quantity

class ShippingAddress:
    def __init__(self, recipient, street, city):
        self.recipient = recipient
        self.street = street  
        self.city = city
    
    def __str__(self):
        return f"{self.recipient}, {self.street}, {self.city}"

class PaymentMethod:
    def __init__(self, type, last_four):
        self.type = type
        self.last_four = last_four
    
    def __str__(self):
        return f"{self.type} ending in {self.last_four}"

class Order:
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.items = []  # Order HAS items
        self.shipping_address = None  # Order HAS shipping address
        self.payment_method = None    # Order HAS payment method
    
    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)
    
    def get_total(self):
        return sum(item.get_total() for item in self.items)
    
    def set_shipping(self, address):
        self.shipping_address = address
    
    def set_payment(self, payment):
        self.payment_method = payment

# Building an order with composition:
laptop = Product("Gaming Laptop", 1299.99)
mouse = Product("Wireless Mouse", 79.99)

order = Order("ORD-12345", "customer@example.com")
order.add_item(laptop, 1)
order.add_item(mouse, 2)

shipping = ShippingAddress("John Doe", "123 Main St", "Anytown")
payment = PaymentMethod("Credit Card", "4567")

order.set_shipping(shipping)
order.set_payment(payment)

print(f"Order total: ${order.get_total()}")
print(f"Ship to: {order.shipping_address}")
print(f"Payment: {order.payment_method}")
```

### When to Use Composition vs Inheritance

| Use Composition When: | Use Inheritance When: |
|----------------------|----------------------|
| Objects can exist independently | Clear "is-a" relationship |
| You want to swap components | Shared behavior needed |
| Avoiding complex inheritance | Polymorphism required |
| Components are reusable | Natural hierarchy exists |

```python
# Good use of Composition:
class Car:
    def __init__(self):
        self.engine = Engine()    # Can swap different engines
        self.wheels = [Wheel()] * 4  # Can change wheel types
        self.gps = GPS()          # Can upgrade GPS system

# Good use of Inheritance:
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):     # Car IS-A Vehicle
    def move(self):
        return "Driving on roads"

class Boat(Vehicle):    # Boat IS-A Vehicle  
    def move(self):
        return "Sailing on water"
```

**🏗️ Composition Benefits:**
1. **Flexibility** - Swap components easily (different engines, payment methods)
2. **Reusability** - Same Address class works for Employee, Customer, Company
3. **Independence** - Engine can exist without Car, Product without Order
4. **Less coupling** - Changes to Engine don't affect Car's other parts

**🎯 Real-world composition:** Order systems, GUI components, game objects, configuration systems, plugin architectures

---

## Encapsulation - Protecting Your Data Like a Vault

### The Problem - When Anyone Can Mess With Your Data
**Real-world meaning:** Like leaving your bank vault open - anyone can take or corrupt your money.

```python
# Dangerous - no protection
class BankAccount_Unsafe:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Anyone can change this!

account = BankAccount_Unsafe("John", 1000)
# Disaster waiting to happen:
account.balance = -5000      # Negative balance?!
account.balance = "hacked"   # String balance?!
```

### The Solution - Controlled Access with Properties
**Real-world meaning:** Like a bank teller - you can't directly touch the money, but you can make safe transactions.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected with _
        self._pin = 1234        # Private-ish
    
    @property
    def balance(self):  # Getter - controlled way to see balance
        return f"${self._balance:.2f}"
    
    @balance.setter
    def balance(self, value):  # Setter - controlled way to change balance
        if isinstance(value, (int, float)) and value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance must be positive number")
    
    def withdraw(self, amount, pin):
        if pin != self._pin:
            return "Wrong PIN"
        if amount > self._balance:
            return "Insufficient funds"  
        self._balance -= amount
        return f"Withdrew ${amount}"

# Safe usage:
account = BankAccount("John", 1000)
print(account.balance)      # $1000.00 (controlled access)
account.balance = 1500      # Uses setter validation
# account.balance = -100    # ERROR - setter prevents this!
```

### Real Example - User Authentication System
```python
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self._password_hash = self._hash_password(password)  # Never store plain password
        self._login_attempts = 0
        self._is_locked = False
    
    @property
    def is_locked(self):  # Read-only property
        return self._is_locked
    
    def login(self, password):
        if self._is_locked:
            return "Account locked"
        
        if self._hash_password(password) == self._password_hash:
            self._login_attempts = 0
            return "Login successful"
        else:
            self._login_attempts += 1
            if self._login_attempts >= 3:
                self._is_locked = True
            return "Wrong password"
    
    def _hash_password(self, password):  # Private helper
        return f"hashed_{password}"

user = UserAccount("john", "secret123")
print(user.login("wrong"))     # Wrong password
print(user.is_locked)          # False (read-only access)
```

**🔒 Encapsulation Rules:**
- `public_var` = Anyone can access/modify
- `_protected_var` = "Don't touch unless you know what you're doing"
- `__private_var` = "Really private" (Python mangles the name)
- Use `@property` for controlled access

---

## Abstract Classes - The "You Must Implement This" Blueprint

### What Abstract Classes Do
**Real-world meaning:** Like a job description that says "You MUST have these skills" - you can't hire someone without them.

```python
from abc import ABC, abstractmethod

# Abstract class - cannot create instances directly
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def sleep(self):  # Concrete method - all animals sleep the same
        return f"{self.name} is sleeping"
    
    @abstractmethod  # Child classes MUST implement this
    def make_sound(self):
        pass  # No implementation - child provides it
    
    @abstractmethod
    def move(self):
        pass  # Child MUST implement this too

# Concrete classes - must implement ALL abstract methods  
class Dog(Animal):
    def make_sound(self):  # REQUIRED
        return f"{self.name} says Woof!"
    
    def move(self):  # REQUIRED
        return f"{self.name} runs on four legs"

class Bird(Animal):
    def make_sound(self):  # REQUIRED
        return f"{self.name} says Tweet!"
    
    def move(self):  # REQUIRED
        return f"{self.name} flies with wings"

# Usage:
# animal = Animal("Generic")  # ERROR! Can't create abstract class
dog = Dog("Buddy")            # Works - implements all required methods
print(dog.make_sound())       # Buddy says Woof!
print(dog.sleep())            # Buddy is sleeping (inherited method)
```

### Real Example - Payment Processing System
```python
class PaymentProcessor(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    def validate_amount(self):  # Shared method
        return self.amount > 0
    
    @abstractmethod
    def process_payment(self):  # Each provider different
        pass
    
    @abstractmethod  
    def send_receipt(self):     # Each has different format
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def process_payment(self):
        return f"Charged ${self.amount} to card ending in {self.card_number[-4:]}"
    
    def send_receipt(self):
        return f"Credit card receipt: ${self.amount}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process_payment(self):
        return f"PayPal charged ${self.amount} to {self.email}"
    
    def send_receipt(self):
        return f"PayPal receipt sent to {self.email}"

# Same interface, different implementations:
processors = [
    CreditCardProcessor(100, "1234567812345678"),
    PayPalProcessor(75, "user@example.com")
]

for processor in processors:
    print(processor.process_payment())  # Works the same way
    print(processor.send_receipt())
```

**🏗️ Why Use Abstract Classes:**
1. **Enforce contracts** - Child classes MUST implement required methods
2. **Common interface** - Different classes can be used interchangeably  
3. **Shared code** - Common methods defined once
4. **Prevent mistakes** - Can't create incomplete classes

---

## Magic Methods (Dunder Methods) - Make Your Objects Behave Like Built-ins

### What Magic Methods Do
**Real-world meaning:** Magic methods let your custom objects work with Python's built-in operations like `print()`, `len()`, `+`, `==`, etc.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):  # What print() shows users
        return f"{self.owner}'s account: ${self.balance:.2f}"
    
    def __repr__(self):  # What developers see for debugging  
        return f"BankAccount('{self.owner}', {self.balance})"
    
    def __len__(self):  # What len() returns
        return len(str(int(self.balance)))  # Number of digits in balance
    
    def __add__(self, other):  # What + operator does
        if isinstance(other, BankAccount):
            # Combine two accounts
            new_owner = f"{self.owner} & {other.owner}"
            new_balance = self.balance + other.balance
            return BankAccount(new_owner, new_balance)
        else:
            # Add money to account
            return BankAccount(self.owner, self.balance + other)
    
    def __eq__(self, other):  # What == operator does
        return (self.owner == other.owner and 
                self.balance == other.balance)

# Real usage - your objects work like built-in types:
account1 = BankAccount("John", 1000.50)
account2 = BankAccount("Sarah", 2500.75)

print(account1)           # John's account: $1000.50 (uses __str__)
print(repr(account1))     # BankAccount('John', 1000.5) (uses __repr__)
print(len(account1))      # 4 (uses __len__ - 1000 has 4 digits)

# Magic operators:
joint_account = account1 + account2  # Uses __add__
account3 = account1 + 500           # Also uses __add__
print(joint_account)                # John & Sarah's account: $3501.25

# Magic comparisons:  
account4 = BankAccount("John", 1000.50)
print(account1 == account4)         # True (uses __eq__)
```

### Most Useful Magic Methods

| Method | Purpose | Example Usage |
|--------|---------|---------------|
| `__init__` | Constructor | `User("john@example.com")` |
| `__str__` | User-friendly display | `print(user)` |
| `__repr__` | Developer debug info | `repr(user)` in debugger |
| `__len__` | Length/size | `len(shopping_cart)` |
| `__add__` | Addition operator | `cart1 + cart2` |
| `__eq__` | Equality comparison | `user1 == user2` |
| `__lt__` | Less than comparison | `account1 < account2` |
| `__getitem__` | Index access | `playlist[0]` |

### Real Example - Shopping Cart
```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def __str__(self):  # User sees this
        total = sum(item["price"] for item in self.items)
        return f"Cart with {len(self.items)} items, Total: ${total:.2f}"
    
    def __len__(self):  # len(cart) returns item count
        return len(self.items)
    
    def __add__(self, other_cart):  # Combine carts with +
        new_cart = ShoppingCart()
        new_cart.items = self.items + other_cart.items
        return new_cart
    
    def __getitem__(self, index):  # Access items with cart[0]
        return self.items[index]

# Usage like built-in types:
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)

print(cart)           # Cart with 2 items, Total: $1029.98
print(len(cart))      # 2
print(cart[0])        # {"item": "Laptop", "price": 999.99}

cart2 = ShoppingCart()
cart2.add_item("Keyboard", 79.99)
combined = cart + cart2  # Magic!
print(len(combined))     # 3
```

**🔥 Pro tip:** Magic methods make your custom objects feel like Python built-ins - users can use `print()`, `len()`, `+`, `==` naturally!

---

## Properties & Decorators - Adding Superpowers to Functions and Attributes

### Properties - Making Attributes Smart
**Real-world meaning:** Like having a smart doorbell that can see who's there and decide whether to let them in.

```python
# Problem - when attributes get out of sync
class Employee_Problem:
    def __init__(self, first, last):
        self.first = first
        self.last = last  
        self.email = f"{first}.{last}@company.com"  # Static - won't update!

emp = Employee_Problem("John", "Doe")
emp.first = "Jane"  # Changed name but...
print(emp.email)    # Still john.doe@company.com - out of sync!

# Solution - dynamic properties
class Employee_Fixed:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):  # Calculated every time it's accessed
        return f"{self.first}.{self.last}@company.com"
    
    @property 
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter  # Allow setting full_name as if it's an attribute
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp = Employee_Fixed("John", "Doe")
print(emp.email)        # john.doe@company.com
emp.first = "Jane"      # Change first name
print(emp.email)        # jane.doe@company.com - auto-updated!

# Set full name like an attribute
emp.full_name = "Mike Smith"
print(emp.email)        # mike.smith@company.com
```

### Decorators - Wrapping Functions with Extra Powers
**Real-world meaning:** Like adding security cameras, timers, or logging to a room without changing the room itself.

```python
import time
import functools

# Basic decorator - adds functionality before/after function
def timer_decorator(func):
    @functools.wraps(func)  # Preserves original function info
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_calculation():
    time.sleep(1)  # Simulate slow work
    return "Calculation complete"

result = slow_calculation()  # Automatically timed!
# Output: slow_calculation took 1.0045 seconds

# Real-world example - logging decorator
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
# Output: 
# Calling add_numbers with args: (5, 3)
# add_numbers returned: 8

# Authentication decorator (web apps)
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_logged_in = True  # Check session/token in real app
        if not user_logged_in:
            return "Access denied - please login"
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_profile():
    return "User profile: John Doe"

@require_auth  
def delete_account():
    return "Account deleted"

print(view_profile())    # User profile: John Doe
print(delete_account())  # Account deleted

# Decorator with parameters - retry failed operations
def retry(max_attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise e  # Give up after max attempts
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_api_call():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("API temporarily down")
    return "API call successful!"

# Multiple decorators - they stack bottom to top
@timer_decorator
@log_calls  
def complex_task(x, y):
    time.sleep(0.1)
    return x * y

result = complex_task(5, 3)
# Logs the call AND times it
```

### Real-World Decorator Examples
```python
# Caching decorator - save expensive calculations
from functools import lru_cache

@lru_cache(maxsize=100)  # Built-in caching decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))  # Fast! Results cached

# Rate limiting decorator
def rate_limit(calls_per_minute):
    def decorator(func):
        calls = []
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [call_time for call_time in calls if now - call_time < 60]
            if len(calls) >= calls_per_minute:
                return "Rate limit exceeded"
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_minute=5)
def send_email():
    return "Email sent"
```

**🚀 Where You See Decorators:**
- **Flask/Django:** `@app.route("/users")`, `@login_required`
- **Testing:** `@pytest.fixture`, `@unittest.mock.patch`  
- **Caching:** `@lru_cache`, `@cached_property`
- **Validation:** `@property`, `@staticmethod`, `@classmethod`

---

## String Operations - Your Text Processing Toolkit

### Real-World String Scenarios

```python
# Real data you'd work with:
user_input = "  PrAtEeK@ExAmPlE.cOm  "
api_response = "user_id:12345,status:active,role:admin"
log_message = "ERROR: Failed to connect to database on 2024-05-01"

# 1. Cleaning user input (very common!)
email = user_input.strip().lower()  # "prateek@example.com" 
print(f"Cleaned email: {email}")

# 2. Processing API responses
data_parts = api_response.split(',')  # ['user_id:12345', 'status:active', 'role:admin']
user_data = {}
for part in data_parts:
    key, value = part.split(':')
    user_data[key] = value
# Result: {'user_id': '12345', 'status': 'active', 'role': 'admin'}

# 3. Log analysis (real DevOps task)
if "ERROR" in log_message:
    error_date = log_message.split(" on ")[1]  # "2024-05-01"
    print(f"Error occurred on: {error_date}")

# 4. Building URLs and messages
base_url = "https://api.myapp.com"  
user_id = 12345
api_endpoint = f"{base_url}/users/{user_id}/profile"  # String interpolation
# Result: "https://api.myapp.com/users/12345/profile"

# 5. Validating input (real form processing)
def is_valid_username(username):
    return (len(username) >= 3 and 
            username.isalnum() and  # Only letters/numbers
            not username.isdigit())  # Not just numbers

print(is_valid_username("john123"))   # True
print(is_valid_username("123"))      # False
print(is_valid_username("jo"))       # False

# 6. Processing file names
filename = "user_report_2024_05_01.csv"
name_parts = filename.split('.')
file_extension = name_parts[-1]  # "csv"
base_name = filename.replace(f".{file_extension}", "")  # "user_report_2024_05_01"

# 7. Dynamic message generation (real notifications)  
user_name = "John"
order_count = 5
total_amount = 299.99
message = f"""
Hi {user_name}!

Your {order_count} items totaling ${total_amount:.2f} 
have been shipped. Track at: mystore.com/track

Thanks for shopping with us!
""".strip()
```

**💫 Real-world truth:** 80% of programming involves cleaning, splitting, joining, and formatting text data!

---

## File Operations - Your Data Persistence Toolkit

### Real-World File Scenarios

```python
from pathlib import Path
import json

# Real scenario 1: Processing log files (DevOps daily task)
log_file = Path("app.log")
error_count = 0

with open(log_file, 'r') as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
            print(f"Found error: {line.strip()}")

print(f"Total errors found: {error_count}")

# Real scenario 2: Saving user data (every app does this)
user_data = {
    "user_id": 12345,
    "email": "john@example.com", 
    "preferences": {"theme": "dark", "notifications": True}
}

# Save as JSON (most common format for APIs)
with open("user_profile.json", 'w') as file:
    json.dump(user_data, file, indent=2)

# Read it back later
with open("user_profile.json", 'r') as file:
    loaded_data = json.load(file)
    print(f"User email: {loaded_data['email']}")

# Real scenario 3: Processing CSV data (data science daily bread)
sales_data = [
    "Date,Product,Amount",
    "2024-05-01,Laptop,999.99", 
    "2024-05-01,Mouse,29.99",
    "2024-05-02,Keyboard,79.99"
]

# Write CSV
with open("sales.csv", 'w') as file:
    for line in sales_data:
        file.write(line + "\n")

# Process CSV  
total_sales = 0
with open("sales.csv", 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip header
        parts = line.strip().split(',')
        amount = float(parts[2])
        total_sales += amount

print(f"Total sales: ${total_sales:.2f}")

# Real scenario 4: Configuration files (every app needs settings)
config = {
    "database_url": "localhost:5432",
    "debug_mode": True,
    "max_connections": 100
}

# Save config
with open("app_config.json", 'w') as file:
    json.dump(config, file, indent=2)

# Real scenario 5: Appending to activity logs (tracking user actions)  
def log_user_activity(user_id, action):
    timestamp = "2024-05-01 10:30:00"  # In real app, use datetime.now()
    log_entry = f"{timestamp} - User {user_id}: {action}\n"
    
    with open("activity.log", 'a') as file:  # Append mode - doesn't overwrite
        file.write(log_entry)

log_user_activity(12345, "logged in")
log_user_activity(12345, "viewed profile")
log_user_activity(12345, "updated settings")
```

**🛡️ Real-world rule:** 
- Use `'r'` to read data (logs, configs, user files)
- Use `'w'` to save new data (overwrites - be careful!)  
- Use `'a'` to add to existing data (logs, activity tracking)
- Always use `with open()` - Python automatically closes the file even if your code crashes!

---

## 🎯 The Big Picture - What You Actually Use in Real Jobs

### What You'll Do Daily as a Developer:

1. **Variables & Logic** → Store user data, check permissions, handle business rules
2. **Functions** → Process payments, send emails, validate forms, call APIs
3. **Classes** → Model users, orders, products, database records
4. **Inheritance** → User roles (Admin extends User), Product types (Digital extends Product)
5. **Composition** → Build complex systems (Order has Items, Car has Engine)
6. **Encapsulation** → Protect sensitive data (passwords, balances, API keys)
7. **Abstract Classes** → Define contracts (PaymentProcessor, DatabaseClient)
8. **Properties** → Smart attributes (auto-updating emails, calculated values)
9. **Decorators** → Add features (logging, timing, authentication, caching)
10. **Strings** → Clean input, build URLs, format messages, parse API responses
11. **Files** → Read configs, process logs, save user data, generate reports

### Mental Models That Work in Real Code:

- **Classes** = Cookie cutters for real things (User, Order, Product templates)
- **Objects** = Cookies made from cutters (John's account, Order #12345)
- **Inheritance** = Job roles (Developer IS an Employee + coding skills)
- **Composition** = Building with Lego blocks (Car HAS Engine + Wheels + GPS)
- **Encapsulation** = Bank vault (controlled access to sensitive data)
- **Abstract Classes** = Job requirements ("You MUST implement these methods")
- **Properties** = Smart doorbell (decides what to show/allow based on rules)
- **Decorators** = Security cameras (add features without changing the room)

### The Rules That Save Your Career:

1. **`self.attribute`** = Permanent data that survives (user's email, account balance)
2. **Inheritance** = "IS-A" relationship (Developer IS an Employee)
3. **Composition** = "HAS-A" relationship (Order HAS Items, Car HAS Engine)
4. **Encapsulation** = Use `_private` and `@property` to control access
5. **Abstract classes** = Force children to implement required methods
6. **Properties** = Make attributes smart and self-updating
7. **Decorators** = Add functionality without changing original code
8. **F-strings** = Fast, readable text formatting (`f"Hello {name}"`)
9. **Always use `with open()`** = Files get closed even if code crashes

### Real Project Ideas to Practice:

- **User Management System** → Classes, inheritance, encapsulation, properties
- **Payment Gateway** → Abstract classes, multiple processors, error handling
- **Social Media App** → User roles, decorators (auth, logging), file uploads
- **API Framework** → Abstract base classes, decorators, property validation
- **Game Engine** → Inheritance (Player, Enemy, Item), abstract GameObjects
- **Configuration Manager** → Properties, encapsulation, file I/O, validation

---

*🚀 These concepts power every Python app - from simple scripts to Netflix's backend. Master these patterns and you can build anything!*