ESC = "\033["
RESET = "\033[0m"

RED = ESC + "31m"
BLUE = ESC + "34m"

'''
displayHelp
Runs when the user enters the help command. Displays list of possible commands and what they do.
'''

def displayHelp():
    print(f"--- {BLUE}COMMAND LIST{RESET}: ---\n{BLUE}HELP{RESET}: Displays command list\
          \n{BLUE}QUIT{RESET}: Quits the program. If changes have been made, the updated file can be saved.\
                  \n{BLUE}SEARCH{RESET}: Display a certain line of data by the ID.\
                  \n{BLUE}REMOVE{RESET}: Remove a line of data by its ID number.")