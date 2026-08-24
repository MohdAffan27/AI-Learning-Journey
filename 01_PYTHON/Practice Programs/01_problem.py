# Find: Maximum, Minimum, Sum, Average, Second-largest number

numbers = [12, 5, 8, 21, 3, 16, 10]

maximum = numbers[0]
minimum = numbers[0]
largest = numbers[0]
total_sum = 0
count = 0
second_largest = None

for num in numbers:
    total_sum += num
    count += 1

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    if num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or (num > second_largest and num != largest):
        second_largest = num

average = total_sum/count

print("maximum: ",maximum)
print("minimum: ",minimum)
print("sum: ",total_sum)
print("Average: ",average)
print("second_largest : ",second_largest)
        
