grocery_list = ["apple", "banana", "cherry"]

print(grocery_list)

grocery_list.append("orange")

print(grocery_list)

grocery_list.remove("banana")

print(grocery_list)

grocery_list.pop() #removes the last item from the list

print(grocery_list)

grocery_list.pop(0) #removes the first item from the list

print(grocery_list)

grocery_list.clear() #clears the list

print(grocery_list)


#looping through a list
item_list = ["wire", "screw", "nail", "bolt"]

for item in item_list:
    print(item) #prints each item in the list ; loops throught the each index of the list and then prints the item at that index


for i  in [0,1,2,3]:
    print(item_list[i]) #prints each item in the list ; loops throught the each index of the list and then prints the item at that index

#Range function
for i in range(4):
    print(item_list[i]) #prints each item in the list ; loops throught the each index of the list and then prints the item at that index

for i , item in enumerate(item_list):
    print(i, item) #prints the index and the item in the list


for i , item in enumerate(item_list, start=1):
    print(i, item) #prints the index and the item in the list starting from 1