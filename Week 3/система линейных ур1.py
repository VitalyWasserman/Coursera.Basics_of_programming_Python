a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0 and (a * d - c * b) != 0:
    y = (f * a - c * e) / (a * d - c * b)
    x = (e - b * y) / a
    print(x, y)
else:
    if a == 0:
        y = e / b
        x = (b * f - d * e) / (b * c)
        print(x, y)
    elif b == 0:
        x = e / a
        y = (f * a - c * e) / (a * d)
        print(x, y)
    elif c == 0:
        y = f / d
        x = (e * d - b * f) / (d * a)
        print(x, y)
    elif d == 0:
        x = f / c
        y = (e * c - a * f) / (b * c)
        print(x, y)
