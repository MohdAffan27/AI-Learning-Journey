# print a Multiplication Table
def mul(n):
    for i in range (1,11):
        print(n,"X",i,"=",n*i)

n = int(input("Enter a number for a Table : "))
mul(n)