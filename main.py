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


choice = int(input('What would u like to see ?\n 1.Games vs Hours Played[line](press_1)\n 2.Games vs Hours Played[bar](press_2)\n 3.Genre(press_3)\n 4.Input Games(press_4) \n Choice = '))

if choice == 1:
    games_vs_hours_line()
elif choice == 2:
    games_vs_hours_bar()
elif choice == 3:
    pie()
elif choice == 4:
    Input_Games()
else:
    print('what broo')