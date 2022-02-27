n = int(input())
i = 1
T = ()
while i <= n:
    T = T + tuple(input())
    i += 1
#print(T)
print(T.count('0'))


#ok