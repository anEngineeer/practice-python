#decorators in python - add functionality to existing functions without modifying them

import functools
import time

#basic decorator concept - function that takes another function and extends it
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()  #call the original function
        print("Something after the function")
    return wrapper

def say_hello():
    print("Hello!")

#using decorator manually
decorated_hello = my_decorator(say_hello)
decorated_hello()

print("------------------------------")

#using @ syntax - cleaner way
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()  #automatically decorated

###############################################################

#real-world example - timing functions (performance monitoring)
def timer_decorator(func):
    @functools.wraps(func)  #preserves original function info
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  #call original with any arguments
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)  #simulate slow operation
    return "Done processing"

result = slow_function()
print(result)

###############################################################

#real-world example - logging decorator (debugging/monitoring)
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    return a + b

@log_calls  
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result1 = add_numbers(5, 3)
result2 = greet_user("John", greeting="Hi")

###############################################################

#real-world example - authentication decorator (web apps)
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #simulate checking if user is logged in
        user_logged_in = True  #in real app, check session/token
        if not user_logged_in:
            return "Access denied - please login"
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_profile():
    return "User profile: John Doe, Premium Member"

@require_auth
def delete_account():
    return "Account deleted successfully"

print(view_profile())
print(delete_account())

###############################################################

#decorator with parameters - more flexibility  
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
                        raise e  #re-raise if all attempts failed
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_api_call():
    import random
    if random.random() < 0.7:  #70% chance of failure
        raise Exception("API temporarily unavailable")
    return "API call successful!"

try:
    result = unstable_api_call()
    print(result)
except Exception as e:
    print(f"All attempts failed: {e}")

###############################################################

#multiple decorators - they stack from bottom to top
@timer_decorator
@log_calls
def complex_calculation(x, y):
    time.sleep(0.1)  #simulate complex work
    return x * y + (x - y)

result = complex_calculation(10, 3)

###############################################################

#class-based decorator - when you need state
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi there!")

say_hi()  #Call #1
say_hi()  #Call #2  
say_hi()  #Call #3

print(f"Total calls: {say_hi.count}")

###############################################################

#real-world examples where decorators are used:
# 1. Flask web framework: @app.route("/users") 
# 2. Django: @login_required, @csrf_exempt
# 3. Testing: @pytest.fixture, @unittest.mock.patch
# 4. Caching: @functools.lru_cache
# 5. Property validation: @property, @setter
# 6. API rate limiting: @rate_limit(calls_per_minute=100)