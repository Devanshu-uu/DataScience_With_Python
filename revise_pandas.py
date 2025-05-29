import pandas as pd


# data={
#      "Time":[1,2,3,4,5],
#      "Value":[10,None,30,None,50]




#  }


# df=pd.DataFrame(data)

# df['Value']=df["Value"].interpolate(method='linear')

# print(df)


data = {
    "name": ["Dev", "Gupil", "Piyush", "Simran", "Asha", "Manav", "Anjali"],
    "salary": [40000, 55000, 32000,  60000, 30000, 52000, 41000],
    "age": [22, 22, 19, 19, 19, 30, 21],
    "performance_score": [85, 70, 92, 96, 75, 58, 89]
}

df=pd.DataFrame(data)

# df.sort_values(by=['age','performance_score'] , ascending=[True,False],inplace=True)
# print(df)

# grouped=df.groupby('age')['salary'].sum()
# print(grouped)

grouped=df.groupby(['age','name'])['salary'].sum()
print(grouped)