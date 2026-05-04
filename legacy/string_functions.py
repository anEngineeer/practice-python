#string functions in python - all widely used ones with examples

#basic string
text = "Hello World Python Programming"
name = "prateek mishra"
sentence = "  this has spaces  "
email = "prateek@example.com"

print("Original:", text)
print()

###############################################################

#1. len() - get length of string
print("1. LENGTH:")
print(len(text))  #29
print(len(name))  #14
print()

###############################################################

#2. upper(), lower(), title(), capitalize()
print("2. CASE CONVERSION:")
print(text.upper())  #HELLO WORLD PYTHON PROGRAMMING
print(text.lower())  #hello world python programming
print(name.title())  #Prateek Mishra (first letter of each word capitalized)
print(name.capitalize())  #Prateek mishra (only first letter capitalized)
print()

###############################################################

#3. strip(), lstrip(), rstrip() - remove whitespace
print("3. REMOVING SPACES:")
print(f"'{sentence}'")  #'  this has spaces  '
print(f"'{sentence.strip()}'")  #'this has spaces' (both sides)
print(f"'{sentence.lstrip()}'")  #'this has spaces  ' (left side only)
print(f"'{sentence.rstrip()}'")  #'  this has spaces' (right side only)
print()

###############################################################

#4. split() - convert string to list
print("4. SPLITTING STRINGS:")
words = text.split()  #splits by spaces (default)
print(words)  #['Hello', 'World', 'Python', 'Programming']

parts = email.split("@")  #split by specific character
print(parts)  #['prateek', 'example.com']

csv_data = "apple,banana,orange"
fruits = csv_data.split(",")
print(fruits)  #['apple', 'banana', 'orange']
print()

###############################################################

#5. join() - convert list to string
print("5. JOINING LISTS:")
word_list = ['Hello', 'World', 'Python']
joined = " ".join(word_list)  #join with spaces
print(joined)  #Hello World Python

joined_comma = ",".join(word_list)  #join with commas
print(joined_comma)  #Hello,World,Python
print()

###############################################################

#6. replace() - replace parts of string
print("6. REPLACING TEXT:")
new_text = text.replace("Python", "Java")
print(new_text)  #Hello World Java Programming

remove_spaces = name.replace(" ", "")
print(remove_spaces)  #prateekmishra
print()

###############################################################

#7. find(), index() - find position of substring
print("7. FINDING TEXT:")
pos1 = text.find("World")  #returns position or -1 if not found
print(f"'World' found at position: {pos1}")  #6

pos2 = text.find("xyz")  #-1 because not found
print(f"'xyz' found at position: {pos2}")  #-1

#index() same as find() but raises error if not found
pos3 = text.index("Python")
print(f"'Python' found at position: {pos3}")  #12
print()

###############################################################

#8. startswith(), endswith() - check beginning/end
print("8. CHECKING START/END:")
print(text.startswith("Hello"))  #True
print(text.startswith("World"))  #False
print(text.endswith("ing"))  #True
print(email.endswith(".com"))  #True
print()

###############################################################

#9. count() - count occurrences
print("9. COUNTING:")
test_string = "hello hello world hello"
print(test_string.count("hello"))  #3
print(test_string.count("world"))  #1
print()

###############################################################

#10. isdigit(), isalpha(), isalnum() - check content type
print("10. CHECKING CONTENT TYPE:")
number_str = "12345"
letter_str = "abcde"
mixed_str = "abc123"
space_str = "hello world"

print(f"'{number_str}' is digit: {number_str.isdigit()}")  #True
print(f"'{letter_str}' is alpha: {letter_str.isalpha()}")  #True
print(f"'{mixed_str}' is alnum: {mixed_str.isalnum()}")  #True
print(f"'{space_str}' is alpha: {space_str.isalpha()}")  #False (has space)
print()

###############################################################

#11. slicing - extract parts of string
print("11. SLICING:")
word = "Programming"
print(word[0])  #P (first character)
print(word[-1])  #g (last character)
print(word[0:4])  #Prog (from index 0 to 3)
print(word[4:])  #ramming (from index 4 to end)
print(word[:4])  #Prog (from start to index 3)
print(word[::2])  #Pormmn (every 2nd character)
print(word[::-1])  #gnimmargorP (reverse)
print()

###############################################################

#12. format() and f-strings - string formatting
print("12. FORMATTING:")
name = "Prateek"
age = 25
score = 95.67

#old way - format()
message1 = "My name is {} and I am {} years old".format(name, age)
print(message1)

#new way - f-strings (preferred)
message2 = f"My name is {name} and I am {age} years old"
print(message2)

#formatting numbers
print(f"Score: {score:.1f}")  #95.7 (1 decimal place)
print(f"Score: {score:.0f}")  #96 (no decimal places)
print()

###############################################################

#13. in operator - check if substring exists
print("13. CHECKING IF TEXT EXISTS:")
print("Python" in text)  #True
print("Java" in text)  #False
print("@" in email)  #True
print()

###############################################################

#14. strip specific characters
print("14. STRIP SPECIFIC CHARACTERS:")
url = "https://www.example.com/"
clean_url = url.strip("https://").strip("/")  #can chain methods
print(clean_url)  #www.example.com

phone = "+++91-9876543210+++"
clean_phone = phone.strip("+")
print(clean_phone)  #91-9876543210
print()

###############################################################

#15. zfill() - pad with zeros
print("15. ZERO PADDING:")
number = "42"
padded = number.zfill(5)
print(padded)  #00042
print()

###############################################################

#bonus: useful string methods for validation
print("BONUS - VALIDATION METHODS:")
test_cases = ["Hello123", "HELLO", "hello", "Hello World", "123", "   "]

for test in test_cases:
    print(f"'{test}': upper={test.isupper()}, lower={test.islower()}, space={test.isspace()}")