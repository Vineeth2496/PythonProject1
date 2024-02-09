import pandas as pd


df=pd.read_csv("details.csv")
print(df["Marks"].mean())