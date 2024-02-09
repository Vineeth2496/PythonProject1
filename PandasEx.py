import pandas as pd
# mydata={
#     "car":["BMW", "Volvo", "Ford"],
#     "Model":[2024, 2022, 2021]
# }
# myvechile=pd.DataFrame(mydata)
# print(myvechile)

#print(pd.__version__)
# a=[1,7,2]
# #myv=pd.Series(a)
# myv=pd.Series(a, index=['x', 'y', 'z'])
# print(myv)
# print(myv["y"])

# calories={"day1":420, "day2":500, "day3":600}
# #my=pd.Series(calories)
# my=pd.Series(calories, index=["day1", "day2"])
# print(my)

#DataFrame
# data={
#     "calories":[420, 380, 390],
#     "duration":[50, 40, 45]
# }
#df=pd.DataFrame(data)
#print(df)
#refer to row index
#print(df.loc[0])

#use list as indexes
#print(df.loc[[0,1]])
# df=pd.DataFrame(data, index=["day1", "day2",  "day3"])
# print(df)
# print(df.loc["day2"])

df=pd.read_csv("data.csv")
# print(df.to_string())
#print(df)
#print(pd.options.display.max_rows)
# print(df.head())
# print(df.tail())
print(df.info())










