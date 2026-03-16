import pandas as pd
df_csv=pd.read_csv("sample.csv")
print("Data Frame fromm csv:")
print(df_csv)
df_json=pd.read_json("sample.json")
print("\n Data Frame from json:\n",df_json)