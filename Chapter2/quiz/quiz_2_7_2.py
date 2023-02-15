# quiz_2_7_2.py

from datetime import datetime

while True:
    ori_time_str = input("請輸入要轉換的日期(%Y/%m/%d %H:%M:%S)：")
    target_time = datetime.strptime(ori_time_str, "%Y/%m/%d %H:%M:%S")
    output_time_str = datetime.strftime(target_time, "%a %b %d %H:%M:%S %Y")
    print("轉換過後的日期時間為：", output_time_str)
    print("==================================")
