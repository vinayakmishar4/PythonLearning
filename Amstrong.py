# Check if a number is an Armstrong number
x = int(input("Enter a number: "))

# Find the length of the number
t1 = x
length = 0
while t1 != 0:
    t1 //= 10
    length += 1

# Find Armstrong number
t2 = x
sum = 0

while t2 != 0:
    re = t2 % 10
    mul = 1
    for i in range(length):
        mul *= re
    sum += mul
    t2 //= 10

if x == sum:
    print(f"{x} is an Armstrong Number")
else:
    print(f"{x} is not an Armstrong Number")
