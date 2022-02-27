def Zero(x1, x2):
    if x2 != 0:
        x1 = x1 + x2
        x2 = int(input())
        Zero(x1, x2)
    else:
        return print(x1 + x2)


x1 = int(input())
x2 = int(input())
c = Zero(x1, x2)
