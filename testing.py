print("Hello world")

import os
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