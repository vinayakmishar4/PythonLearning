#manputing tuples
num=(1,2,3,4,5,6,7,8,9,10)
print("before changing tuples indriecty",num)
# it will convert in list
num1=list(num) 
num1.append(11)
num1.pop(10)
num1[9]=0
num=tuple(num1)
print("After Changing tuple Indriecty = " , num)
# We can Concatting to list directly without manupting
num2=(1,2,5,6,7,6,8,9,10)
num3=num+num2
print("Concatting two tuples",num3)
