import pandas as pd

df = pd.read_csv('hh.csv')

df.drop(28, axis=0, inplace=True)

print(df)