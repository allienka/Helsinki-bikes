import pandas as pd
import numpy as np
import os.path
from csvvalidator import *
#from datetime import datetime

def checkFileExists(file):
    if os.path.isfile(file)==True:
        print("CSV File exists OK")
    else:
        print("The CSV file does not exist")    
def checkFileNotEmpty(file):
    df=getCsvFile(file)
    if df.empty==True:
        print("File is empty")
    else:
        print("File OK")

def getCsvFile(file):
    df=pd.read_csv(file)
    return df

def getColumnNames(file): 
    df=pd.read_csv(file)
    return(df.columns.values)

def validateJourneyCoulmnNames(journeyfiles): # comparing if all the csv files for journeys have the same values
    
    a=getColumnNames(journeyfiles[0])
    b=getColumnNames(journeyfiles[1])
    c=getColumnNames(journeyfiles[2])

    if (np.array_equal(a,b)==True and np.array_equal(a,c)==True):
        print("Column values OK") 
    else:
        print("There are not the same columns names in the files")    


def validationJourneyTotalColumns(journeyFiles):   #if journey csv files have the same amount of columns
    array=[]
    for file in journeyFiles:
        totalCols=len(getColumnNames(file))
        array.append(totalCols)
    if (array[0]==array[1] and array[0]==array[2]):
        print("Amount of columns OK")   
    else:
        print("Files dont have the same amount of columns")

def validateTimeDateValues(file):
    df=getCsvFile(file)
    validationDeparture=pd.to_datetime(df["Departure"], errors='coerce').notnull().all()
    validationReturn=pd.to_datetime(df["Return"], errors='coerce').notnull().all()
    
    if validationDeparture==False:
        print("Departure must be timedate")
    elif validationReturn==False:
        print("Return must be timedate")
    else:
        print("Timedates OK")
    
def validateIntegerValues(file):
    df=getCsvFile(file)

    validationDepartureStationId=pd.to_numeric(df['Departure station id'], errors='coerce').notnull().all()
    validationReturnStationId=pd.to_numeric(df['Return station id'], errors='coerce').notnull().all()
    validationDuration=pd.to_numeric(df['Duration (sec.)'], errors='coerce').notnull().all()
    
    if validationDepartureStationId==False:
        print("Departure station id must be integer")
    elif validationReturnStationId==False:
        print("Return station id must be integer")
    elif validationDuration==False:
        print("Duration (sec.) must be integer")
    else:
        print("Integers OK")
def validateFloat(file):
    df=getCsvFile(file)
    validationDistance=pd.api.types.is_float_dtype(df["Covered distance (m)"])
    if validationDistance==False:
        print("Distance must be float")
    else:
        print("Floats OK")

def validateStringValues(file):
    df=getCsvFile(file)
    validationDepartureStName = pd.api.types.is_string_dtype(df['Departure station name'].dtype)
    validationReturnStName = pd.api.types.is_string_dtype(df['Return station name'].dtype)
    if validationDepartureStName==False:
        print("Departure st. name must be string")
    elif validationReturnStName==False:
        print("Return st. name must be string")
    else:
        print("Strings OK")

#Functions for stations validation
def validationStationsIntegers(file):
    df=getCsvFile(file)

    validationFID=pd.to_numeric(df['FID'], errors='coerce').notnull().all()
    validationID=pd.to_numeric(df['ID'], errors='coerce').notnull().all()
    validationKapasiteet=pd.to_numeric(df['Kapasiteet'], errors='coerce').notnull().all()

    if validationFID==False:
        print("FID must be integer")
    elif validationID==False:
        print("ID id must be integer")
    elif validationKapasiteet==False:
        print("Kapasiteet must be integer")
    else:
        print("Integers OK")

def validationStationsFloat(file):
    df=getCsvFile(file)
    validationX=pd.api.types.is_float_dtype(df["x"])
    validationY=pd.api.types.is_float_dtype(df["y"])
    if validationX==False:
        print("X must be float")
    elif validationY==False:
        print("Y must be float")
    else:
        print("Floats OK")
def validationStationsString(file):
    df=getCsvFile(file)

    validationStNimi = pd.api.types.is_string_dtype(df['Nimi'].dtype)
    validationStNamn = pd.api.types.is_string_dtype(df['Namn'].dtype)
    validationStName = pd.api.types.is_string_dtype(df['Name'].dtype)
    validationStOsoite = pd.api.types.is_string_dtype(df['Osoite'].dtype)
    validationStAdress = pd.api.types.is_string_dtype(df['Adress'].dtype)
    validationStKaupunki = pd.api.types.is_string_dtype(df['Kaupunki'].dtype)
    validationStStad = pd.api.types.is_string_dtype(df['Stad'].dtype)
    validationStOperaattor = pd.api.types.is_string_dtype(df['Operaattor'].dtype)

    if validationStNimi==False:
        print("Nimi must be string")
    elif validationStNamn==False:
        print("Namn must be string")
    elif validationStName==False:
        print("Name must be string")
    elif validationStOsoite==False:
        print("Osoite must be string")
    elif validationStAdress==False:
        print("Adress must be string")
    elif validationStKaupunki==False:
        print("Kaupunki must be string")
    elif validationStStad==False:
        print("Stad must be string")
    elif validationStOperaattor==False:
        print("Operaattor must be string") 
    else:
        print("Strings OK")
