import pandas as pd


def createInsertedStations(file,mycursor,engine):
    stationsDF=pd.read_csv(file)
    stationsDF.to_sql('insertedstations', engine,if_exists='replace',index=False)
    insertedstations="SELECT * FROM insertedstations"
    mycursor.execute(insertedstations)

def getModifiedJourneysCSV(file,):
    journeysDF=pd.read_csv(file)
    journeysDF.rename(columns = {'Departure':'DEPARTURE','Return':'RETURN','Departure station id':'DEPARTURE_STATION_ID','Return station id':'RETURN_STATION_ID','Departure station name':'DEPARTURE_STATION','Return station name':'RETURN_STATION','Covered distance (m)':'DISTANCE','Duration (sec.)':'DURATION'}, inplace = True)
    journeysDF['DISTANCE']=(journeysDF['DISTANCE']/1000).round(2)
    journeysDF['DURATION']=(journeysDF['DURATION']/60).round(2)
    return journeysDF

def createHslJourneys(DF,mycursor,engine):
    DF.to_sql('hsl_journeys', engine,if_exists='replace',index=False)
    journeysSql="SELECT * FROM hsl_journeys WHERE DISTANCE >0.01 AND DURATION >0.01"
    mycursor.execute(journeysSql)


"""
def getSQLquery(tablename,columns,values):
    sql = (f"INSERT INTO {tablename}"
        f"({columns})" 
        f" VALUES ({values})")
    
    return sql
def getCountFromDepartureStation(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT Departure_station_name, count(*) from hsl_journeys GROUP BY Departure_station_name")
    records=mycursor.fetchall()
    return records

def getCountFromReturnStation(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT Return_station_name, count(*) from hsl_journeys GROUP BY Return_station_name")
    records=mycursor.fetchall()
    return records
    """