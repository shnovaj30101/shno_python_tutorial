# 3_6_format_function_dict_print_time.py

args_dict = {
    "days": 5,
    "hours": 20,
    "minutes": 3,
    "seconds": 15,
}

# 我想要print出 5天20時3分15秒
print("{days}天{hours}時{minutes}分{seconds}秒".format(**args_dict))