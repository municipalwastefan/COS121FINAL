from fileFunctions import *
from helpIndex import *
from colorResources import *
'''
This is the main function of the program. It starts by asking the user for the name of the file they'd like to process.
It checks if the file exists by attempting to open it. If it doesn't, then the user is notified and prompted to enter a 
valid file name. 
Next, the user is asked to enter a command. Entering 'help' displays a list of all possible commands.
'''
def main():
    while True:
        fileInput = input("Hello user! Please declare the name of the csv file to be processed. NOTE: do NOT include the .csv. Input is case sensitive.\n:")
        fileInput = fileInput + ".csv"
        try:
            f = open(fileInput,"r")
            f.close()
            break
        except:
            print("File not found! Please enter a valid file name.")
            continue
    print(f"File {BLUE}{fileInput}{RESET} selected for processing.\nNow initiating file...")
    allPpl = initiate(fileInput)
    #print(allPpl)
    while True:
        commandInput = input("Please enter a command. Enter 'help' for a list of commands.\n:")
        commandInput = commandInput.lower().strip()
        if commandInput == "help":
            displayHelp()
            continue
        elif commandInput == "search":
            searchChoice = input("Enter ID of data set you'd like to be returned.\n:")
            searchChoice = searchChoice.strip()
            idGet(searchChoice, allPpl)
        elif commandInput == "remove":
            removeChoice = input("Enter the ID of the data set you'd like to remove.\n:")
            removeChoice = removeChoice.strip()
            idRemove(removeChoice, allPpl)
        else:
            print("Command not found!")

main()

        