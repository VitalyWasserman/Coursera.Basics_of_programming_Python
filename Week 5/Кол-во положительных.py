L = list(map(int, input().split()))
i = 0
n = len(L)
while i < n:
    if L[i] > 0:
        print(L[i], end=' ')
        i += 1
    else:
        i += 1

# OK