import pandas as pd

# 读取清洗后的数据
df = pd.read_csv('./data/ai_jobs_market_cleaned.csv')

print("=" * 50)
print("AI岗位薪资分析")
print("=" * 50)

#1.平均薪资最高的岗位
job_salary = (
    df.groupby('job_title')['annual_salary_usd']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n平均薪资最高的10个岗位：")
print(job_salary)

#2.平均薪资最高的国家
country_salary = (
    df.groupby('country')['annual_salary_usd']
    .mean()
    .sort_values(ascending=False)
)

print("\n平均薪资最高的10个国家：")
print(country_salary.head(10))

#3.LLM岗位 vs 非LLM岗位
llm_salary = (
    df.groupby('llm_label')['annual_salary_usd']
    .mean()
)

print("\nLLM岗位 vs 非LLM岗位的平均薪资：")
print(llm_salary)

#4.Remote岗位分析
remote_salary = (
    df.groupby('remote_label')['annual_salary_usd']
    .mean()
)

print("\n远程岗位薪资分析：")
print(remote_salary)

#5.学历薪资分析
education_salary = (
    df.groupby('education_required')['annual_salary_usd']
    .mean()
    .sort_values(ascending=False)
)

print("\n学历薪资分析：")
print(education_salary)

#6.Senior薪资分析
senior_salary = (
    df.groupby('senior_label')['annual_salary_usd']
    .mean()
)

print("\nSenior薪资分析：")
print(senior_salary)
