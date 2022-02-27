L = list(map(int, input().split()))
i_max = L.index(max(L))
i_min = L.index(min(L))
i_min_temp = L[i_min]
L.insert(i_min, L[i_max])
L.pop(i_min + 1)
L.insert(i_max, i_min_temp)
L.pop(i_max + 1)
print(' '.join(map(str, L)))

#OK
