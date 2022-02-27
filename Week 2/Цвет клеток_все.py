stb1 = int(input())
str1 = int(input())
stb2 = int(input())
str2 = int(input())
if stb1 == stb2 and (str1 - str2) % 2 == 0:
    print('YES')
elif str1 == str2 and (stb1 - stb2) % 2 == 0:
    print('YES')
elif (((str1 - str2) % 2 == 0) and ((stb1 - stb2) % 2 == 0)) or \
        (((str1 - str2) % 2 != 0) and ((stb1 - stb2) % 2 != 0)):
    print('YES')
else:
    print('NO')
