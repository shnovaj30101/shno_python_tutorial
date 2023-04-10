# 3_13_percent_operator_carry_transform_table.py

print("%6s%6s%6s" % ("Dec", "Oct", "Hex"))
print("-----------------------------")

for i in range(101, 121):
    print("%6d%6o%6x" % (i, i, i))
