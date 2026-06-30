import pandas as pd
import numpy as np

data = {
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Department':['HR','IT','IT','Marketing',np.nan]  ,
    'Salary':[50000,60000,np.nan,45000,70000] ,
    'Join_year':[2021,2020,2023,2022,2019]
    
}

df=pd.DataFrame(data)
print("---original dataframe---")
print(df)

df['Salary']=df['Salary'].fillna(df['Salary'].mean())
df['Department']=df['Department'].fillna('Unknown')

high_earners=df[df['Salary']>50000]

df['Yoe']=2026-df['Join_year']
avg_sal=df.groupby('Department')['Salary'].mean()

df.to_csv("cleaned_employees.csv",index=False)
loaded_df = pd.read_csv("cleaned_employees.csv")


print("\n---cleaned dataframe---")
print(df)
print("\n---average salary by department---")
print(avg_sal)
print("---loaded df---")
print(loaded_df)