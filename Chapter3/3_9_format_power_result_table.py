# 3_9_format_power_result_table.py

print("{:>6s}{:>6s}{:>6s}".format('a', 'a^2', 'a^3'))

for i in range(1, 11):
    print("{:>6d}{:>6d}{:>6d}".format(i, i**2, i**3))
