import pandas as pd

# read = pd.read_csv("sales_data_sample.csv",encoding="latin1")

# read = pd.read_excel("SampleSuperstore.xlsx")

# read = pd.read_json("sample_Data.json")
# print(read)


data= {
    "Name":['Dev','gupil','piyush'],
    "Age":[20,22,14],



}

# dt= pd.DataFrame(data)
# # print(dt)

# print(dt.head(1))

# dt.to_csv("output.csv",index=False)
# dt.to_excel("output.xlsx") 
# dt.to_json("output.json")

read = pd.read_json("sample_Data.json")

# print("First ten rows")
# print(read.head(10))


# print("Second ten rows")
# print(read.tail(10))

# print("First 5 rows")
# print(read.head())


# print("Second 5 rows")
# print(read.tail())


print("Display The Info")

print(read.info())

print("Discripton of Data")
print(read.describe())

data=pd.read_json("sample_Data.json")
print(f'Shape: {data.shape}')
print(f'column: {data.columns}')

print(data['name'])

coloums= data[["name", "price"]]
print(coloums)



# high_prices= data[data["price"]>500]

# print(high_prices)

# print(data['category'])

# high_values= data[(data["price"]>500) & (data["price"]< 900)]

# print(high_values)

# high_values= data[(data["price"]<200) | (data["category"]== "Home & Kitchen")]

# print(high_values)

data = {
    "name": ["Dev", "Gupil", "Piyush", "Simran", "Asha", "Manav", "Anjali"],
    "salary": [40000, 55000, 32000,  60000, 30000, 52000, 41000],
    "age": [22, 25, 19, 26, 21, 30, 24],
    "performance_score": [85, 70, 92, 96, 75, 58, 89]
}

df=pd.DataFrame(data)
# print(df)

# df['bonus']= df["salary"] * 0.1
# print(df)

# df.insert(0,"Employ ID", [10,20,30,40,50,60,70])

# print(df)

# df["salary"]= df["salary"]* 1.05

# df.loc[0,"salary"]=30000
# print(df)



# df.loc[0,"performance_score"]=45
# print(df)

# df.drop(columns=["performance_score"], inplace=True)
# print(df)

print(df.isnull())


print(df.isnull().sum())

# df.dropna(inplace=True)

# df.fillna(0,inplace=True)

# df["age"].fillna (df["age"].mean(),inplace=True )

# df["salary"].fillna(df["salary"].mean(),inplace=True)

# df["performance_score"].fillna(df["performance_score"].mean(),inplace=True)
# print(df)


data1={

    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]

}


df1=pd.DataFrame(data1)

# print(df1)

# df1["Value"]=df1["Value"].interpolate(method="linear")

# # print(df1)


# df.sort_values(by="age",ascending=False,inplace=True)



df.sort_values(by="age",ascending=True,inplace=True)
df.sort_values(by=["age","salary"],ascending=[True,True],inplace=True)
print(df)

# avg_salary=df["salary"].mean()
# print(avg_salary)

# min_salary=df["salary"].min()
# print(min_salary)

# sum_salary=df["salary"].sum()
# print(sum_salary)

# max_salary=df["salary"].max()
# print(max_salary)


group=df.groupby("age")["salary"].sum()
print(group)

group=df.groupby(["age","name"])["salary"].sum()
print(group)


df_customers=pd.DataFrame({

    "id":[1,2,3],
    "name":["ramesh","suresh","mukesh"]

})


df_orders=pd.DataFrame({

    "id":[1,2,4],
    "orders":[220,129,344]

})


print("from Here")

df_merge=pd.merge(df_customers,df_orders,on="id",how="inner")
# print(df_merge)


df_merge=pd.merge(df_customers,df_orders,on="id",how="outer")
print(df_merge)


df_merge=pd.merge(df_customers,df_orders,on="id",how="left")
print(df_merge)


df_merge=pd.merge(df_customers,df_orders,on="id",how="right")
print(df_merge)



df_region1=pd.DataFrame({

    "id":[1,2,3],
    "name":["ramesh","suresh","mukesh"]

})


df_region2=pd.DataFrame({

    "id":[1,2,4],
    "name":["manu","panu","janu"]})



data_conta=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)

print(data_conta)

data_conta=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)

print(data_conta)

import pandas as pd

ages = [15, 47, 56, 23, 78, 90]        # Use '=' instead of space
bins = [12, 30, 70, 95]                # Use '=' instead of '-'

categories = pd.cut(ages, bins)        # Use '=' instead of space
print(categories)
