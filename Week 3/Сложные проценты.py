#import time

p = int(input())
x = (int(input())) * 100
y = int(input())
k = int(input())
k1 = 1
#start_time = time.time()
res1 = int(((x + y) + (x + y) * p / 100))
res = 0
while k1 < k:
    res = int(res1 * p / 100 + res1)
    k1 += 1
    res1 = res
print(res1)
print(int(res / 100),  res - int(res / 100)*100)
#print("---%s seconds---" % (time.time() - start_time))