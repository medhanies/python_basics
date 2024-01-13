def area(a, b):
    return a * b

print(area(4, 8))

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)

print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))