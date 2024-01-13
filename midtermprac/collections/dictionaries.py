'''
Dictionaries
'''
# Dictionaries are a collection of key, value pairs:


employee_name_by_id = {
    1: 'John Doe',
    2: 'Jane Doe',
    3: 'James Doe'
}

# to access an item in a dictionary use the get function:
print(employee_name_by_id.get(1))  # returns John Doe
# returns None (i.e., key with value 4 is not found in the dictionary)
print(employee_name_by_id.get(4))

# to add an item to a dictionary:
employee_name_by_id[4] = 'Medhanie Doe'
# note keys in dictionary are unique, if you add a new value to an existing key it will overide the existing value

# to get all the keys
print(employee_name_by_id.keys())

# to get all values
print(employee_name_by_id.values())

# to get all items: a list of key, value tuples
print(employee_name_by_id.items())

# to loop over dictionary:
# 1. you can loop over the keys and use each key in the iteration to query the value from the dictionary:
# for id in employee_name_by_id.keys():
#     print(f'Employee id: {id}, Employee name: {employee_name_by_id[id]}\n')
# 2. you can loop over the values in the dictionary directly:
# for name in employee_name_by_id.values():
#     print(f'Employee name: {name}\n')
# 3. you can loop over the items in the dictionary, this provides you a variable reference to the key and value
# in each iteration:
# for id, name in employee_name_by_id.items():
#     print(f'Employee ID: {id}, Employee name: {name}\n')

# print(employee_name_by_id.keys(), '\n')
# print(employee_name_by_id.values(), '\n')
# print(employee_name_by_id.items(), '\n')

name = {
    'bill':1,
    'todd':2,
    'jane':3
}

print(name)

print(name.get('bill'))

print(name.keys())
print(name.values())

for n in name.keys():
    print(f'name: {n}, id: {name[n]}')

for n in name.values():
    print(f'name: {name["bill"]}, id: {n}')

for n, id in name.items():
    print(f'name: {n}, id: {id}')
