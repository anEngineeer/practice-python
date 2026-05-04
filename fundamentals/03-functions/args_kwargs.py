"""
*args and **kwargs - Python's Flexible Function Parameters

These are your "wildcard" tools that allow functions to handle any number of inputs,
even if you didn't define them when you wrote the function.
"""


# 1. *args (Arguments as a Tuple)
# The * is the "unpacker" - it tells Python to collect extra positional arguments into a tuple

def add_all_scores(*args):
    """Add any number of scores together"""
    print(f"Received args: {args}")  # args is a TUPLE
    return sum(args)

# Examples
print("=== *args Examples ===")
print(add_all_scores(10, 20))         # Result: 30
print(add_all_scores(10, 20, 30, 40)) # Result: 100
print(add_all_scores(5))              # Result: 5
print()


# 2. **kwargs (Keyword Arguments as a Dictionary)  
# The ** tells Python to collect named arguments into a dictionary

def print_user_profile(**kwargs):
    """Print user profile information"""
    print(f"Received kwargs: {kwargs}")  # kwargs is a DICTIONARY
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Examples
print("=== **kwargs Examples ===")
print_user_profile(name="Prateek", role="Developer", city="Noida")
print()
print_user_profile(name="Alice", age=25, department="Engineering", salary=75000)
print()


# 3. Combining *args and **kwargs
def flexible_function(required_param, *args, **kwargs):
    """Function that accepts required, optional positional, and keyword arguments"""
    print(f"Required: {required_param}")
    print(f"Optional positional args: {args}")
    print(f"Optional keyword args: {kwargs}")

print("=== Combined *args and **kwargs ===")
flexible_function("must_have", 1, 2, 3, name="John", age=30)
print()


# 4. Real-world OOP Example: Future-proof classes
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        # Store any extra information for future use
        self.extra_info = kwargs
        
    def display_info(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")
        if self.extra_info:
            print("Additional info:")
            for key, value in self.extra_info.items():
                print(f"  {key}: {value}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language, *args, **kwargs):
        # Pass everything up to parent class - future-proof!
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language
        
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

print("=== OOP with *args and **kwargs ===")
# Even if we add new fields later, the class handles them gracefully
dev = Developer(
    "Prateek", 
    75000, 
    "Python", 
    location="Noida", 
    age=31, 
    years_experience=5,
    team="Backend"
)
dev.display_info()
print()


# 5. Unpacking arguments when calling functions
def greet(first_name, last_name, greeting="Hello"):
    return f"{greeting} {first_name} {last_name}!"

# Using * to unpack a list/tuple
names = ["John", "Doe"]
print("=== Unpacking with * ===")
print(greet(*names))  # Unpacks to: greet("John", "Doe")

# Using ** to unpack a dictionary
person_data = {"first_name": "Jane", "last_name": "Smith", "greeting": "Hi"}
print(greet(**person_data))  # Unpacks to: greet(first_name="Jane", last_name="Smith", greeting="Hi")
print()


# 6. Advanced: Decorator using *args and **kwargs
def timing_decorator(func):
    """A decorator that times function execution"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Pass through all arguments
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_calculation(n):
    """A slow calculation for demonstration"""
    total = 0
    for i in range(n):
        total += i * i
    return total

print("=== Decorator Example ===")
result = slow_calculation(100000)
print(f"Result: {result}")
print()


# Quick Reference Summary
print("=== Quick Reference ===")
print("*args:")
print("  - Collects extra positional arguments into a TUPLE")
print("  - Use when you don't know how many arguments will be passed")
print("  - Example: func(1, 2, 3) -> args = (1, 2, 3)")
print()
print("**kwargs:")
print("  - Collects extra keyword arguments into a DICTIONARY") 
print("  - Use when you want to handle optional named parameters")
print("  - Example: func(a=1, b=2) -> kwargs = {'a': 1, 'b': 2}")
print()
print("Order in function definition:")
print("  def func(required, *args, **kwargs):")
print()
print("Common use cases:")
print("  - Making decorators that work with any function")
print("  - Creating flexible APIs")
print("  - Building future-proof class hierarchies")
print("  - Wrapping functions while preserving their signature")