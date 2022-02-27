def ReduceFraction(n, m):
    i = 2
    while i <= n:
        while n % i == 0 and m % i == 0:
            p = n / i
            q = m / i
            n = p
            m = q
        else:
            i += 1
    #print(n, m)


n = int(input())
m = int(input())
print(ReduceFraction(n, m))


#ok
