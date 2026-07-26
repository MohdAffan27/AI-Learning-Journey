# program to find greatest of four number entered by the user
a = input("Enter number 1 : ")
b = input("Enter number 2 : ")
c = input("Enter number 3 : ")
d = input("Enter number 4 : ")

if(a>b and a>c and a>d):
    print("Greatest number is a :" ,a)

elif(b>a and b>c and b>d):
    print("Greatest number is b :" ,b)

elif(c>a and c>b and c>d):
    print("Greatest number is c :" ,c)

else:
    print("Greatest number is d :" ,d)