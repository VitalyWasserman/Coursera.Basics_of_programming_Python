N = int(input())
L = list(map(int, input().split()))
L = L[:N]
L.sort()
# print(*L)
print(' '.join(map(str, L)))

# OK
