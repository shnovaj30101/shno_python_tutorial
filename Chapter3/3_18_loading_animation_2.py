# 3_18_loading_animation_2.py

import time

for i in range(101):
    print(f'  [{"*"*i}->{"."*(100-i)}]    {i:>2d} %', end='\r')
    time.sleep(0.1)

print()