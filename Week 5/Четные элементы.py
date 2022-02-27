L = list(map(int, input().split()))
i = 0
n = len(L)
#for i in range(len(L)): или так или через while
while i < n:
    if L[i] % 2 == 0:
        print(L[i], end=' ')
        i += 1
    else:
        i += 1


#ok