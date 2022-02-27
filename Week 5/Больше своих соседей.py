L = list(map(int, input().split()))
kol = 0
for i in range(1, len(L)):
    if L[i] > L[i - 1] and L[i] > L[i + 1]:
        kol += 1
print(kol)

#ok