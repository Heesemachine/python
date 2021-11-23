"""
Побудувати прямокутну матрицю А, елементи якої задаються формулою:
a_ij = 1 / (i+j)
Обчислити суму додатних елементів елементів матриці А.
"""
A = []
sum_d = 0
b = int(input('Рядки: '))
c = int(input('Стовпці: '))
for i,j in range(b,c):
    A.append([1 / ((i + j)) for j in range(c)])
print(A)
for i in range(b):
    for j in range(c):
        if A[i][j] < 0 and (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
            sum_d += 1
print("Сума відємних елементів матриці з парною сумою індексів : {0:.2f}".format(sum_d))