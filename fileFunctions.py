from helpIndex import *

'''
Initiate
Runs automatically after file name is entered and confirmed to exist.
First, it opens the file, and saves its contents to fileContents.
Next, it splits fileContents into a list by each new line. This list is 
saved to fileLines, where the legend is removed and any potential white space
at the end is removed as well. 
'''

def initiate(file):
   try:
      file = open(file,"r")
      fileContents = file.read()
      fileLines = fileContents.split("\n")
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
idGet
Runs when the search command is entered and an ID is specified.
'''
def idGet(id, updatedPpl):
   data = 0

   for person in updatedPpl:
      if person["id"] == id:
         data = person
         print(data)
         break
      else:
         continue
   if data == 0:
      print(f"No data found for ID number {BLUE}{id}{RESET}.")
   
'''
idRemove
Runs when the remove command is entered and an ID is specified.
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



