'''
Everything in Python is an object including functions. That means functions can:
1. assigned to variabled
2. be passed as arguments to other functions
3. be returned by other functions 
'''


def sum(a, b):
    return a + b


sum_func = sum  # functions can be assigned to variables
print(type(sum_func))  # this will return <class function>
# this will call the sum function since sum_func variable has the sum func as a value
print(sum_func(2,2))

'''
Function can be passed as arguments
'''

def execute(func):  # this function simply takes in a function as an argument and calls it
    func()

def simple_func():
    print('Hello world!')


# here the simple_func is passed as a parameter argument to execute function
# execute(simple_func)
# e = execute
# e(simple_func)

'''
Functions can be returned by other functions
'''


def get_printer():
    def prints(message):
        print(message)
    return prints

get_printer()('hello')
# since get_printer returns a function, the printer variable is a function
printer = get_printer()
print(type(printer))  # this will return <class function>
# since printer is a function, it can be called like any other function
printer('Hello world')

# a short hand to do the same is:
# this saves the step of assigned the returned function from get_printer to a variable and then calling that variable
# get_printer()('Hello world')


def x():
    def y(message):
        print(message)
    return y

# p = x()
# print(type(x))

# p('Hello World')

# x()('hello there')

def name(name='medhanie'):
    print('name')

    def id():
        return '\t mms150330'
    
    if name == 'medhanie':
        return id
    else:
        print('error')

# func = name()
# print(func())

# def cool():
#     def super_cool():
#         return 'I am super cool'
#     return super_cool

# # cool()
# me = cool()
# print(me())

def greet():
    return 'my name is medhanie'

def other(new_func):
    print('this is other func')
    print(new_func())

# other(greet)