import pandas as pd
import seaborn as sns
import matplotlib as mat

df = pd.read_csv('Data.csv')

sorted = df.sort_values('Data.csv')
print(sorted)