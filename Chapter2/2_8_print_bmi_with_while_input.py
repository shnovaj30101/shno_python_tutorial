# 2_8_print_bmi_with_while_input.py

while True:
    height = float(input("小明的身高為(cm)： "))
    weight = float(input("小明的體重為(kg)： "))
    print("小明的 BMI 為：", weight/(height*height/10000))
    print("==========================")
