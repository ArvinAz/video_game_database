from pynput.keyboard import Key, Listener

my_dict = {
    1: 'apple',
    2: 'banana',
    3: 'cherry',
    4: 'date',
    5: 'elderberry',
    6: 'fig',
    7: 'grape',
    8: 'honeydew',
    9: 'kiwi',
    10: 'lemon',
    11: 'mango',
    12: 'nectarine',
    13: 'orange',
    14: 'pear',
    15: 'quince'
}

def reviewMenu(searchResults, page):
    print(searchResults)
    dict={}
    count = 0
    print("SELECT WHICH TO PICK GAME REVIEWS")

    # TODO: Make the for loop run and get certain items depending on the page parameter.
    #Example: 1 = 0-5; 2 = 6-11;
    #Inserting data in
    for x in searchResults:
        
        dict[count] =  searchResults.get(x)
        count += 1 
  
    #    print(str(i) + " : " +dict.get(i))
        def show(key):
        
            print('\nYou Entered {0}'.format( key))
         
            if key == Key.right:
                reviewMenu(searchResults, page + 1)
            elif key == Key.left:
                reviewMenu(searchResults, page - 1)  
            elif key == Key.esc:
                return False   

    i = 1 + (page *   6)
    #print(str(i). str(len(dict)))
    '''''''''
    if(i > len(dict)):
        print("OUT OF SCOPE")
    print("Page " + str(page + 1))
    for i  in range(i+4):
        print(str(i) + " : " + dict.get(i))    
    '''''''''
    while(i < len(dict)):
        for i  in range(i+4):
            print(str(i) + " : " + dict.get(i))   

    with Listener(on_press = show) as listener:   
        listener.join() 
reviewMenu(my_dict, 0)