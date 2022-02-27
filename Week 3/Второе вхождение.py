s = input('')
n1 = s.find('f')
n2 = s.find('f', n1 + 1)
if n2 != -1:
    print(n2)
elif n1 != -1:
    print(-1)
else:
    print(-2)
