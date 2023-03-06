# User Input:-
# input function is used to take input from the user in from of string or character and return a string
# for example:-
a=input("Enter your Name :-")
print("My name is " ,a)
# but if you want to use another datatype, you can use using the typecasting 
b=int(input("Enter your Sap ID :- "))
print("Your Sap ID  is = ",b)
# if you don't use type Casting then it will  Contcattion to integer as a string
# for example:-
#c=input("Enter your Number :-")
#d=input("Enter your Number  :-")
#print(c+d)# it concatenates the numbers as strings
# but if  you want to add two numbers then you want to use typecasting
# like this:-
c=int(input("Enter your One Number :- "))
d=int(input("Enter your Second Number :- "))
sum=c+d
print("Sum of the two numbers = " , sum)