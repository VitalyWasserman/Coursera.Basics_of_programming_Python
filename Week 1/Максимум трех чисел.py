a = int(input('Введите число 1\n'))
b = int(input('Введите число 1\n'))
c = int(input('Введите число 1\n'))
if a > b:
    if a > c:
        print (a)
    else:
        print (b)
elif b > c:
    print (b)
else:
    print (c)