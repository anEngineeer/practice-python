#functions in python - everything you need to know

import copy

#basic function - parameter vs argument
def our_print(s):  #s is parameter
    print(s)

our_print("Prateek")  #"Prateek" is argument

#scope - global vs local variable with same name
a = 8  #global variable

def add(b):
    a = 10  #local variable - does not change global a
    return a + b

print(add(2))  #prints 12 (uses local a=10)
print(a)  #still prints 8 (global a unchanged)

###############################################################

#default parameters and different ways to call functions
def show_two(s, a=10):
    print(s, a)

show_two("Prateek")  #using default value for a
show_two(s="Prateek", a=10)  #keyword arguments
show_two("Prateek", 10)  #positional arguments

###############################################################

#function changing caller's list - side effect
def append_4_to_list(lst):
    lst.append(4)  #this changes the original list

a = [1, 2, 3]
append_4_to_list(a)
print(a)  #prints [1, 2, 3, 4] - list got changed!

###############################################################

#is vs == - very important difference
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  #False - different objects in memory
print(a == b)  #True - same values

b = a  #now b points to same object as a
print(a is b)  #True - same object now
print(a is not b)  #False

###############################################################

#deepcopy - making completely separate copy
a = [1, 2, 3]
b = copy.deepcopy(a)
print(a is b)  #False - different objects
print(a == b)  #True - same values

b[0] = 99
print(a)  #[1, 2, 3] - a unchanged
print(b)  #[99, 2, 3] - only b changed

###############################################################

#when does caller's variable change? - the tricky part!

#case 1: function assigns new list to parameter - caller unchanged
def replace_list(x):
    print("before:", x is a_outer)  #True - same object
    x = [1, 2]  #x now points to NEW list
    print("after:", x is a_outer)  #False - different objects now

a_outer = [1, 2, 3]
replace_list(a_outer)
print(a_outer)  #still [1, 2, 3] - unchanged

###############################################################

#case 2: function mutates the list - caller changes!
def append_four(x):
    print("same object?", x is a_mut)  #True
    x.append(4)  #mutates same object
    print("still same object?", x is a_mut)  #still True

a_mut = [1, 2, 3]
append_four(a_mut)
print(a_mut)  #[1, 2, 3, 4] - got changed!

###############################################################

#case 3: with numbers (immutable) - caller never changes
def try_change_int(n):
    print("same object?", n is k)  #True for small numbers
    n = n + 1  #creates new int, n points to it
    print("n is now:", n)

k = 10
try_change_int(k)
print("k is still:", k)  #still 10

###############################################################

#case 4: x = x + [4] vs x += [4] - big difference!

#x = x + [4] creates NEW list
def concat_new_list(x):
    x = x + [4]  #new list created

a_plus = [1, 2, 3]
concat_new_list(a_plus)
print(a_plus)  #[1, 2, 3] - unchanged

#x += [4] modifies existing list
def iadd_list(x):
    x += [4]  #same as x.extend([4]) - mutates existing list

a_iadd = [1, 2, 3]
iadd_list(a_iadd)
print(a_iadd)  #[1, 2, 3, 4] - changed! this is the gotcha

###############################################################

#if you want to change caller's variable, return new value
def doubled_list(x):
    return [v * 2 for v in x]

nums = [1, 2, 3]
nums = doubled_list(nums)  #assign returned value back
print(nums)  #[2, 4, 6]