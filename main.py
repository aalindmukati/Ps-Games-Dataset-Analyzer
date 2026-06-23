import pandas as pd
import seaborn as sns
import matplotlib as mat

df = pd.read_csv('Data.csv')
df_sorted = df.sort_values(by='HoursPlayed',ascending=False).reset_index(drop=True) 
print(df_sorted)

# Plotting graph test


ax1.plot(df['Name'],df['HoursPlayed'],color='red',marker='o',linewidth=2.5)
ax1.set_xlabel('Name',fontsize=12)
ax1.set_ylabel('HoursPlayed',fontsize=12)
ax1.tick_param(axis='x',color='blue')
ax1.grid(True,linestyle=':',alpha=0.5)

mat.title('Test Graph')
mat.show()