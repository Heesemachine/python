import random
a = [x for x in range(random.randint(1,10))]
print(a)
def pidp(x):
    if len(x) == 4:
        print('Підпослідовність містить послідовність з 4-х чисел')
    elif len(x) !=4:
        print('Підпослідовність не містить послідовність з 4-х чисел')
pidp(a)
