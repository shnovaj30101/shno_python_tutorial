# quiz_2_1_6.py

a = 2574

print("給定一個整數：", a)
print("該整數的千位數為：", a//1000)
a %= 1000
print("該整數的百位數為：", a//100)
a %= 100
print("該整數的十位數為：", a//10)
a %= 10
print("該整數的個位數為：", a)

