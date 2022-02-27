import math


def distance(x1, y1, x2, y2):
    res = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return res


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
