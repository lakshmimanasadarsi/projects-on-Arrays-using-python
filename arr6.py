from array import array
numbers = array('i')
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)
target = int(input("Enter target value: "))
found = False
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] + numbers[j] == target:
            print(
                "Pair:",
                numbers[i],
                "+",
                numbers[j],
                "=",
                target
            )
            found = True
if not found:
    print("No pair found")