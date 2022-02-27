CountSettl = int(input())
RoadToSettls = list(map(int, input().split()))
for i in range(CountSettl):
    RoadToSettls[i] = [RoadToSettls[i], i + 1, 0]
RoadToSettls.sort()

CountBomb = int(input())
RoadToBombs = list(map(int, input().split()))
for i in range(CountBomb):
    RoadToBombs[i] = [RoadToBombs[i], i + 1, 0]
RoadToBombs.sort()

CountBomb_First = 0

for i in range(CountSettl):
    Min = 10e10
    index = 0
    for j in range(CountBomb_First, CountBomb):
        DeltaRoad = abs(RoadToSettls[i][0] - RoadToBombs[j][0])
        if DeltaRoad < Min:
            Min = DeltaRoad
            index = j
            RoadToSettls[i][2] = RoadToBombs[j][1]
        else:
            break

    CountBomb_First = index

RoadToSettls.sort(key=lambda index: index[1])
# print(RoadToSettls)


for k in RoadToSettls:
    print(k[2], end=' ')

# OK
