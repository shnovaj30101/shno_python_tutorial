# 2_20_cal_final_loan.py

from datetime import datetime, timedelta

while True:
    init_loan = int(input("請輸入貸款的本金(元)："))
    interest = int(input("請輸入貸款的利息(%)："))
    duration = int(input("請輸入多久會計算一次利息(天)："))
    lending_date_str = input("請輸入何時借錢(西元年/月/日)：") 
    cal_date_str = input("請輸入何時結算本利和(西元年/月/日)：")

    lending_date = datetime.strptime(lending_date_str, "%Y/%m/%d")
    cal_date = datetime.strptime(cal_date_str, "%Y/%m/%d")
    diff_day = (cal_date - lending_date).days
    print("結算出來的本利和為(元)：", int(init_loan*(1+interest/100)**int(diff_day/duration)))
    print("========================================")