'''
fileFunctions.py
This
'''

from helpIndex import *

'''
Initiate
Runs automatically after file name is entered and confirmed to exist.
First, it opens the file, and saves its contents to fileContents.
Next, it splits fileContents into a list by each new line. This list is 
saved to fileLines, where the legend is removed and any potential white space
at the end is removed as well. The lists are then sent to createPerson(), and a dictionary
for each line of data is created and added to a list of dictionaries representing the data.
Then the function asks the user if they'd like to print the data. If the answer is "y" the 
csv data is printed, otherwise it is not printed. Then the function returns the list of dictionaries
containing each line of csv data in the form of the variable allPpl.
'''

def initiate(file):
   try:
      file = open(file,"r")
      fileContents = file.read()
      fileLines = fileContents.split("\n")
      fieldLine = fileLines[0]
      fieldLine = fieldLine.split(",")
      fileLines.pop(0)
      while '' in fileLines:
         fileLines.remove('')
      file.close()
      allPpl = []
      for line in fileLines:
         sLine = line.split(",")
         onePerson = createPerson(sLine)
         allPpl.append(onePerson)

      printContents = input("Would you like the print the contents of the file? (Y/N)\n:")
      printContents = printContents.strip().lower()
      if printContents == "y":
         print(allPpl)
      else:
         print()
      print("File initiated and ready for processing!")
      return allPpl
   except:
      print("Unknown file!")

'''
getFieldNames
Runs right after initiate(). It opens the file inputted by the user in the main function, reads it, and saves the
first line of csv data in fieldLine. Then, it splits it by , and saves it as a list in fieldNames and returns that
list to main.
'''
def getFieldNames(file):
   try:
      file = open(file,"r")
      fileContents = file.read()
      fileLines = fileContents.split("\n")
      fieldLine = fileLines[0]
      fieldLine = fieldLine.split(",")
      fieldNames = [fieldLine[0], fieldLine[1], fieldLine[2], fieldLine[3], fieldLine[4], fieldLine[5]]
      return fieldNames
   except:
      print("Unknown file!")
'''
createPerson
This function is called by the initiate function. It takes the lists of csv data generated by initiate() and turns it into
individual dictionaries for each line of data. It is run for each line of csv data already split by commas in the variable
sLine. Then the dictionary for the individual line of data is returned to initiate() in the variable onePerson. For each
line of data, this variable is added to the list of all data called allPpl.
'''

def createPerson(sLine):
   onePerson = {
    "id":sLine[0],
    "first_name":sLine[1],
    "last_name":sLine[2],
    "email":sLine[3],
    "gender":sLine[4],
    "ip_address":sLine[5],
   }
   return onePerson

'''
dataSearch
Runs when the search command is entered and an ID is specified. It starts by setting the data variable to 0. This is so
if there is no data for the user's search input found, the program can know to say that it is not present in the data.
The for loop goes through each person, or individual dictionary in the list updatedPpl, and checks if the 

'''
def dataSearch(field, searchChoice, updatedPpl):
   data = 0

   for person in updatedPpl:
      if person[field].strip() == searchChoice or person[field].strip().lower() == searchChoice:
         data = person
         print(data)
         break
      else:
         continue
   if data == 0:
      print(f"No data found for {field} {BLUE}{searchChoice}{RESET}.")
   
'''
idRemove
Runs when the remove command is entered and an ID is specified. It starts by setting the data variable to 0. This is so
if there is no data for the entered ID found, the program can say that there was nothing to remove. The for loop goes through
all the individual dictionaries in the list updatedPpl and looks for a line with the id matching the user entered one. If it is
found, this is saved to data. Then, this dictionary is removed from the list. The function then announces that this line of
data was removed and asks if they'd like the updated data to be printed. If so, it will be, if not, nothing changes. Either way,
then the updated list of data with the person removed is returned by the function.
'''
def idRemove(id, updatedPpl):
   data = 0

   for person in updatedPpl:
      if person["id"] == id:
         data = person
         updatedPpl.remove(person)
         printNew = input(f"Data corresponding to ID number {BLUE}{id}{RESET} has been removed. Would you like to print updated data list? (Y/N)\n:")
         printNew = printNew.strip().lower()
         if printNew == "y":
            print(updatedPpl)
            break
         else:
            break
      else:
         continue
   if data == 0:
      print(f"No data found for ID number {BLUE}{id}{RESET}.")
   else:
      return updatedPpl

'''
dataAdd
This
'''

def dataAdd(inputList, updatedPpl):
   newDataLine = {}
   # newDataId = int(updatedPpl[-1]['id']) + 1
   newDataLine["id"] = int(updatedPpl[-1]['id']) + 1
   newDataLine["first_name"] = inputList[0]
   newDataLine["last_name"] = inputList[1]
   newDataLine["email"] = inputList[2]
   newDataLine["gender"] = inputList[3]
   newDataLine["ip_address"] = inputList[4]
   print(newDataLine)
   updatedPpl.append(newDataLine)


   return newDataLine


