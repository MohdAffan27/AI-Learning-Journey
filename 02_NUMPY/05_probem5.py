import numpy as np

# 1. Pick the number you want a table for
target_number = int(input("Enter a number for a Multiplication Table : "))

# 2. Generate numbers from 1 to 10 using linspace
multipliers = np.linspace(1, 10, 10, dtype=np.int32).reshape(10, 1)

# 3. Multiply the single number by the entire list
table = target_number * multipliers

# 4. Loop through the rows to print them line by line
for i in range(10):
    # .item() converts the NumPy grid value into a clean, normal number
    m = multipliers[i].item()
    t = table[i].item()
    print(f"{target_number} X {m} = {t}")