Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Data', 2: 'Science', 3: 'Python'})
print("Dictionary with the use of dict() method: ")
print(Dict)

Dict = dict([(1, 'Data'), (2, 'Science')])
print("Dictionary with each item as a pair: ")
print(Dict)

my_dict = {'name':'Rose', 'age': 24}
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('name','Unknown'))
print(my_dict.get('city','Unknown'))

my_dict = {'name':'Rose', 'age': 24}
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('name','Unknown'))
print(my_dict.get('city','Unknown'))

Dict = {}
Dict['name'] = 'Rose'
Dict['age'] = 24
Dict['city'] = 'Gwalior'
Dict ['city'] = 'Jaipur'
print("Dictionary after adding/modifying elements: ")
print(Dict)

#modifying dict using update function
print("Dictionary after modifying elements through update:")
Dict.update({'age':26,'city':'Noida'})
print(Dict)

Dict = {'name':'Rose','age':24, 'gender':'Female'}

#removing a key using pop
removed_value = Dict.pop('gender')
print(removed_value)
print(Dict)

# Removing a key using del
del(Dict['age'])
print(Dict)

my_dict = {'name':'Rose','age':24, 'gender':'Female'}
for key in my_dict:
    print(key, end=' ')
print('\n')
# Iterating through values
for value in my_dict.values():
    print(value, end=' ')
print('\n')
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value, end = ' ')
