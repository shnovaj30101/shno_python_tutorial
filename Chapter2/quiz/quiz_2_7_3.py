# quiz_2_7_3.py

import time
from datetime import datetime

while True:
    now_time = datetime.now()
    now_time_str = datetime.strftime(now_time, "%Y/%m/%d %H:%M:%S")
    print("現在時間為：", now_time_str, end='\r')
    time.sleep(1)