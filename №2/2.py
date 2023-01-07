import random
n = int(input("Введите количество элементов Вашего списка: "))
ar = []
for i in range(n):
    ar.append(random.randint(0,10))
print(f"Вот Ваш список, состоящий из {n} произвольных чисел: {ar}")
ar_new = []
i = 0
j = 0
while i < n/2:
    ar_new.append(ar[i]*ar[j-1])
    i=i+1
    j=j-1
print(f"Вот новый список, заполненный произведением пар чисел из старого списка: {ar_new}")

