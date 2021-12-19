n = int(input("Рядки : "))
m = int(input("Стовпці : "))
suma = 0
a = [[(1/(i+j)) for j in range(1,m)] for i in range(1,n)]
print(*a, sep="\n")
for i in range(len(a)):
    for j in range(len(a)):
        if (i+j)%2 == 1:
            suma += a[i][j]
print("Сума відємних елементів матриці з парною сумою індексів : {0:.2f}".format(suma))
