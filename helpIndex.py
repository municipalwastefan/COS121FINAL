'''
helpIndex.py
This file contains the code for the formatting of the help index. It also has the variables containing escape codes for
coloring the text.
'''

ESC = "\033["
RESET = "\033[0m"

RED = ESC + "31m"
BLUE = ESC + "34m"

'''
displayHelp
Runs when the user enters the help command. Displays list of possible commands and what they do. This is done mainly to avoid
cluttering the main() function in main.py.
'''

def displayHelp():
    print(f"--- {RED}COMMAND LIST{RESET}: ---\n{BLUE}HELP{RESET}: Displays command list\
          \n{BLUE}QUIT{RESET}: Quits the program. If changes have been made, the updated file can be saved.\
          \n{BLUE}PRINT{RESET}: Prints the data of the file currently being process in the terminal.\
                  \n{BLUE}SEARCH{RESET}: Display a certain line of data by the ID.\
                  \n{BLUE}REMOVE{RESET}: Remove a line of data by its ID number.\
                  \n{BLUE}ADD{RESET}: Add a new line of data by each field")