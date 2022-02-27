CountSettl = int(input())
RoadToSettls = []
# CountSettl = 5
# RoadToSettls = [(25, 1), (5, 2), (20, 3), (10, 4), (15, 5)]
temp_Settl = input().split()
for i in range(CountSettl):
    RoadToSettls.append((int(temp_Settl[i]), i))
RoadToSettls.sort()

CountBomb = int(input())
RoadToBombs = []
# CountBomb = 3
# RoadToBombs = [(30, 1), (10, 2), (17, 3)]
temp_Bombs = input().split()
for i in range(CountBomb):
    RoadToBombs.append((int(temp_Bombs[i]), i))
RoadToBombs.sort()
Itog = []
for i in range(CountSettl):
    DeltaRoad_Settl_Bomb = []
    for j in range(CountBomb):
        DeltaRoad = abs(RoadToSettls[i][0] - RoadToBombs[j][0])
        # разница м-у расстояниями сел и бомб
        DeltaRoad_Settl_Bomb.append((DeltaRoad, RoadToSettls[i][1], RoadToBombs[j][1]))
        # делаем список кортежей из разницы  и номеров селений и бомб
    #print(DeltaRoad_Settl_Bomb)
    DeltaRoad_Settl_Bomb.sort()  # сортируем по минимальному расстоянию
    # print(DeltaRoad_Settl_Bomb)
    # print(DeltaRoad_Settl_Bomb[0][1], DeltaRoad_Settl_Bomb[0][2])
    Itog.append((DeltaRoad_Settl_Bomb[0][1], DeltaRoad_Settl_Bomb[0][2]))
    # делаем список толкьо из пар номеров сел и бомб, выбираем номера
    # толкьо для минимального расст-я после сортировки(всегда будет первым)
Itog.sort()  # сортируем по номеру сел
# print(Itog)
for k in Itog:
    print(k[1] + 1, end=' ')

# print(RoadToSettls)
# print(RoadToBombs)
# print(Itog)

# OK
