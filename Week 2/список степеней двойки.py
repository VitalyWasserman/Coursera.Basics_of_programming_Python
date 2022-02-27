n = int(input())
i = 0
res = 0
while n >= res:
    res = 2 ** i
    i += 1
    if res <= n:
        print(res, end = ' ')

