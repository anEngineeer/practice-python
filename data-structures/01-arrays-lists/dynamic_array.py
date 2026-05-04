"""
Dynamic Array Implementation

A dynamic array (similar to Python's list) that can grow and shrink as needed.
This implementation shows how Python lists work under the hood.
"""

a = [1,2,3]

#Appending - insert an element at the end of the array - on Averag O(1)
a.append(4)
print(a) #prints [1,2,3,4]

#Pop - Delete an element from the end of the array - on Average O(1)
a.pop()
print(a) #prints [1,2,3]

#Insert - Insert an element at a specific index - on Average O(n)
a.insert(2, 4) #first zero means index and second zero means the element to be inserted
print(a) #prints [1,2,4,3]

#modify - modify an element at a specific index - on Average O(1)
a[2] = 5
print(a) #prints [1,2,5,3]

#delete - delete an element at a specific index - on Average O(n)
del a[2]
print(a) #prints [1,2,3]

#concatenate - concatenate two arrays - on Average O(n)
a = a + [4,5,6]
print(a) #prints [1,2,3,4,5,6]

#access - access an element at a specific index - on Average O(1)
print(a[2]) #prints 5

#length - get the length of the array - on Average O(1)
print(len(a)) #prints 6


#iterate - iterate through the array - on Average O(n)
for i in a:
    print(i) #prints 1,2,5,3,4,5,6

#reverse - reverse the array - on Average O(n)
print(a[::-1]) #prints [6,5,4,3,2,1]

#checking if an element is in the array - on Average O(n)
print(5 in a) #prints True
