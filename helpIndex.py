from colorResources import *
'''
displayHelp
Runs when the user enters the help command. Displays list of possible commands and what they do.
'''

def displayHelp():
    print(f"--- {BLUE}COMMAND LIST{RESET}: ---\n{BLUE}HELP{RESET}: Displays command list\
          \n{BLUE}AVERAGE{RESET}: Find the average of a certain data set (must be numerical).\
                  \n{BLUE}SEARCH{RESET}: Display a certain line of data by the ID.\
                  \n{BLUE}REMOVE{RESET}: Remove a line of data by its ID number.")