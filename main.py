import pandas as pd
import seaborn as sns
import matplotlib as mat

df = pd.read_csv('Data.csv')
df_sorted = df.sort_values(by='HoursPlayed',ascending=False)
print(df_sorted)