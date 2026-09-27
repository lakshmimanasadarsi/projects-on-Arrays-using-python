from array import array
numbers = array('i')
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
print("\nArray:", numbers)
print("\nFrequency:")
for i in range(n):
    already_checked = False
    for j in range(i):
        if numbers[j] == numbers[i]:
            already_checked = True
    if not already_checked:
        count = 0
        for j in range(n):
            if numbers[i] == numbers[j]:
                count += 1
        print(numbers[i], "->", count, "times")