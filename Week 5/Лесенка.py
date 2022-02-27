n = int(input())
i = 1
while i <= n:
    T_n = tuple(range(1, i+1))
    i += 1
    s = str(T_n)
    s = s.replace('(', '' )
    s = s.replace(')', '')
    s = s.replace(',', '')
    s = s.replace(' ', '')
    print(s)

#ok