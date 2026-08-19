# find gratest of three numbers
def greatest(a,b,c):
    if (a>b and a>c):
        return a
    if (b>a and b>c):
        return b
    if (c>a and c>b):
        return c

c = int(input("Enter number1 : "))
a = int(input("Enter number2 : "))
b = int(input("Enter number3 : "))

print(greatest(a,b,c))