# #collection: variable that has multiple values

# #List: ordered, mutable, allow duplicates
# #Tuple: ordered, immutable, allow duplicates
# #Set: unordered, immutable, no duplicates
# #Dictionary: ordered, mutable, no duplicates
'''
List
'''
#     #ordered: order of the items in a list is guaranteed
#     #mutable: items can be added, removed, and updated
#     #allow duplicates: list can store 2 identical items

name = ['medhanie', 'biden', 'joe', 'bill', 'tony']
# to retrieve an element from a list use the element's index between square brackets
medhanie = name[0]  # this will return the first element in the list
biden = name[1]  # second element in the list

#add elements to a list
name.append('richard') #this will add items to the end of a list

# to insert an element in a specific position use the insert funtion
name.insert(3, 'carl')

# to remove an item from a list:
# remove function
name.remove('tony')

#delete items by value 
del name[2] #deletes the 3rd item in the list

# pop function: returns and removes the item with the given index
# print(name.pop(4))

# use the built-in len function to get the number of elements in a list
size = len(name)

# ways to loop over a list
# for _ in name:
    # print(_)
# or
# for i in range(len(name)):
    # print(name[i])

print(name)
print(name[0])
print(name.remove('richard'))
print(name)
name.append('medhanie')
print(name)
name[-1] = 'tom'
print(name)