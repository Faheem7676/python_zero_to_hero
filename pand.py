import pandas as pd
import difflib



df=pd.read_csv("/home/faheem/Desktop/python_zero_to_hero/testdata.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df["email"])

print(df[["email","captcha"]])
print(df.columns)

df.rename(columns={"password":"Age"},inplace=True)
print(df["Age"])

print(df["email"])
print(df["Age"])
print(df["captcha"])

print(df.columns)

print(df.head())
print(df.sample())

df=pd.read_csv("/home/faheem/Desktop/python_zero_to_hero/testdata.csv")
print(df)

close_matches=difflib.get_close_matches("Age",df.columns)

print(close_matches)


