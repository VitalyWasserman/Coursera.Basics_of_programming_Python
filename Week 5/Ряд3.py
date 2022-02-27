n = int(input())
n1 = ('9'*n)
n2 = 10 ** (n - 1)
for i in range(int(n1), n2 - 1, -2):
    print(i, end=' ')

    #ok