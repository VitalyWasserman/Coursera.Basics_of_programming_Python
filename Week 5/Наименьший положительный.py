L = list(map(int, input().split()))
n = len(L)
i = 1
#for i in range(len(L)): или так или через while
while i < n:
    if L[i] > 0:
        Min = L[i]
        i += 1
    else:
        i += 1
print(Min)

#OK