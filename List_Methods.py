# list meoths in python
num1=[6,7,8,3,0,4,1]
# append is add number in the list
num1.append(13)
# it sort the list in ascending order
num1.sort()
print("List is stored in increasing order ", num1)
# it sort the list in descending order
num1.sort(reverse=True)
print("List is sorted in decreasing order" , num1)
# it reverse the list
num1.reverse();
print("List in Reverse order" , num1)
# index fuction used to print the number at  that index
print("Number of List " , num1.index(4))
num2=[2,4,4,5,5,7,7,8,8,8]
print("Number of times a number of occurrences " , num2.count(8))
# it will copy who thing as it is without changing 
num3=num2.copy()
print("Number are copied from the nunmber one to thrid " , num3)
# it will insert the number at given index of list
num3.insert(1,67)
print("After The Insert",num3)
# Concatenate the two lists together
num=num1+num2+num3
print("List are cobimed together",num)
