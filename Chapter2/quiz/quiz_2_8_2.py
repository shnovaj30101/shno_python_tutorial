
# quiz_2_8_2.py

import random
import datetime

while True:
    start_year = int(input("請輸入起始年份: "))
    end_year = int(input("請輸入終止年份: "))

    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    print("你的隨機日期為: ", random_date)
    print('================================')

