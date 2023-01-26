# 2_9_cal_bmi_with_comment.py

while True:
    # 以下經過縮排的程式
    # 是 while 迴圈會重複執行的部分
    
    height = float(input("小明的身高為(cm)： "))
    weight = float(input("小明的體重為(kg)： "))
    print("小明的 BMI 為：", weight/(height*height/10000))
    print("==========================") # 這是分隔線
