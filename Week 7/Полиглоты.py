N = int(input())

setLang_one = set()
setLang_all = set()
setLang = set()
listLang = []
for j in range(1, N + 1):
    N_Mi = int(input())
    for i in range(1, N_Mi + 1):
        setLang.add(input())
    setLang_one |= setLang
    listLang.append(setLang)
    setLang = set()

setLang_all = set(listLang[0])
for k in range(1, len(listLang)):
    setLang_all &= set(listLang[k])

listLang_all = list(setLang_all)
listLang_one = list(setLang_one)

print(len(listLang_all))
for i in listLang_all:
    print(i)

print(len(listLang_one))
for i in listLang_one:
    print(i)

# OK
