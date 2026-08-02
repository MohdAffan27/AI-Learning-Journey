# Multiplication table
n = int(input("Enter a number: "))

table = [n*i for i in range (1,11)]
print(f"\n========= Table of {n} ========== \n")
for i, item in enumerate(table,start=1):
    print(f" {n} * {i} = {item}")

with open("table,txt","a") as f:
    f.write(str(table))