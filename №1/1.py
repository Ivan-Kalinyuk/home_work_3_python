import random
n = int(input("Введите количество элементов Вашего списка: "))
ar = []
for i in range(n):
    ar.append(random.randint(0,20))
print(f"Вот список, заполненный произвольными числами: {ar}")
sum = 0
i=1
while i < n:
    sum = sum + ar[i]
    i = i + 2
print(f"Сумма чисел, стоящих на нечетных позициях из этого списка = {sum}")
