from validationfunctions import *

#files from https://github.com/solita/dev-academy-2023-exercise

def validations(file1,file2,file3,file4):
   

    toReadFiles=[file1,file2,file3,file4]
    journeyFiles=[file1,file2,file3]

    #checking if file exists or if its not empty

    for file in toReadFiles:
        print(file)
        checkFileExists(file)
        getCsvFile(file)
        checkFileNotEmpty(file)
      
#validating the csv files for journeys
    validateJourneyCoulmnNames(journeyFiles)

    validationJourneyTotalColumns(journeyFiles)
    print()
    for file in journeyFiles:
        print(file)
    
        validateTimeDateValues(file)
        validateIntegerValues(file)
        validateFloat(file)
        validateStringValues(file) 
        print()

# validating the stations csv file
    print(file4)
    validationStationsIntegers(file4)
    validationStationsFloat(file4)
    validationStationsString(file4)
