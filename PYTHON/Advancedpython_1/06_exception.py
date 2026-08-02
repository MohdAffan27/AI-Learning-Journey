try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    result = a / b
    print(f"{result:.2f}")
    
except ZeroDivisionError as z:
    print("infinite")