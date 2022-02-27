n = int(input())
setA = set()
for i in range(1, n + 1):
    setA.add(i)  # множество А

setB = input()  # предположенеи Б
while setB != 'HELP':
    setB = set(map(int, setB.split()))
    if input() == 'YES':  # ответ B
        setA &= setB
        setB = input()  # предположенеи Б
    else:
        setA -= setB
        setB = input()  # предположенеи Б
else:
    print(*sorted(setA))

# OK
