# 2_18_cal_future_time.py

import time
from datetime import datetime, timedelta

while True:
    seconds = int(input("請輸入需要計算的秒數："))
    now_time = int(time.time())
    future_time = now_time + seconds
    future_time_obj = datetime.fromtimestamp(future_time)
    print("經過", seconds, "秒後的時間為：", datetime.strftime(future_time_obj, "%Y/%m/%d %H:%M:%S"))
    print('==================================')