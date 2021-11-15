"""
Побудувати прямокутну матрицю А, елементи якої задаються формулою:
Aij = 1 / (i+j), i,j = 1,N
"""
A = []
sum = 0
N=int(input("N = "))
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i,j in range(n,m):
    A.append([(1/(i+j))])
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > 0 and (i+1) % 2 == 0 and (j+1) % 2 != 0:
            sum += 1
print(A)
print(sum)