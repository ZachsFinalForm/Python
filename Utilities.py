def clearScreen():
        import os
        os.system('cls')

def TempConversion():
        line = "You are currently running a Temperature converter.\nEnter 'FtoC' to convert Fahrenheit to Centegrade or 'CtoF' to do the opposite"
        print(line)

'''        
    line = "You are currently running a Temperature converter. \nEnter 'FtoC' to convert Fahrenheit \
                        to Centigrade or 'CtoF' to cconvert Centigrade to Fahrenheit
    print(line)
'''

def FtoC(value):
    line = "Your converted Centigrade value is: " + str(value)
    print(line)
    print("Thank You Good Bye")


def CtoF(value):
    line = "Your converted Fahrenheit value is: " + str(value)
    print(line)
    print("Thank You Good Bye")

def PrintAList(theList):
    for i in theList:
        print(i)
    print("\n")         # \ is the escape charactor

def PrintEveryOtherListMember(theList):
        ll = len(theList)
        for i in range(0, 11, +2):
            if (i < ll):
                print(theList[i])
            else:
                pass

def readABaseBallCSV(fileName):
    FO=open(fileName, 'r')
    theList = FO.readlines()
    FO.close()
    for i in range(len(theList)):
        theList[i] = theList[i].replace('\n','')
    return theList


def readsFileIntoListRCRLF(theFile):
    def removeCRLF(tempList):
        count = 0
        for i in range(0,len(tempList)):
            tempList[i] = tempList[i].replace('\n','')
        return tempList
    with open(theFile, 'r') as file:
        theList = file.readlines()
    theList = removeCRLF(theList)
    return theList

def dumpToFileAString(name, theString):
    fO = open(name, 'w')
    fO.write(theString)
    fO.close()
    
def dumpListToAFile(theList, name):   # this is more for test
    fO = open(name, 'w') 
    for i in range(0, len(theList)):
        fO.write(theList[i])
        fO.write('\n')
    fO.close()

def dumpListToAFileA(theList, name):   # this is more for test
    fO = open(name, 'a') 
    for i in range(0, len(theList)):
        fO.write(theList[i])
        fO.write('\n')
    fO.close()             


'''
def readsFileIntoListRCRLF(theFile):
    def removeCRLF(tempList):
        count = 0
        for i in range(0,len(tempList)):
            tempList[i] = tempList[i].replace('\n','')
        return tempList
    with open(theFile, 'r') as file:
        theList = file.readlines()
    theList = removeCRLF(theList)
    return theList
'''
'''
def dumpToFileAString(name, theString):
    fO = open(name, 'w')
    fO.write(theString)
    fO.close()
'''

'''
    
def dumpListToAFile(theList, name):   # this is more for test
    fO = open(name, 'w') 
    for i in range(0, len(theList)):
        fO.write(theList[i])
        fO.write('\n')
    fO.close()
'''
'''

def dumpListToAFileA(theList, name):   # this is more for test
    fO = open(name, 'a') 
    for i in range(0, len(theList)):
        fO.write(theList[i])
        fO.write('\n')
    fO.close()             
'''
# opens a file
myfile = open("Python Week1 Code.txt", "rt")
contents = myfile.read()
myfile.close()
print(contents)

# temp convert FtoC
temp =input("Input Temperature Here:")
temp = int(temp)
finalTemp = int(temp)-32*5/9
print ("Today's temperature is",(finalTemp))

#temp convert CtoF
temp =input("Input Temperature Here:")
temp = int(temp)
finalTemp = int(temp *9/5)+32
print ("Today's temperature is",(finalTemp))

# dollar to euro
currency = input ("Dollars:")
currency = (int(currency))
currency = (currency*.8906)
print (currency)

# A-euro to dollar B-dollar to euro
print("Currency Converter")
print("Please Type A or B to make your selection.")
convert = str(input ("A-Euros to Dollars B-Dollars to Euros"))
if convert == "A":
    etd = float(input("How much would you like to convert: "))
    f = etd * 1.12
    f2 = round(f,2)
    print("it is $",f2)
if convert == "B":
    etd = float(input("How much would you like to convert: "))
    f = etd * .89
    f2 = round(f,2)
    print("it is €",f2)

#file reader
    input('Press enter to continue.')
fO = open("Conversion.csv",'r') # Opens Conversion file
conversion = fO.readlines()
fO.close()
fO = open('Quantity.csv','r') # Opens Quantity file
quantity = fO.readlines()
fO.close()

for i in range(len(quantity)):
    quantity[i]=quantity[i].replace('\n','') 

#Prints out column headers of the conversion .csv file
headers = conversion[0].split(',')
position = 0
for i in headers:
    print(str(position) + ' -- ' + i)
    position = position + 1

#Prints a statement showing the value of the initial currency and what it is worth in another currency
for i in range(1, len(conversion)):
    conversionList = conversion[i].split(',')
    convertedValue = float(quantity[0]) * float(conversionList[0])
    print(quantity[0] + ' USD is worth ' + str(convertedValue) + ' ' + conversionList[1])

input('Press enter to continue.')

