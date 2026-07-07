import pandas as pd
import csv
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
    ax1.tick_params(axis='x',color='blue',labelrotation=90)
    ax1.grid(True,linestyle=':',alpha=0.5)
    

    mat.title('Hours per game')
    mat.show()

def games_vs_hours_bar(): #games played vs hours they are played
    fig,ax1 = mat.subplots(figsize =(15,6))

    ax1.bar(df['Name'],df['HoursPlayed'],width=0.8,bottom=None,align='center',color='purple')
    ax1.tick_params(axis='x',labelrotation=90)
    mat.subplots_adjust(bottom=0.3)

    mat.title('Hours per game')
    mat.show()

def pie(): #Genre Distribution
    fig,ax1 = mat.subplots(figsize=(15,7))
    tt = df['Genre'].value_counts()
    
    ax1.pie(tt.values, labels=tt.index.to_list())

    mat.title('Pie Chart')
    mat.show()

def Sctr(): #Scatter graph
    fig,ax1 = mat.subplots(figsize=(15,6))
    for index, row in df.iterrows():
        ax1.text(
        row["Genre"],
        row["PersonalRating"],
        row["Name"]
    )
    sns.scatterplot(x='Genre',y='PersonalRating',data=df,palette='hot')

    mat.title('Genre vs Rating')
    mat.show()

def Pair():
    sns.pairplot(df,hue='Genre',diag_kind='kde')
    mat.suptitle('PLOS')
    mat.show()
    

def Input_Games():
    global df 
    
    Name = input('Enter the Game name ').title()
    Genre = input('Enter the Genre ').title()
    HoursPlayed = int(input('Enter the Hours played or playing '))
    PersonalRating = float(input('How much would u rate it out of 10 '))

    new_game = {
        "Name": Name,
        "Genre": Genre,
        "HoursPlayed": HoursPlayed,
        "PersonalRating": PersonalRating
    }

    new_game_df = pd.DataFrame([new_game]) #conv3rting dictionary to data frame
    df = pd.concat([df, new_game_df], ignore_index=True) #concat() simply stacks the dictionary data to pre existing df, ignore_index=True creates fresh numbering.

    df.to_csv("Data.csv", index=False) #This saves your updated dataframe back into the CSV.

    print("\nGame Added Successfully!")


choice = int(input(
'''What would u like to see?

1. Games vs Hours Played [Line]
2. Games vs Hours Played [Bar]
3. Genre Distribution [Pie]
4. Genre vs Rating [Scatter]
5. Pair-plot
6.
7. Add New Game

Choice = '''
))

if choice == 1:
    games_vs_hours_line()
elif choice == 2:
    games_vs_hours_bar()
elif choice == 3:
    pie()
elif choice == 4:
    Sctr()
elif choice == 5:
    Pair()
elif choice == 6:
    Input_Games()
else:
    print('what broo')