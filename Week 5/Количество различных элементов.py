L = list(map(int, input().split()))
i_uniq = 1
i_1 = L[0]
for i in L:
    if i != i_1:
        i_uniq += 1
        i_1 = i
print(i_uniq)

# OK
