# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KRozanska,11.10.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strFile = ""    # A string that represents the characters in a file
strData = ""    # A row of text data from the file
dicToDo = {}    # The main dictionary
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []   # A list that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have in a text file
# called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
import os
filesize = os.path.getsize(objFile)

if filesize == 0:
    print("You have no items on your ToDo List.")
else:
    strFile = open(objFile, "r")
    print("Current ToDo List:")
    for row in strFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
        dicToDo[strData[0]] = strData[1].strip()
        lstTable.append(dicRow)
        print(dicRow["Task"] + ' - ' + dicRow["Priority"])
    strFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
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
        filesize = os.path.getsize(objFile)
        if filesize == 0 and not lstTable:
            print("You have no items on your ToDo List.")
        else:
            print("ToDo List:")
            for row in lstTable:
                print(row["Task"] + " - " + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strMenu = str(input("What task would you like to add?: ")).strip()
        if strMenu not in dicToDo:
            intPriority = input("What priority would you like to assign it?: ")
            dicToDo[strMenu] = intPriority
            dicRow = {"Task": strMenu, "Priority": intPriority}
            lstTable.append(dicRow)
            print("\nYou have added task \"" + strMenu + "\" with priority \"" + intPriority + "\".")
        else:
            print("\nThat task already exists.")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strMenu = str(input("Which task would you like to remove?: ")).strip()
        if strMenu in dicToDo:
            del dicToDo[strMenu]
            for row in lstTable:
                if row["Task"] == strMenu:
                    lstTable.remove(row)
            print("Your task \"", strMenu, "\" has been removed.")
        else:
            print("\nError. \"" + strMenu + "\" doesn't exist on the list.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        strFile = open(objFile, "w")
        for row in lstTable:
            strFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        strFile.close()
        print("You list has been saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye.")
        break  # and Exit the program
