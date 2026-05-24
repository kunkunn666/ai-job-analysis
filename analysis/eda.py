import pandas as pd

# 读取数据
df = pd.read_csv('./data/ai_jobs_market_2025_2026.csv')

# 查看前5行
print(df.head())

# 查看字段信息
print(df.info())

# 查看数值统计
print(df.describe())

# 查看字段名
print(df.columns)