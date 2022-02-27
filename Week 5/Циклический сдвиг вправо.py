L = list(map(int, input().split()))
n = len(L)
L.insert(0, L[n - 1])
L.pop(n)
print(*L)

#ok
