#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# J. Byrne, 2021-Aug-8, Rev A - Change to LIST of Dictionaries.  NO FUNCTIONS
#----cont'd----> Add ability to load existing data.  Add ability to delete entry
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # dictionary for data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        
        for row in objFile:
            output = row.strip().split(',')
            dicRow = {'CD ID': int(output[0].strip()), 'CD Title':output[1].strip(), 'CD Artist':output[2].strip()}
            lstTbl.append(dicRow)
        
        objFile.close()
        pass
    
    
    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'CD ID': intID, 'CD Title':strTitle, 'CD Artist':strArtist}
        lstTbl.append(dicRow)
        print('\n')
        
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            cd_id = row['CD ID']
            cd_title = row['CD Title'].strip()
            cd_artist = row['CD Artist'].strip()
            print(cd_id, cd_title, cd_artist, sep = ', ')
        print('\n')
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry        
        print('ID, CD Title, Artist')
        for row in lstTbl:
            cd_id = row['CD ID']
            cd_title = row['CD Title'].strip()
            cd_artist = row['CD Artist'].strip()
            print(cd_id, cd_title, cd_artist, sep = ', ')
        print('\n')
        row_del = input("Enter ID of row to delete:  ")
    
        x = 0
        row_del = int(row_del)
        for row in lstTbl:
            if row['CD ID'] == row_del:
                del lstTbl[x]
                x += 1
            else:
                x += 1
        print('\n')
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = str(row['CD ID']) + ', ' + row['CD Title'] + ', ' + row['CD Artist'] + '\n'
            objFile.write(strRow)
        objFile.close()
        lstTbl = []
        
        
    else:
        print('Please choose either l, a, i, d, s or x!')

