#Append - Append a character to the end of the string - on Average O(1)
string = "Hello"
string.append("World")
print(string) #prints HelloWorld

#Insert - Insert a character at a specific index - on Average O(n)
string = "Hello"
string.insert(2, "World")
print(string) #prints HelloWorld

#Remove - Remove a character at a specific index - on Average O(n)
string = "Hello"
string.remove("World")
print(string) #prints Hello

#Concatenate - Concatenate two strings - on Average O(n)
string = "Hello"
string = string + "World"
print(string) #prints HelloWorld

#Access - Access a character at a specific index - on Average O(1)
string = "Hello"
print(string[2]) #prints l