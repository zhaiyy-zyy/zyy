import csv
import json

csv_file = "ads.csv"  # 替换为你的 CSV 文件名
json_file = "ads.json"

data = []
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print(f"CSV 数据已成功转换为 JSON 文件：{json_file}")