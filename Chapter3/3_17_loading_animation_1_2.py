# 3_17_loading_animation_1_2.py

import time

for i in range(101):
    print(f'  {chr(10246)}    {i:>2d} %', end='\r')
    time.sleep(0.1)
    print(f'  {chr(10243)}    {i:>2d} %', end='\r')
    time.sleep(0.1)
    print(f'  {chr(10249)}    {i:>2d} %', end='\r')
    time.sleep(0.1)
    print(f'  {chr(10264)}    {i:>2d} %', end='\r')
    time.sleep(0.1)
    print(f'  {chr(10288)}    {i:>2d} %', end='\r')
    time.sleep(0.1)
    print(f'  {chr(10276)}    {i:>2d} %', end='\r')
    time.sleep(0.1)

print()