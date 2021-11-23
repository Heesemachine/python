
"""
Нехай x_0 = 0, x1 = 7 xi=xi-1(1+xi-2) .Визначити x_n.
"""


def create_x(i):
    if i == 0:
        return 0
    if i == 1:
        return 7
    else:
        x_i = (create_x(i - 1) * (1 + create_x(i - 2)))
        return (x_i)


i = int(input("Введіть номер елемента: "))
res = create_x(i)
print("{0}".format(res))