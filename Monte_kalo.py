import random
import math

Total_count = [10,100,1000,10000,100000,1000000,10000000]

for t in Total_count:
    count = 0
    for i in range(t):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x*x + y*y)
        if dist <= 1:
            count += 1
    print(4*count/t)
