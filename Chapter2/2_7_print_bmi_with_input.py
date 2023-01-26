# 2_7_print_bmi_with_input.py

height = float(input("小明的身高為(cm)： "))
weight = float(input("小明的體重為(kg)： "))
print("小明的 BMI 為：", weight/(height*height/10000))
