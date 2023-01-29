# quiz_2_5_2.py

import math

while True:
    base = int(input("請輸入底數："))
    exponent = int(input("請輸入指數："))

    log_ans = math.log10(base**exponent)
    ans = math.floor(log_ans) + 1

    print(base, "的", exponent, "次方為", ans, "位數")
    print("=============================")

    
