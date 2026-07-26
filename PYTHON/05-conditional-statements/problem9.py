# calculator

num1 = float(input("Enter number 1 : "))
op = input("Enter a operand (=,-,*,/) : ")
num2 = float(input("Enter number 2 : "))

if (op == "+"):
    print(num1,"+",num2,"=",num1+num2)
elif (op == "-"):
    print(num1,"-",num2,"=",num1-num2)
elif (op == "*"):
    print(num1,"*",num2,"=",num1*num2)
elif (op == "/"):
    if num2 != 0:
        print(num1,"/",num2,"=",num1/num2)
    else:
        print("Invalid number entered!")