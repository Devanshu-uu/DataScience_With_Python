import pandas as pd
# data = {
# 'company': ['TCS', 'TCS', 'Infosys', 'Wipro', 'Infosys', 'TCS', 'Wipro', 'IBM'],
# 'name': ['Dev', 'Gupil', 'Piyush', 'Simran', 'Ravi', 'Asha', 'Manav', 'Anjali'],
# 'sales': [12000, 15000, 18000, 11000, 14000, 16000, 10000, 19000]
# }

# df=pd.DataFrame(data)
# print(df)

# groupby_sum=df.groupby('name')['sales'].sum()
# print(groupby_sum)

# groupbysales=df.groupby('company')['sales'].agg(['sum','count','mean'])
# print(groupbysales)

# mean=df.groupby('company')['sales'].mean()
# print(mean)


# max=df.groupby('company')['sales'].max()
# min=df.groupby('company')['sales'].min()
# print(min)
# print(max)


# discribe=df.groupby('company')['sales'].describe()
# print(discribe)

# all=df.groupby('company').agg(
#     total_sales=('sales', 'sum'),
#     avg_sales=('sales', 'mean'),
#     employee_count=('name', 'count')
# )

# print(all)

# pivort_table=pd.pivot_table(df,values='sales',index='name',columns='company',aggfunc='sum',fill_value=0)
# print(pivort_table)

df=pd.read_excel('survey.xls')
print(df)

crosstab = pd.crosstab(df['Sex'],df['Handedness'], values=df['Age'],aggfunc='sum')
print(crosstab)
