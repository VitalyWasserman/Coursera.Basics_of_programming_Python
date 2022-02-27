k = int(input())
if k % 3 == 0 or k % 5 == 0 or k % 8 == 0:
    print('YES')
elif k >= 3 and 5 * (k // 5) % 3 == 0:
    print('YES')
elif k >= 3 and 5 * ((k // 5) - 1) % 3 == 0:
    print('YES')
elif k >= 3 and 5 * ((k // 5) - 2) % 3 == 0:
    print('YES')
else:
    print('NO')