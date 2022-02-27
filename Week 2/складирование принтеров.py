room_a = int(input())
room_b = int(input())
room_h = int(input())
nout_a = int(input())
nout_b = int(input())
nout_h = int(input())
# ноут лежа, одноименными сторонами
kol_gor1 = room_a // nout_a
kol_vert1 = room_b // nout_b
kol_hight1 = room_h // nout_h
kol_summ1 = kol_gor1 * kol_vert1 * kol_hight1

# ноут лежа, разноименными сторонами
kol_gor2 = room_a // nout_b
kol_vert2 = room_b // nout_a
kol_hight2 = room_h // nout_h
kol_summ2 = kol_gor2 * kol_vert2 * kol_hight2

# ноут стоя, одноименными сторонами
kol_gor3 = room_a // nout_a
kol_vert3 = room_b // nout_h
kol_hight3 = room_h // nout_b
kol_summ3 = kol_gor3 * kol_vert3 * kol_hight3

# ноут стоя, разноименными сторонами
kol_gor4 = room_a // nout_b
kol_vert4 = room_b // nout_h
kol_hight4 = room_h // nout_a
kol_summ4 = kol_gor4 * kol_vert4 * kol_hight4

max_kol = max(kol_summ1, kol_summ2, kol_summ3, kol_summ4)

#print(kol_gor1, kol_vert1, kol_hight1, kol_summ1)
#print(kol_gor2, kol_vert2, kol_hight2, kol_summ2)
#print(kol_gor3, kol_vert3, kol_hight3, kol_summ3)
#print(kol_gor4, kol_vert4, kol_hight4, kol_summ4)
print(max_kol)