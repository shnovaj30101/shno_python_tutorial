# 3_14_time_sleep_print_without_flush.py

import time
for i in range(5): # for 迴圈現在還沒有講到，但這裡的作用是讓下面兩行可以重複執行 5 次
    print('ha ', end='')
    time.sleep(0.5)