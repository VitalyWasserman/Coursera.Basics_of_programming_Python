F = int(input())
n0 = 0
n1 = 1
k = 1
n2 = 1
while F > n2:
    n2 = n0 + n1
    k += 1
    n0 = n1
    n1 = n2
if F == n2:
    print(k)
else:
    print('-1')