from functions import *
from queries import *
from validations import *
from connection import createDbc
from sqlalchemy import create_engine


journeys1="../2021-05.csv"
journeys2="../2021-06.csv"
journeys3="../2021-07.csv"
asematCSV="../asemat_avoin.csv"


#validating CSV files before using
validations(journeys1,journeys2,journeys3,asematCSV)

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
print (f"{asematCSV} inserted")


engine.dispose()
db.commit()
db.close()