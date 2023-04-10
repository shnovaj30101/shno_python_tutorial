# 3_11_f_string_carry_transform_table.py

print(f"{'Dec':>6s}{'Oct':>6s}{'Hex':>6s}")
print("-----------------------------")

for i in range(101, 121):
    print(f"{i:>6d}{i:>6o}{i:>6x}")
