# 2_3_time_calculation.py

ori_hour = 12
ori_minute = 34
ori_second = 28
pass_second = 8543

print("起始時間為", ori_hour, "時", ori_minute, "分", ori_second, "秒")
print("經過了", pass_second, "秒之後...")

end_hour = ori_hour + pass_second // 3600
pass_second %= 3600
end_minute = ori_minute + pass_second // 60
pass_second %= 60
end_second = ori_second + pass_second

print("最終時間為", end_hour, "時", end_minute, "分", end_second, "秒")
