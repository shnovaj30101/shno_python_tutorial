# 3_16_loading_animation_1_1.py

import time

for i in range(101):
    print('  '+chr(10246)+'   ', i , "%", end='\r')
    time.sleep(0.1)
    print('  '+chr(10243)+'   ', i , "%", end='\r')
    time.sleep(0.1)
    print('  '+chr(10249)+'   ', i , "%", end='\r')
    time.sleep(0.1)
    print('  '+chr(10264)+'   ', i , "%", end='\r')
    time.sleep(0.1)
    print('  '+chr(10288)+'   ', i , "%", end='\r')
    time.sleep(0.1)
    print('  '+chr(10276)+'   ', i , "%", end='\r')
    time.sleep(0.1)

print()