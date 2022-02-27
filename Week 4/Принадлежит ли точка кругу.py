import math


def isPointInSquare(x, y, xc, yc, r):
    return math.sqrt((xc - x) * (xc - x) + (yc - y) * (yc - y)) <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if isPointInSquare(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
