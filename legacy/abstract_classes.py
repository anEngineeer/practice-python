#abstract classes - blueprints that force child classes to implement certain methods

from abc import ABC, abstractmethod #ABC is Abstract Base Class and abstractmethod is a decorator that forces child classes to implement certain methods

#abstract class - cannot be instantiated directly
class Animal(ABC):  #inherit from ABC (Abstract Base Class)
    def __init__(self, name):
        self.name = name
    
    def sleep(self):  #concrete method - all animals sleep the same way
        print(f"{self.name} is sleeping")
    
    @abstractmethod  #forces child classes to implement this
    def make_sound(self):
        pass  #no implementation - child MUST provide one
    
    @abstractmethod
    def move(self):
        pass  #child MUST implement this too

#concrete classes - must implement ALL abstract methods
class Dog(Animal):
    def make_sound(self):  #REQUIRED implementation
        return f"{self.name} says Woof!"
    
    def move(self):  #REQUIRED implementation  
        return f"{self.name} runs on four legs"

class Bird(Animal):
    def make_sound(self):  #REQUIRED implementation
        return f"{self.name} says Tweet!"
    
    def move(self):  #REQUIRED implementation
        return f"{self.name} flies with wings"

#usage - cannot create Animal directly
# animal = Animal("Generic")  # ERROR! Can't instantiate abstract class

#but can create concrete animals
dog = Dog("Buddy")
bird = Bird("Tweety")

print(dog.make_sound())  #Buddy says Woof!
print(dog.move())        #Buddy runs on four legs  
dog.sleep()              #Buddy is sleeping (inherited method)

print(bird.make_sound()) #Tweety says Tweet!
print(bird.move())       #Tweety flies with wings

###############################################################

#real-world example - payment processing system
class PaymentProcessor(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    def validate_amount(self):  #concrete method - same for all
        return self.amount > 0 and isinstance(self.amount, (int, float))
    
    @abstractmethod
    def process_payment(self):  #each provider implements differently
        pass
    
    @abstractmethod  
    def send_receipt(self):  #each provider has different receipt format
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def process_payment(self):
        if self.validate_amount():
            return f"Charged ${self.amount} to card ending in {self.card_number[-4:]}"
        return "Invalid amount"
    
    def send_receipt(self):
        return f"Credit card receipt: ${self.amount} charged"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process_payment(self):
        if self.validate_amount():
            return f"PayPal charged ${self.amount} to {self.email}"
        return "Invalid amount"
    
    def send_receipt(self):
        return f"PayPal receipt sent to {self.email} for ${self.amount}"

class CryptoProcessor(PaymentProcessor):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address
    
    def process_payment(self):
        if self.validate_amount():
            return f"Crypto payment of ${self.amount} sent to {self.wallet_address[:8]}..."
        return "Invalid amount"
    
    def send_receipt(self):
        return f"Blockchain transaction confirmed: ${self.amount}"

#usage - same interface, different implementations
processors = [
    CreditCardProcessor(100, "1234567812345678"),
    PayPalProcessor(75, "user@example.com"),  
    CryptoProcessor(200, "1A2B3C4D5E6F7G8H9I0J")
]

for processor in processors:
    print(processor.process_payment())
    print(processor.send_receipt())
    print("---")

###############################################################

#real-world example - database connections
class Database(ABC):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def get_connection_string(self):  #common method
        return f"{self.host}:{self.port}"
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    @abstractmethod
    def close_connection(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return f"Connected to MySQL at {self.get_connection_string()}"
    
    def execute_query(self, query):
        return f"MySQL executing: {query}"
    
    def close_connection(self):
        return "MySQL connection closed"

class PostgreSQLDatabase(Database):
    def connect(self):
        return f"Connected to PostgreSQL at {self.get_connection_string()}"
    
    def execute_query(self, query):
        return f"PostgreSQL executing: {query}"
    
    def close_connection(self):
        return "PostgreSQL connection closed"

#usage - same interface for different databases
def run_database_operations(db: Database):  #type hint - any Database
    print(db.connect())
    print(db.execute_query("SELECT * FROM users"))
    print(db.close_connection())

mysql_db = MySQLDatabase("localhost", 3306)
postgres_db = PostgreSQLDatabase("localhost", 5432)

run_database_operations(mysql_db)
print("---")
run_database_operations(postgres_db)

###############################################################

#why use abstract classes?
# 1. ENFORCE CONTRACTS - child classes MUST implement required methods
# 2. COMMON INTERFACE - different classes can be used interchangeably  
# 3. SHARED CODE - common methods defined once in parent
# 4. PREVENT MISTAKES - can't accidentally create incomplete classes
# 5. DOCUMENTATION - clearly shows what methods are required

#real-world usage:
# - Django models inherit from abstract Model class
# - Flask view classes inherit from abstract View  
# - Game engines: GameObject -> Player, Enemy, Item
# - GUI frameworks: Widget -> Button, TextBox, Label
# - API clients: BaseClient -> RESTClient, GraphQLClient