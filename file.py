# f = open('configuration.txt', 'rt')

# content = f.read()

# print(content)

my_tuple = (1, 2, 3, 'a', 'b', 'c', [4, 5, 6])


# print(my_tuple[::2])

(x,y,z) = (15,25,35)

r = y%x
# print(r)

my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'

import re
a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
# print(a.group(1))

r1=range(10)
print(list(map((lambda a: a * 10), r1))[-1])