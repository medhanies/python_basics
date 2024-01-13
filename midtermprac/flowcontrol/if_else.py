'''
  Flow control
'''
# if/else statement
if 1 == 1:
    print('duh!')
else:
    print('The world is ending!')

# an if statement controls whether a block of code will execute or not
# the code will execute only when the if statement condition evaluates to True
# syntax: if <condition> : <code>

# common conditional operators:
# == :  equals
# != :  does not equal
# > :   greater than
# >= :  greater than or equal
# < :   less than
# <=    less than or equal
# and:  combine two conditions with and
# or:   comines two conditions with or

animal = 'dog'
if animal == 'cat':
    print('a cat!')
elif animal == 'fish':  # use elif to nest if statements. Like if, elif expects a condition which determines whether the code block will execute
    print('a fish!')
else:
    print('It must be a dog!')

year = [2000, 2001, 2002, 2003]
name = ['karl', 'mike', 'jan', 'bob']

if year[0] == 2000 and name[2] == 'jan':
    print(year[0], name[2].title())
else:
    print('Wrong year and name')
