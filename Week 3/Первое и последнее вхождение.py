s = input('')
len = len(s)
n1 = s.find('f')
if n1 == -1:
    print()
else:
    s2 = s[::-1]
    n2 = len - (s2.find('f')) - 1
    if n1 == n2:
        print(n1)
    else:
        print(n1, n2)
