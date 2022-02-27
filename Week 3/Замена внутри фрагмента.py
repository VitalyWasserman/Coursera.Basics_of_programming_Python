s = input('')
n1 = s.find('h')
n2 = s.rfind('h')
n3 = s.count('h')
s1 = s[0:n1 + 1]
s2 = s[n1 + 1:]
if n1 != n2:
    s2 = s2.replace('h', 'H', n3 - 2)
print(s1, s2, sep='')

# OK