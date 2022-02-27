x1 = int(input())
x2 = int(input())
if x1 < x2:
    for i in range(x1, x2 + 1):
        print(i, end=' ')
else:
    for i in range(x1, x2 - 1, -1):
        print(i, end=' ')

# ok
