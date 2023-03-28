
# quiz_2_8_3.py

import random

while True:
    min_value = int(input("請輸入數字範圍的最小值: "))
    max_value = int(input("請輸入數字範圍的最大值: "))
    num_of_nums = int(input("請輸入要生成的數字數量: "))

    random_list = []
    for i in range(num_of_nums):
        random_list.append(random.randint(min_value, max_value))

    random_list.sort()

    print("你的隨機整數數列為: ", random_list)
    print('================================')
