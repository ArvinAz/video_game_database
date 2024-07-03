print("Hello world")
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os
api = KaggleApi()
api.authenticate()
#Check if file exists
if(os.path.isfile('./games.csv') != true){
    api.dataset_download_file('arnabchaki/popular-video-games-1980-2023', file_name='games.csv')
}
with zipfile.ZipFile('games.csv.zip', 'r') as zipref: zipref.extractall()
work = True
while(work == True):
    print("Press 1 to launch Firefox.")
    print("Press 2 to launch Chrome.")
    print("Press 3 to launch Notepad.")
    print("Press 4 to launch Jupyter Notebook.")
    x = int(input())
    if x == 1:
        os.system("start firefox")
    elif x == 2:
        os.system("start chrome")
    elif x == 3:
        os.system("start notepad")
    elif x == 4:
        os.system("start jupyter notebook")
    else: work = False