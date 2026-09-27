from array import array
numbers = array('i')
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
print("Array:", numbers)
print("Duplicate elements:")
found = False
for i in range(n):
    count = 0
    for j in range(n):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1:
        already_printed = False
        for k in range(i):
            if numbers[k] == numbers[i]:
                already_printed = True
        if not already_printed:
            print(numbers[i])
            found = True
if not found:
    print("No duplicate elements")