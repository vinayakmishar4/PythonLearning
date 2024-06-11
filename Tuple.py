my_tuple = (2, 4, "Python", 5.0, -3)
ele_1 = my_tuple[-2]
ele_2 = my_tuple[2]
print (ele_1, ele_2)

my_tuple = (1, 3, "Geeks", 4.0, "python", 1)
index= my_tuple.index('python')
count = my_tuple.count(1)
print (f"index of python: { index }, count of 1 : {count}")

packed_tuple = 1, 2, 'three'

# Tuple unpacking
a, b, c = packed_tuple
print (f" packed Tuple : {packed_tuple}, unpacked tuple a: {a}, b: {b}, c : {c}")
