def add(a,b):
    return a+b
print(add(5,6)) #prints 11


# def minus(a,b,c):
#     return a-b-c

# print(minus(10,5)) #this will fail because we did not pass the third parameter ; TypeError: minus() missing 1 required positional argument: 'c'

def doit(a,b,c=4):
    return a+b+c

print(doit(5,6)) #prints 11, here c is not passed so it takes the default value of c which is 4 
print(doit(5,6,7)) #prints 18 , as c is passed as 7 so it overrides the default value of c which is 4

def doit(a,b=5,c=4):
    return a+b+c

print(doit(5)) #prints 14, here b and c are not passed so it takes the default value of b which is 5 and c which is 4
print(doit(5,6)) #prints 15, here c is not passed so it takes the default value of c which is 4
print(doit(5,6,7)) #prints 18, as c is passed as 7 so it overrides the default value of c which is 4

def doit(a,b=5,c=4):
    return a+b+c

print(doit(5,c=7)) #prints 16, here c is passed as 7 so it overrides the default value of c which is 4
print(doit(5,b=6,c=7)) #prints 18, as b is passed as 6 so it overrides the default value of b which is 5
print(doit(a=5)) #prints 14 , here a becoimes 5 and b and c are not passed so it takes the default value of b which is 5 and c which is 4


def doit(a,b=5,c=4):
    return a+b+c

print(doit(10,a=2,c=7)) #TypeError: doit() got multiple values for argument 'a' , because a is passed as 2 and then again as 10 so it is ambiguous