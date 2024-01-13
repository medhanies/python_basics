'''
Tuple
'''
# to construct a tuple use the parantheses
ids = (154, 187, 192, 101)

# Like lists, tuples allow duplicates and are ordered.
# unlike lists, tuple are immutable (can not change!)

# Tuple items are accessed the same way as lists:
# like lists (and all other Python collections), tuples are use 0-based index
id1 = ids[0]
id2 = ids[1]

# you can use the in keyword to check if an item exists in a tuple:
# if 154 in ids:
#     print('154 ID is found')

# loop over tuple:
# for id in ids:
#     print(id)
# or
for i in range(len(ids)):
    print(ids[i])

print(id1, id2)

num = (1,2,3,3,4,5,6,6,7,32,23)
# print(num)

# for _ in num:
#     print(_)

for i in range(len(num)):
    print(num[i])
