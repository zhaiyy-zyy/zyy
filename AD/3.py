import csv
import os

# 输入文件路径
csv_file = '3.csv'

# 读取现有的 CSV 文件，修改 'video_name' 为 '0001.mp4' 的行
rows = []
updated = False

# 打开文件读取原数据
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # 获取表头
    header.append('product_name')  # 在表头添加 'product_name' 列

    # 遍历原有数据
    for row in reader:
        # 检查 video_name 是否为 '0001.mp4'
        if row[1] == '0064.mp4':  # 假设 'video_name' 在第二列（index 1）
            row.append('Washing Machine')  # 添加带有一组引号的 'product_name' 字段
            updated = True
        rows.append(row)

# 如果更新了数据，写回文件
if updated:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # 写入表头
        writer.writerow(header)

        # 写入更新后的数据
        writer.writerows(rows)

    print("Data updated successfully!")
else:
    print("No data found for video_name = 0001.mp4.")