# quiz_3_3_2.py

import time

unit_num = int(input("請輸入進度條的單位個數（不大於 100）："))

for i in range(unit_num+1):
    progress_percent = 50*i/unit_num
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10246)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10243)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10249)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10264)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10288)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)
    print(f'  |{chr(9608)*int(progress_percent)}{" "*(50-int(progress_percent))}|  {chr(10276)}   {i}/{unit_num}  [{progress_percent:>6.2f}%]', end='\r')
    time.sleep(0.1)

print()
