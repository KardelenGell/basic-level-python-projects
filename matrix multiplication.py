print("-Multiplication Of 2 Matrices-")

print("Please, enter the size of first matrix , A(x,y): ")
x = int(input())
y = int(input())

print("Please, enter the size of second matrix , B(m,n): ")
m = int(input())
n = int(input())

if y != m:
    print("-ERROR- \nMatrices cannot be multiplied.\nThe column size of the first matrix must be equal to the row size of the second matrix!")
else:
    A = [[0 for a in range(y)] for a in range(x)]
    B = [[0 for a in range(n)] for a in range(m)]
    M = [[0 for a in range(n)] for a in range(x)]

    print("\nEnter the elements of matrix A: ")
    for i in range(x):
        for j in range(y):
            print('A[{}][{}]'.format(i+1 , j+1))
            A[i][j] = int(input())

    print("\nEnter the elements of matrix B: ")
    for i in range(m):
        for j in range(n):
            print('B[{}][{}]'.format(i+1 , j+1))
            B[i][j] = int(input())

    for i in range(x):
        for j in range(n):
            for k in range(y):
                M[i][j] += A[i][k] * B[k][j];

print("\nResult: " + str(M))


