# 3_19_write_power_result_table_to_file.py

file_obj = open('power_result_table.txt', 'w')

print(f"{'a':>6s}{'a^2':>6s}{'a^3':>6s}", file=file_obj)

for i in range(1, 11):
    print(f"{i:>6d}{i**2:>6d}{i**3:>6d}", file=file_obj)