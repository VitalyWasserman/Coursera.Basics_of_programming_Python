n = int(input())
i = 0
while 2 ** i <= n:
    res = 2 ** i
    i += 1
if res != n:
    print('NO')
else:
    print('YES')
