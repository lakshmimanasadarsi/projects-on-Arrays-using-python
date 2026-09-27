from array import array
numbers = array('i')
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
k = int(input("Enter number of rotations: "))
for r in range(k):
    first = numbers[0]
    for i in range(n - 1):
        numbers[i] = numbers[i + 1]
    numbers[n - 1] = first
print("Array after left rotation:", numbers)