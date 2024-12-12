import csv
from fileFunctions import *
from helpIndex import *
'''
This is the main function of the program. It starts by asking the user for the name of the file they'd like to process.
It checks if the file exists by attempting to open it. If it doesn't, then the user is notified and prompted to enter a 
valid file name. 
Next, the user is asked to enter a command. Entering 'help' displays a list of all possible commands.
If the user inputs a valid command other than help, it calls its respective function, listed in fileFunctions.
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
    updatedPpl = allPpl
    wasEdited = False
    while True:
        commandInput = input("Please enter a command. Enter 'help' for a list of commands.\n:")
        commandInput = commandInput.lower().strip()
        if commandInput == "help":
            displayHelp()
            continue
        elif commandInput == "print":
            print(updatedPpl)
        elif commandInput == "search":
            searchChoice = input("Enter ID of data set you'd like to be returned.\n:")
            searchChoice = searchChoice.strip()
            idGet(searchChoice, updatedPpl)
        elif commandInput == "remove":
            removeChoice = input("Enter the ID of the data set you'd like to remove.\n:")
            removeChoice = removeChoice.strip()
            updatedPpl = idRemove(removeChoice, updatedPpl)
            wasEdited = True
        elif commandInput == "quit":
            if wasEdited == False:
                quit()
            else:
                quitResp = input("You have made changes to the data. Would you like to save these to a new file? (Y/N)\n:")
                quitResp = quitResp.lower().strip()
                if quitResp == "y":
                    fieldNames = ["id", "first_name", "last_name", "email", "gender", "ip_address"]
                    with open("UPDATED_DATA.csv","w",newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
                        writer.writeheader()
                        writer.writerows(updatedPpl)
                        f.close()
                quit()
        else:
            print("Command not found!")

main()

        