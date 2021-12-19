"""
Визначити кількість від’ємних елементів матриці з обома парними індексами.
"""
A=[]
suma=0
r=int(input('Vvedit k-st ryadkiv matricu: '))
c=int(input('Vvedit k-st stovbciv matricu: '))
for i in range(r):
    A.append([int(input('{0} {1} el:'.format(i,j)))for j in range(c)])
for i in range(len(A)):
    for j in range(len(A)):
        if i%2 == 0 and j%2 == 0:
            if A[i][j] < 0:
                suma +=1
print(A)
print(suma)
