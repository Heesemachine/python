import random
import pickle

n = int(input("Кількість чисел = "))
a = [random.randint(-5, 5) for i in range(n)]
with open("file.txt", "wb") as file1:
    pickle.dump(a, file1)
with open("file.txt", "rb") as file1:
    b = pickle.load(file1)
print(b)
d_e = 0 # dodatni elementu
v_e = 0 # videmni elementu
for elements in b:
    if elements > 0:
       d_e += 1
    else:
        v_e += 1
if d_e > v_e:
    print("Додатніх елементів більше ніж відємних")
else:
    print("Відємних елементів більше ніж додатніх")
with open("d.dat", "wb") as file1:
    pickle.dump(d_e, file1)
with open("v.dat", "wb") as file1:
    pickle.dump(v_e, file1)