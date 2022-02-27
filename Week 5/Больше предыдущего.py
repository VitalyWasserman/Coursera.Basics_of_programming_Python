L = list(map(int, input().split()))
n = len(L)
i = 1
while i < n:
    if L[i - 1] < L[i]:
        print(L[i], end=' ')
        i += 1
    else:
        i += 1


#OK