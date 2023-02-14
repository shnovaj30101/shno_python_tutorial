from datetime import datetime, timedelta

while True:
    seconds = int(input("請輸入需要計算的秒數："))
    now_time = datetime.now()
    future_time = now_time + timedelta(seconds=seconds)
    print("經過", seconds, "秒後的時間為：", datetime.strftime(future_time, "%Y/%m/%d %H:%M:%S"))
    print('==================================')