# quiz_3_3_1.py

while True:
    filename = input("請輸入要寫入的檔名： ")
    range_min = int(input("請輸入數字範圍的最小值： "))
    range_max = int(input("請輸入數字範圍的最小值： "))

    filename += '.csv'
    file_obj = open(filename, 'w')
    print('a', 'a^2', 'a^3', 'a^4', file=file_obj, sep=',')

    for i in range(range_min, range_max+1):
        print(i, i**2, i**3, i**4, file=file_obj, sep=',')

    file_obj.close()
    print(f"檔案 {filename} 已寫入成功！")
    print('=================================')