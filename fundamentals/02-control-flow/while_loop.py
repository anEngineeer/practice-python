#While loop
grocery_list = ["apple", "banana", "cherry"]

j = len(grocery_list) - 1
print(j)

while j >= 0:
    grocery_list[j]
    j-=1 

    print(grocery_list[j])


items_list = ["wire", "screw", "nail", "bolt"]

i=0

while i < len(items_list):
    print(items_list[i])
    i+=1