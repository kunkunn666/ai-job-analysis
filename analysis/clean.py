import pandas as pd

# 读取数据
df = pd.read_csv('./data/ai_jobs_market_2025_2026.csv')

#1.查重复值
print("重复值数量：", df.duplicated().sum())

#删除重复值
df = df.drop_duplicates()

#2.统一薪资字段
df['salary_k_usd'] = df['annual_salary_usd'] / 1000

#3.构造远程工作标签
df['remote_label'] = df['is_remote_friendly'].map({
    1:'Remote',
    0:'On-site'
})

#4.构造LLM岗位标签
df['llm_label'] = df['is_llm_role'].map({
    1:'LLM Role',
    0:'Non-LLM Role'
})

#5.Senior标签
df['senior_label'] = df['is_senior'].map({
    1:'Senior',
    0:'Junior/Mid'
})

#6.薪资等级分类
def salary_level(salary):
    if salary < 150000:
        return 'Low'
    elif salary < 250000:
        return 'Middle'
    else:
        return 'High'
    
df['salary_level'] = df['annual_salary_usd'].apply(salary_level)

#7.保存清洗后的数据
df.to_csv('./data/ai_jobs_market_cleaned.csv', index=False)

print("数据清洗完成!")
print(df.head())