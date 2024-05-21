import pandas as pd

df = pd.read_csv('imdb-movies-dataset.csv')

print(df)
print(df.head())
print(df.info())
print(df.describe())


