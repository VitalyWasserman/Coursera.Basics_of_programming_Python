s = int(input())
L = list(map(int, input().split()))
k = 0
s_max = s
for i in L:
    if i == s or (i - s_max) >= 3:
        # print(i)
        s_max = i
        k += 1
print(k)

# OK
