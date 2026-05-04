#every character in python belongs to class unlike other languages like java where every character is a diff data type
#string is immutable in python

#split method - splits the string into a list of substrings based on the delimiter
#delimiter is the character that is used to split the string
#delimiter is optional and if not provided then the string is split at every whitespace
#delimiter is a string and not a character

# --- THE TRUTH ABOUT SPLIT ---
string = "Python,Java,C++,Ruby,JavaScript"

# 1. No maxsplit: Cuts EVERYWHERE it finds a comma
print(string.split(",")) 
# Output: ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']

# 2. maxsplit=1: Make 1 cut at the first comma. 
# Everything after that stays together in the second piece.
print(string.split(",", 1)) 
# Output: ['Python', 'Java,C++,Ruby,JavaScript']

# 3. maxsplit=2: Make 2 cuts at the first two commas.
print(string.split(",", 2)) 
# Output: ['Python', 'Java', 'C++,Ruby,JavaScript']

#tuples
#tuples are immutable and ordered and can contain different data types
#tuples are defined using parentheses
#tuples are indexed and can be sliced
#tuples are iterable
#tuples are hashable and can be used as keys in dictionaries
#tuples are immutable and can be used as keys in dictionaries
#tuples are immutable and can be used as keys in dictionaries

tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[0])

#ßtuple[0] = 10 #this will raise an error because tuples are immutable
print(tuple)


#try except
try:
    tuple[0] = 10
except TypeError:
    print("Tuples are immutable")

#try except else finally
try:
    tuple[0] = 10
except TypeError:
    print("Tuples are immutable")
else:
    print("Tuple is immutable")
finally:
    print("Finally block")

#-----------------------------------------------------------#

#input method - takes input from the user

result = input("Hey, give us a number:")
print(f"The result is: {result})")
#-----------------------------------------------------------
chr(65) #- returns A, chr(66) returns B, chr(67) returns C and so on
char(97) #- returns a, char(98) returns b, char(99) returns c and so on
#-----------------------------------------------------------
#ord method - returns the ASCII value of the character
ord('A') #- returns 65, ord('B') returns 66, ord('C') returns 67 and so on
ord('a') #- returns 97, ord('b') returns 98, ord('c') returns 99 and so on
