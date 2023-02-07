# Helsinki-citybikes

The aim of this project is to create a web application which lists all the journeys and stations by Helsinki city bikes. The app uses a backend service to fetch the data. Backend can use a database, or it can be memory-based. 

# Requirements

- Import data from the CSV files to a database or in-memory storage
- Validate data before importing
- Don't import journeys that lasted for less than ten seconds
- Don't import journeys that covered distances shorter than 10 meters

datasets of journey data:<br>
https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv<br>
https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv<br>
https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv

dataset of stations data:<br>
https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv

<b>Journey list view</b><br>

- List journeys
- For each journey show departure and return stations, covered distance in kilometers and duration in minutes

<b>Station list</b><br>

- List all the stations

<b>Single station view</b><br>

- Station name
- Station address
- Total number of journeys starting from the station
- Total number of journeys ending at the station

you can find additional requirements or extras [here](https://github.com/solita/dev-academy-2023-exercise#functional-requirements)

# PREREQUISITES

- Install MySQLWorkbench or Xampp
- Any Editor (Preferably VS Code or Sublime Text)
- Any web browser with the latest version


Languages and Technologies used

- XAMPP or MySQL Workbench
- Python 3
- MySQL
- Node.js, Express


<b>Steps to run the project on your machine</b>
1. Download and install Python ([instructions here](https://www.geeksforgeeks.org/how-to-install-python-on-windows/))
2. Install the libraries needed (pandas, numpy, os.path, connection,sqlalchemy) in vscode download python get-pip.py  and then pip run 'libraryname'
3. Download and install XAMPP  or MYSQLWorkbench ([XAMPP](https://www.wikihow.com/Install-XAMPP-for-Windows) [WORKBENCH](https://www.tutorialsfield.com/how-to-install-mysql-workbench/))
4. Install Node and Express on your machine:
  - create a folder and open it in cmp: 
  - npm install -g express-generator (install express generator)
  - npx express --view=ejs (install Node.js Express framework, with EJS template engine)
  - npm install (install node.js dependencies)
  - npm install mysql (install node mysql module)
  - npm install python-shell
 
5. Clone or download the repository 
6. Extract all the files and move them to a folder
7. Start Mysql in your XAMPP control panel or Workbench
8. For Xampp open your web browser and type 'localhost/phpmyadmin' 
9. In phpmyadmin page or Workbench, create a new database from the left panel and name it as 'helsinki_bikes'
10. Open backend files in editor and run main.py
11. After the data are inserted to the database
12. Open the folder JourneysFront in terminal
13. Write 'npm run start' (it should connect to the database)
14. Open localhost:3000 in browser , you should see the Journeys list
15. For Stations repeat the same from step 11, but with the folder SingleStationFront

# DATABASE STRUCTURE

![helsinki_bikes_structure](https://user-images.githubusercontent.com/105230372/215819132-10c70a02-85e6-4bbd-804c-b9f2b15999c6.jpg)

TABLE HSL_STATIONS:
-	STATION ID: stations ID  INTEGER
-	STATION: station name  VARCHAR
-	ADDRESS: stations address VARCHAR
-	JOURNEYS STARTED: how many journeys started from the particular station DOUBLE(10,2)
-	JOURNEYS ENDED: how many journeys ended at this station DOUBLE(10,2)
-	AVG STARTING JOURNEY DIST: average amount of journeys starting from this station DOUBLE(10,2)
-	AVG ENDING JOURNEY DIST: average amount of journeys ending from this station DOUBLE (10,2)
-	TOTAL ENDING JOURNEY DIST: amout of all journeys starting from this station (needed for counting the avg) DOUBLE(10,2)
-	TOTAL STARTING JOURNEY DIST: amout of all journeys ending from this station (needed for counting the avg) DOUBLE(10,2)
-	LAST PROCESSED TM: time of the last insert TIMESTAMP

TABLE HSL_JOURNEYS	:
- DEPARTURE: the time of the departure TIMESTAMP
- RETURN: the time of retrun TIMESTAMP
- DEPARTURE STATION ID: ID of the departure station INTEGER
- DEPARTURE STATION: name of the departure station VARCHAR
- RETURN STATION ID:ID of the return station INTEGER
- RETURN STATION: name of the return station VARCHAR
- DISTANCE: the distance of the journey in KM DOUBLE
- DURATION: duration of the journey in minutes DOUBLE
- JOURNEYS ID: created ID in the journeys table


# FILES DESCRIPTIONS

- BACKEND:
  - validationfunctions.py : functions used for validating the CSV files before they would be inserted into the database. 
     such as: - file exists<br>
              - same amount of columns<br>
              - same names of the columns<br>
              - all datatypes are valid<br>
               
  - validations.py: executing the validation functions
  - connection.py : creating the connection to the database helsinki-bikes
  - functions.py, queries.py : functions and queries needed for modifing the csv files and inserting data to the database
  - mainjourneys.py, mainstations: running the program
  
- JOURNEYS, STATIONS
    (files created by the express and node js, modified for my datatable) 
  - bin
  - node_modules
  - public (includes css file)
  - routes / - users.js
             - index.js: Connecting to the DB. Also sort, filter,pagination and search of the datatable, creating the JSON output for the frontend file (ejs)
  - views / - error.ejs<br>
           - index.ejs :file to display HTML output in the browser. It includes jQuery, Boostrap 5 library link. 
  - app.js
  - database.js : creating the connection to the DB
  - package.json
  - package-lock.json
  
           
          





https://user-images.githubusercontent.com/105230372/217209229-2dd76240-3256-4c8b-ab25-3cc2c4bb28a3.mp4





https://user-images.githubusercontent.com/105230372/217209270-f1f41d11-dd5a-4358-bb3c-66bf220db963.mp4



# TO DO

- tests
