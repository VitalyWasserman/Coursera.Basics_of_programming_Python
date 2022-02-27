#s = input('')
s = 'abfcdfgh'
n = s.count('f')
pos = s.find('f')
if n == 1:
    print(pos)
elif n > 1:
    while pos != -1:
        print(pos)




