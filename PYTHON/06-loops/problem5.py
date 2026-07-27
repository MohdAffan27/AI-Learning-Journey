# Find a factorial of a number 
n = int(input("Enter a number : "))

i = 1
fact = 1
while(i<=n):
    fact *= i
    i += 1
print(fact)