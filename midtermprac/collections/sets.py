'''
Set
'''
# to construct a set use the curly braces
departments = {'Sales', 'Engineering', 'Marketing', 'Finance'}

# Sets are:
# 1. unordered: the order of items is not guaranteed
# 2. immutable: items cannot be changed
# 3. unique: duplicates are not allowed

# The distinguishing feature about sets is that they don't allow duplicates
departments_with_duplicates = {'Sales', 'Sales',
                                'Engineering', 'Marketing', 'Finance'}

# the above two sets are identical, because one of the two Sales items will be removed (no duplicated allowed)
# print(departments_with_duplicates)
# to add an item to a set use the add function
# departments.add('Accounting')
# print(departments_with_duplicates)
# to remove an item from a set use the remove or pop functions
# departments.remove('Sales')
# with sets pop doesn't accept an argument because items in a set are not accessible
# departments.pop()
# print(departments_with_duplicates)
# looping over a set
# for department in departments_with_duplicates:
#     print(department)

car = {'honda', 'toyota', 'bmw', 'benz', 'honda'}
print(car)

car.add('ford')
print(car)
car.pop()
print(car)