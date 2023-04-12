# tuples cant be changed 
# tuples are same as list in which you can enter data items of any types
num=(1,2,3,4,5)
print("This is my tuple",num)
print("Tuples at index of [0]",num[0])
a=int(input("Enter the element to find in tuples = "))
if a in num:
    print("Element is persent in tuples")
else:
  print("Element is not persent in tuples")

#Scling in tuples
start=int(input("Enter The Strat number of scling in tuples = "))
end=int(input("Enter The End number of  Scling in tuples = "))
num2=num[start:end]
print("After Scling new tuples is created " , num2)

