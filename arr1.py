from array import array
numbers = array('i')
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
print("\nArray:", numbers)
largest = numbers[0]
for i in range(1, n):
    if numbers[i] > largest:
        largest = numbers[i]
smallest = numbers[0]
for i in range(1, n):
    if numbers[i] < smallest:
        smallest = numbers[i]
total = 0
for i in range(n):
    total = total + numbers[i]
average = total / n
print("\n----- Array Statistics -----")
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)

