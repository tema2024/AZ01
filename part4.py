import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

df.fillna(0, inplace=True)

print(df)

df.dropna(inplace=True)
print(df)