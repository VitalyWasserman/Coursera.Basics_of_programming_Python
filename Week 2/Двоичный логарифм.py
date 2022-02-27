n = int(input())
k = 0
res = 0
while res < n:
    k += 1
    res = 2 ** k
print(k)
