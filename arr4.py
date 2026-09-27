from array import array
numbers = array('i')
n = int(input("Enter n: "))
print("Enter", n - 1, "numbers:")
for i in range(n - 1):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
total = 0
for i in range(1, n + 1):
    total = total + i
array_total = 0
for i in range(n - 1):
    array_total = array_total + numbers[i]
missing = total - array_total
print("Array:", numbers)
print("Missing number:", missing)