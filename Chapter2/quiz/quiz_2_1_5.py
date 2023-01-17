# quiz_2_1_5.py

a = 3
b = 5
c = 7
print("給定三角形三個邊長：", a, b, c)

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("該三角形的面積為：", area)
