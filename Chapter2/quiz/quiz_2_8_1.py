# quiz_2_8_1.py

import random

while True:
    min_value = int(input("請輸入最小值: "))
    max_value = int(input("請輸入最大值: "))

    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    num3 = random.randint(min_value, max_value)

    print("你的隨機數字為: ", num1, num2, num3)
    print('================================')

