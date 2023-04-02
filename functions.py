# function in python
# it is block of code that performs specfic tasks whenever its is called i
# there are two types of functions
#1. built in functions
# built in functions are those functions which are olready defined by code of python
# 2.user defined functions

print("This is Without functions used")
a=int(input("Enter the First Number = "))
b=int(input("Enter the Second Number = "))
gmean=a*b/(a+b)

print("The Geometric Mean is :- ",gmean)
print("This is after using the function")
def calulate(a,b):
    mean=a*b/(a+b)
    print("The Geometric Mean is :- ",mean)

calulate(a,b)
# this user defined function in which user make it is own function
def compare(a,b):
    if(a>b):
        print("A is Greater than B ")
    else:
     print("A is Less than B ")
    
compare(a,b)

#default arguments it is arguments in which function assumses default arguments values for the code.
print("Default arguments")
def add(c=6, d=8):
    add=c+d
    print("The Sum of Two Number:-",add)
    
add(4)
