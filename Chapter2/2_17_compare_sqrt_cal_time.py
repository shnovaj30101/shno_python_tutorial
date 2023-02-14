# 2_17_compare_sqrt_cal_time.py

import time
from math import sqrt

start_time = time.time()

for i in range(10000000):
    i**0.5

end_time = time.time()

print("i**0.5 運行總秒數：", end_time - start_time)

start_time = time.time()

for i in range(10000000):
    sqrt(i)

end_time = time.time()

print("sqrt(i) 運行總秒數：", end_time - start_time)