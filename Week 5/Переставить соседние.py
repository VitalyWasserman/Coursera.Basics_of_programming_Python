L = list(map(int, input().split()))
n = 1
for i in L[1::2]:
    L.insert(n - 1, i)
    L.pop(n + 1)
    n += 2
#print(*L)
print(' '.join(map(str, L)))

#OK
