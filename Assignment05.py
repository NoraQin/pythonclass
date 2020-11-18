# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog
# RRoot,1.1.2030,Created started script
# qinlaura,11/17/2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
file = open(objFile, 'r')
for row in file:
    listRow = row.split(',')
    dicRow = {'Task':listRow[0], 'Priority':listRow[1].strip()}
    lstTable.append(dicRow)
file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for item in lstTable:
            print(f"Task: {item['Task']} | Priority: {item['Priority']}")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('Enter a task: ')
        priority = input('Enter a priority: ')
        lstTable.append({'Task':task, 'Priority':priority})
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print('Here\'s what you have in your list:')
        for i in range(0, len(lstTable)):
            dicRow = lstTable[i]
            print(f"    Item {i+1} | Task: {dicRow['Task']} | Priority: {dicRow['Priority']}")
        while True:
            strChoice = input('Which item would you like to delete? (Enter "x" to cancel)')
            if strChoice.lower() == 'x':
                break
            try:
                del lstTable[int(strChoice)-1]
                print('Item deleted')
                break
            except:
                print('Invalid entry')
                continue
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        file = open(objFile, 'w')
        for item in lstTable:
            file.write(item['Task'] + ',' + item['Priority'] + '\n')
        file.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
    else:
        print('Invalid entry')
