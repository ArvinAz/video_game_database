print("Hello world")
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os
import csv
api = KaggleApi()
api.authenticate()
#Check if file exists
if(os.path.isfile('./games.csv') != true){
    api.dataset_download_file('arnabchaki/popular-video-games-1980-2023', file_name='games.csv')
}
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
    

def dataMenu():
    print("This is data menu")
    print("Click on 5 to go back to main menu")
    x4 = input()
    if x4.isnumeric():
        if int(x4) == 5:
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

    
    
