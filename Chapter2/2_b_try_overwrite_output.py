# 2_b_try_overwrite_output.py

import time

print("hi你好 我是一隻小狗", end='\r')
time.sleep(1)
print("hi你好 我是一隻小貓", end='\r') # 會覆寫掉 "hi你好 我是一隻小狗"
time.sleep(1)
print("hi你好 我是一隻小兔子", end='\r') # 會覆寫掉 "hi你好 我是一隻小貓"
time.sleep(1)
print("###", end='\r') # 會覆寫掉原本的輸出，但不會覆寫全部
time.sleep(1)
print("@@@@@", end='\r') # 會覆寫掉原本的輸出，但不會覆寫全部
time.sleep(1)
print("$$$$$$$", end='\r') # 會覆寫掉原本的輸出，但不會覆寫全部
time.sleep(1)