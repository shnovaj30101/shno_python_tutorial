# quiz_2_7_1.py

from datetime import datetime

while True:
    init_invest = int(input("請輸入小明的初始資金(元)："))
    every_year_invest = int(input("請輸入每滿一年後固定加注投資的金額(元)："))
    earning_rate = int(input("請輸入每滿一年的固定收益率(%)："))
    enter_time_str = input("請輸入初入股場的時間(西元年/月/日)：")
    leave_time_str = input("請輸入退隱江湖的時間(西元年/月/日)：")

    enter_time = datetime.strptime(enter_time_str, "%Y/%m/%d")    
    leave_time = datetime.strptime(leave_time_str, "%Y/%m/%d")    
    diff_time = leave_time - enter_time

    ans = init_invest
    for i in range(int(diff_time.days/365)):
        ans *= (1+earning_rate/100)
        ans += every_year_invest

    print("小明經過這些年來的總資產為(元)：", int(ans))
    print("===================================")