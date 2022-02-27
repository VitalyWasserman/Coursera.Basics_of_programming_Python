x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and y1 > 0:
    n = 1
elif x1 > 0 and y1 < 0:
    n = 2
elif x1 < 0 and y1 < 0:
    n = 3
else:
    n = 4
if x2 > 0 and y2 > 0:
    n1 = 1
elif x2 > 0 and y2 < 0:
    n1 = 2
elif x2 < 0 and y2 < 0:
    n1 = 3
else:
    n1 = 4
if n == n1:
    print('YES')
else:
    print('NO')
