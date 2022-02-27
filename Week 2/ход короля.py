stb1 = int(input())
str1 = int(input())
stb2 = int(input())
str2 = int(input())
if stb1 == stb2:
    if (str1 - str2 == 1) or (str1 - str2 == -1):
        print('YES')
    else:
        print('NO')
elif str1 == str2:
    if (stb1 - stb2 == 1) or (stb1 - stb2 == -1):
        print('YES')
    else:
        print('NO')
elif ((stb1 - stb2 == 1) or (stb1 - stb2 == -1)) and \
        ((str1 - str2 == 1) or (str1 - str2 == -1)):
    print('YES')
else:
    print('NO')
