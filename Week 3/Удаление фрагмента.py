s = input('')
len = len(s)
n1 = s.find('h')
s2 = s[::-1]
n2 = len - (s2.find('h')) - 1
print(s[:n1], s[n2 + 1:], sep='')
