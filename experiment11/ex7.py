import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','San Fransisco','Los angels']
}
df=pd.DataFrame(data)
print("DataFrame")
print(df)
print("\n Age column")
print(df['Age'])
print("\n Row at index1:")
print(df.iloc[1])