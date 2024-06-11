
Set = {1,2,3, 4,5,7,8,9}
Set.remove(5)
Set.discard(3)
popped_element = Set.pop()
print(Set,f"Popped element is {popped_element}")

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5, 7, 9, 1}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set2-set1
symmeteric_diff = set1 ^ set2
print(f"union set : {union_set}")
print(f"intersection set : {intersection_set}")
print(f"difference of sets : {difference_set}")
print(f"symmetric difference : {symmeteric_diff}")

Set = {2, 3, 4, 7, 8, 0}
copy_set = Set.copy()
set_length = len(Set)
print("copy of set ", copy_set," set length ", set_length)
Set.clear()
print("Original set ", Set)

Set = {2, 4, 5, 7, 8}
if 5 in Set:
    print("5 is in the set")
