from array import array
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
A = []
print("\nEnter Matrix A:")
for i in range(rows):
    row = array('i')
    for j in range(columns):
        value = int(input(f"A[{i}][{j}]: "))
        row.append(value)
    A.append(row)
B = []
print("\nEnter Matrix B:")
for i in range(rows):
    row = array('i')
    for j in range(columns):
        value = int(input(f"B[{i}][{j}]: "))
        row.append(value)
    B.append(row)
result = []
for i in range(rows):
    row = array('i')
    for j in range(columns):
        value = A[i][j] + B[i][j]
        row.append(value)
    result.append(row)
print("\nMatrix A:")
for i in range(rows):
    print(A[i])
print("\nMatrix B:")
for i in range(rows):
    print(B[i])
print("\nResult of Matrix Addition:")
for i in range(rows):
    print(result[i])