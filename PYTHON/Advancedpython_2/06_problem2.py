# Find a maximum number from the list
from functools import reduce
l = [1,5,2,8,4,9,5,99,75]

maximum = lambda l:max(l)
print(reduce(max,l))