def isPointInSquare(x, y):
    return x == y


x = float(input())
y = float(input())
if isPointInSquare(x, y):
    print(0)
else:
    print(1)
