from functools import reduce
from random import randint
n, m = 4, 4
a = [[randint(10, 99) for _ in range(m)] for _ in range(n)]

for i in range(len(a)):
    if a[i][i] == 0:
        row_ind = i+1
        while row_ind<len(a) and a[row_ind][i] == 0:
            row_ind += 1
        if row_ind<len(a):
            a[i], a[row_ind] = a[row_ind], a[i]
    if a[i][i] != 0:
        for r in range(i+1,len(a)):
            if a[r][i] != 0:
                d = - a[r][i]/a[i][i]
                for j in range(i, len(a)):
                    a[r][j] = a[i][j]*d + a[r][j]

print(*a, sep='\n')
