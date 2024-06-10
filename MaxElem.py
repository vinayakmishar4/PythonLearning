# Max value in python

List = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
max=List[0][0];

for i in range(len(List)):
    for j in range(len(List[i])):
            if List[i][j]>max:
             max=List[i][j]



print(max)
