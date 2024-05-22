import pandas as pd

data = pd.read_csv('dz.csv')

average_salary_by_city = data.groupby('City')['Salary'].mean().reset_index()

print(average_salary_by_city)
