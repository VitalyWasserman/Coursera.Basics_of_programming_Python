n = int(input())
L = list(map(int, input().split()))
k = int(input())
j_max = 99999
for i in L:
    j = abs(k - i)
    if j_max > j:
        j_max = j
        i_max = i
print(i_max)

# OK
