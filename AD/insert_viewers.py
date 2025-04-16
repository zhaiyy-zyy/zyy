import csv
import sqlite3
from datetime import datetime

# 连接到SQLite数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('advertisements.db')
cursor = conn.cursor()

# 创建viewers表（如果表不存在）
cursor.execute('''
CREATE TABLE IF NOT EXISTS viewers (
    viewer_id SERIAL PRIMARY KEY,
    demographics_id INT NOT NULL,
    ad_id INT NOT NULL,
    view_time INT NOT NULL,
    visit_date DATE NOT NULL
)
''')

# 读取CSV文件并插入数据
with open('22.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # 将visit_date转换为SQLite支持的日期格式
        visit_date = datetime.strptime(row['visit_date'], '%Y-%m-%d').date()
        
        # 插入数据到viewers表
        cursor.execute('''
        INSERT INTO viewers (demographics_id, ad_id, view_time, visit_date)
        VALUES (?, ?, ?, ?)
        ''', (row['demographics_id'], row['ad_id'], row['view_time'], visit_date))

# 提交事务并关闭连接
conn.commit()
conn.close()

print("数据已成功插入到viewers表中。")