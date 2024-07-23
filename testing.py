print("Hello world")
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os
import csv
import pandas as pd
api = KaggleApi()
api.authenticate()
#Check if file exists
if os.path.isfile('./games.csv') != True:
    api.dataset_download_file('arnabchaki/popular-video-games-1980-2023', file_name='games.csv')
else:
    print("File already exists")

with zipfile.ZipFile('games.csv.zip', 'r') as zipref: zipref.extractall()
work = True

#functions 
def mainMenu():
    print("Welcome to Video Game project.")
    print("Press 1 to view data")
    print("Press 2 to open developer commands")
    print("Enter Q to quit")
    x1 = input()
    if x1.isnumeric():
        if int(x1) == 1:
            dataMenu()
        elif int(x1) == 2:
            devMenu()
        else:
            work = False
    else:
        quiteCheck(x1)

        print("ERROR: input is a string")
        
    


def devMenu():
    print("Press 1 to launch Firefox.")
    print("Press 2 to launch Chrome.")
    print("Press 3 to launch Notepad.")
    print("Press 4 to launch Jupyter Notebook.")
    print("Click on 5 to go back to main menu")
    x3 = input()
    if x3.isnumeric():
        if int(x3) == 1:
            os.system("start firefox")
        elif int(x3) == 2:
            os.system("start chrome")
        elif int(x3) == 3:
            os.system("start notepad")
        elif int(x3) == 4:
            os.system("start jupyter notebook")
        elif int(x3) == 5:
            mainMenu()
        else: work = False
    else:
        quiteCheck(x3)
    
#Search for data
def searchData():
     search_Input = input("Please enter the game you want to find: ")
     isFound = False
     if(str(search_Input)== "Q" or str(search_Input)== "q"):
        dataMenu()
     else:
         datagames = []

         with open("games.csv", encoding="utf8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    datagames.append(row)
         #print(row)
         #col = [x[1] for x in datagames]
         col = [games for games in datagames]
         col = [x[1] for x in col]
         count = 0
         for title in col:
            count = count + 1
            if search_Input in title:
                isFound = True
                print(str(count) + ": " + title)
                
         if(isFound == False):
             print("Error: Game does not exist")
             searchData()

         


#Data menu
def dataMenu():
    print("This is data menu")
    print("Type 1 to see data")
    print("Type 2 to search for game description")
    print("Type 5 to go back to main menu")
    x4 = input()
    if x4.isnumeric():
        if int(x4) == 1:
            df = pd.read_csv('games.csv')
            print(df['Title'])
            print(df.iloc[0])
        elif int(x4) == 2:
            searchData()
        elif int(x4) == 5:
            mainMenu()
    else:
        quiteCheck(x4)

#Checks if the user wants to quit
def quiteCheck(isquit):
    if isquit == "Q" or isquit == "q":
        print("Quiting")
        quit()
    else:
        print("ERROR: Input is a string value")
    


x1 = 0
while(x1 != "q" or x1 != "Q"):
    mainMenu()
    x1 = input()

    
    
