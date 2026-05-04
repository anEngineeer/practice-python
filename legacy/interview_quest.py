import requests
import time
import logging

logging.basicConfig(level=logging.INFO) 

# def create_user(url, payload):
#    max_retries = 3 
#    for attempt in range (max_retries+1):
#         try:
#             response = requests.post("url", "payload", timeout = 5)

#             if response.status_code==201:
#                 response = response.json()
#                 if "id" in response and "name" in response:
#                     return response
#                 else:
#                     return None
#             elif 600>response.status_code >=500:
#                 logging.error("server error")

#         except:
#             logging.error(f"Client Error {response.status_code}: {response.text}")
#             break
#-------------------------------------------------------------------------------------#

order_data_response = {
  "orders": [
    {"id": 101, "amount": 250.00, "status": "completed"},
    {"id": 102, "amount": 450.00, "status": "pending"},
    {"id": 101, "amount": 250.00, "status": "completed"},
    {"id": 103, "amount": 150.00, "status": "completed"},
    {"id": 104, "amount": 450.00, "status": "completed"},
    {"id": 105, "amount": 600.00, "status": "completed"},
    {"id": 103, "amount": 150.00, "status": "completed"}
  ]
}

def analyze_orders():
    total_sale = 0
    unique_amounts = set()
    for order in order_data_response["orders"]:
            status = order["status"]
            amount = order["amount"]

            if status == "completed":
                total_sale = total_sale+amount

            if amount not in unique_amounts:
                unique_amounts.add(amount)
    
    sorted_list = sorted(unique_amounts,reverse=True)
    top_2 = sorted_list[0:2]

    print(f"Total sale: {total_sale}")
    print(f"unique_amounts:{unique_amounts}")
    print(f"Top 2 amounts: {top_2}")


analyze_orders()

#------------------------------------#



response_data = {
  "users": [
    {"id": 1, "email": "test@example.com"},
    {"id": 2, "email": "user@domain.com"},
    {"id": 3, "email": "test@example.com"} 
  ]
}

def verify_users(response_data):
    if "users" not in response_data or not isinstance(response_data["users"], list):
        raise Exception("invalid format, 'users key missing or is not a list")
    
    for user in response_data["users"]:
        if "id" not in user or "email" not in user:
            raise Exception(f"id or email not present in data {user}")
        
        user_id = user["id"]
        user_email = user["email"]

        if not isinstance(user_id, int):
            raise Exception(f"id is not integer")
        
        if "@" not in user_email or "." not in user_email:
            raise Exception(f"Format Error: '{user_email}' is not a valid email address")

    return None

verify_users(response_data)

#------------------------------------#

given_string = "a2b3c1d2"


def solve_expand(data):
    expanded_string = ""
    last_letter = ""
    for char in given_string:
        if char.isalpha():
            last_letter = char
        elif char.isdigit():
            expanded_string = expanded_string+last_letter*int(char)
        
    print(expanded_string)

solve_expand(given_string)

#------------------------------------#
def get_frequency(input):
    output={}
    for char in input:
        if char not in output:
            output[char] = 1
        else:
            output[char]+= 1
    return output

user_input = "apple"

print(get_frequency(user_input))
#------------------------------------#

def first_non_repeating_char(input):
    final_chars={}
    for char in input:
        if char not in final_chars:
                final_chars[char] = 1
        else:
            final_chars[char] += 1
    for char in input:
        if final_chars[char] == 1:
                return char
    
    

word = "banana"

print(first_non_repeating_char(word))

#------------------------------------#
#prime_numbers

def is_prime(num):
    if num<=1:
        raise Exception("num below valid range")
    for i in range (2,num):
        if num%i==0:
            return False
    
    return True

n = 7

print(is_prime(n))

#------------------------------------#

num = [10, 20, 4, 45, 99] #output should be 45
def find_second_largest(nums):
    # Initialize both to the smallest possible value
    first = float('-inf')
    second = float('-inf')

    for n in nums:
        if n > first:
            # New largest found! 
            # The old 'first' becomes the 'second'
            second = first
            first = n
        elif n > second and n != first:
            # Not bigger than 'first', but bigger than 'second'
            second = n

    return second

# Testing with your example
my_list = [10, 20, 4, 45, 99]
print(find_second_largest(my_list)) # Output: 45

#------------------------------------#

#reverse an array

def reverse_array(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        arr[left], arr[right] = arr[right], arr[left]

        left +=1
        right -=1

    return arr


print(reverse_array([10,20,30,40,50,60,20]))












        
