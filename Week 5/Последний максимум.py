L = list(map(int, input().split()))
n = len(L)
i = 1
while i < n:
    if L[i - 1] < L[i]:
        Max = L[i]
        i += 1
        i_Max = (i - 1)
    else:
        i += 1
print(Max, i_Max)

# OK
