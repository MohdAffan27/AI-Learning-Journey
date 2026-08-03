#Find the number which was divisible by 5
def divisibleby5(n):
    if (n%5==0):
        return True
    return False

a = [1,5,7,11,13,15,16,17,4643,5665,595,325]
f = list(filter(divisibleby5,a))
print(f)