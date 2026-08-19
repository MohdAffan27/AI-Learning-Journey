from functools import reduce
# Map example
l = [1,2,3,4,5,6]

square = lambda x:x*x
sqlist = map(square,l)#map(function, iterable)
print(list(sqlist))

# Filter Example
def even(n):
    if(n%2==0):
        return True
    return False

onlyeven = filter(even,l)#filter(function,iterable)
print(list(onlyeven))

# Reduce Example
sum = lambda x,y:x+y
mul = lambda x,y:x*y
print(reduce(sum,l))#reduce(func,iterable)
print(reduce(mul,l))