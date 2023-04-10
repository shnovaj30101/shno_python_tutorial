# 3_8_f_string_power_result_table.py

print(f"{'a':>6s}{'a^2':>6s}{'a^3':>6s}")

for i in range(1, 11):
    print(f"{i:>6d}{i**2:>6d}{i**3:>6d}")
