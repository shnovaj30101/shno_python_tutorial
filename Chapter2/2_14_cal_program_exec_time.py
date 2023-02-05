# 2_14_cal_program_exec_time.py

import time

start_time = time.time()

user_input = input("請隨便輸入一個字串： ")
print("這是你剛剛隨便輸入的一個字串喔： " + user_input)

end_time = time.time()

time_diff = end_time - start_time

print("運行總秒數: " + str(time_diff))