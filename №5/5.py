n = int(input('Введите любое натуральное число: '))
ar1 = [0,1]
ar2 = [-1,-1]
i = 0
j = 0
while i < n-1:
    ar1.append(ar1[i]+ar1[i+1])
    i=i+1
while j < n-2:
    ar2.append(ar2[j]+ar2[j+1])
    j=j+1
print(ar1)
k=0
while k < n:
    ar2[k] = ar2[k] * (-1)
    k = k + 2
ar2.reverse()
print(ar2)
ar2 = ar2 + ar1
print(ar2)

