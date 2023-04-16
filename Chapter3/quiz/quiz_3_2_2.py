# quiz_3_2_2.py

import random

while True:
    input("請按下 Enter 輸出一個數字範圍在 1 ~ 999 的隨機九宮格：")
    print(f"{random.randint(1,999):>5d}{random.randint(1,999):>5d}{random.randint(1,999):>5d}")
    print(f"{random.randint(1,999):>5d}{random.randint(1,999):>5d}{random.randint(1,999):>5d}")
    print(f"{random.randint(1,999):>5d}{random.randint(1,999):>5d}{random.randint(1,999):>5d}")
    print('==================================================')
    