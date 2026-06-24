import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mat

df = pd.read_csv('Data.csv')
df_sorted = df.sort_values(by='HoursPlayed',ascending=False).reset_index(drop=True) 
print(df_sorted)


print('--------------------------------------------------------')

# Plotting graph test
def games_vs_hours_line(): # GVH mean games vs hours graph
    fig,ax1 = mat.subplots(figsize =(15,6))


    ax1.plot(df['Name'],df['HoursPlayed'],color='red',marker='o',linewidth=2.5)
    ax1.set_xlabel('Game Name',fontsize=12)
    ax1.set_ylabel('HoursPlayed',fontsize=12)
    ax1.tick_params(axis='x',color='blue')
    ax1.grid(True,linestyle=':',alpha=0.5)
    

    mat.title('Line Graph')
    mat.show()

def games_vs_hours_bar(): #games played vs hours they are played
    fig,ax1 = mat.subplots(figsize =(15,6))

    ax1.bar(df['Name'],df['HoursPlayed'],width=0.8,bottom=None,align='center',color='purple')
    ax1.tick_params(axis='x',labelrotation=90)
    mat.subplots_adjust(bottom=0.3)

    mat.title('Bar Graph')
    mat.show()

def pie(): #Genre Distribution
    fig,ax1 = mat.subplots(figsize=(15,6))
    tt = df['Genre'].value_counts()
    
    ax1.pie(tt.values, labels=tt.index.to_list())

    mat.title('Pie Chart')
    mat.show()


choice = int(input('What would u like to see ?\n 1.LineGraph(press_1)\n 2.BarGraph(press_2)\n 3.PieChart(press_3)\n'))

if choice == 1:
    games_vs_hours_line()
elif choice == 2:
    games_vs_hours_bar()
elif choice == 3:
    pie()
else:
    print('what broo')