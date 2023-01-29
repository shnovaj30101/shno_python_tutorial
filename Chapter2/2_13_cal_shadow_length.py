# 2_13_cal_shadow_length.py

import math

while True:
    angle = float(input("請輸入太陽的仰角："))
    bamboo_len = float(input("請輸入竹竿的長度："))

    print("該竹竿投射出來的影子長度為：",  bamboo_len / math.tan(math.radians(angle)))
    print("=============================")

