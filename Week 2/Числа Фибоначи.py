F = int(input())
n0 = 0
n1 = 1
k = 1
n2 = int()
while F > k:
    n2 = n0 + n1
    k += 1
    n0 = n1
    n1 = n2
print(n2)
