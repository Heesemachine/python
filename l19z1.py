import random
import pickle # modul dlya roboty z filamu


n = int(input("Кількість чисел = "))
a = [random.randint(-5, 5) for i in range(n)]
with open("file.txt", 'wb') as file:
    pickle.dump(a, file)
with open("file.txt", "rb") as file:
    b = pickle.load(file)
print(b)
sum_2 = 0 # suma parnuh
for elements in b:
    if elements % 2 == 0:
        sum_2 += 1
print("Кількість парних чисел = {0}".format(sum_2))