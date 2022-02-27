a = int(input())
b = int(input())
c = int(input())
h = int()
k = int()
l = int()
# h - макс сторона k , l - длины других сторон
if (a + b > c) & (a + c > b) & (b + c > a):
    if a > max(b, c):
        h = a
        k = b
        l = c
    elif b > c:
        h = b
        k = a
        l = c
    else:
        h = c
        k = a
        l = b
    if h ** 2 == (k ** 2) + (l ** 2):
        print('rectangular')
    elif h ** 2 < (k ** 2) + (l ** 2):
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')


