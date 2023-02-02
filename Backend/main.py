from functions import *
from queries import *
from connection import createDbc
import pandas as pd
from sqlalchemy import create_engine
from validations import *

#validationg CSV files before using
validations()


journeys1="./2021-05.csv"
journeys2="./2021-06.csv"
journeys3="./2021-07.csv"
asematCSV="./asemat_avoin.csv"

db_data = 'mysql+pymysql://' + 'root' + ':' + '' + '@' + 'localhost' + ':3306/' \
       + 'helsinki_bikes' + '?charset=utf8mb4'

engine=create_engine(db_data)
db=createDbc()
mycursor = db.cursor()

result=createInsertedStations(asematCSV,mycursor,engine)
result=mycursor.fetchall()

#changin data types so that they will match with HSL_STATIONS
mycursor.execute(changeFID)
mycursor.execute(changeName)
mycursor.execute(createTableHslStations)
mycursor.execute(insertIntoHslStations) 

#journeyFiles=[journeys1,journeys2,journeys3]
#for file in journeyFiles:
journeysDF=getModifiedJourneysCSV(journeys1)

result=createHslJourneys(journeysDF,mycursor,engine)
result=mycursor.fetchall()
mycursor.execute(addJourneysID)
#changing datatypes 
mycursor.execute(changeDTDeparture)
mycursor.execute(changeDTReturn)
mycursor.execute(changeDTDstID)
mycursor.execute(changeDTDstName)
mycursor.execute(changeDTRstID)
mycursor.execute(changeDTRstName)


#fill table HSL_STATIONS with potentially missing stations from journeys
mycursor.execute(insertMissingSt)

#add number of journeys starting and ending at each station for this batch of data
mycursor.execute(journeysStarted)
mycursor.execute(journeysEnded)

#add total duration of all journeys to this station and AVG
mycursor.execute(totalStartingJourneyDist)
mycursor.execute(totalEndingJourneyDist)
mycursor.execute(average)
#update timestamp of last processed data
mycursor.execute(updateProcessedTM)

engine.dispose()
db.commit()
db.close()

