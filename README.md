# Helsinki-citybikes

The aim of this project is to create a web application that shows the list of the journeys and stations used with Helsinki city bikes. The app uses a backend service to fetch the data. Backend can use a database, or it can be memory-based. 

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

-List all the stations

<b>Single station view</b><br>

- Station name
- Station address
- Total number of journeys starting from the station
- Total number of journeys ending at the station

you can find additional requirements or extras:  

https://github.com/solita/dev-academy-2023-exercise#functional-requirements

# PREREQUISITES

- Install XAMPP web server
- Any Editor (Preferably VS Code or Sublime Text)
- Any web browser with the latest version


Languages and Technologies used

- XAMPP (A web server by Apache Friends)
- Python
- MySQL
- Node.js, Express


<b>Steps to run the project on your machine</b>

1. Download and install XAMPP
2. Install Node and Express on your machine:
  - create a folder and open it in cmp: 
  - npm install -g express-generator (install express generator)
  - npx express --view=ejs (install Node.js Express framework, with EJS template engine)
  - npm install (install node.js dependencies)
  - npm install mysql (install node mysql module)
 
3. Clone or download the repository 
4. Extract all the files and move them to a folder
5. Start Apache and Mysql in your XAMPP control panel. 
6. Open your web browser and type 'localhost/phpmyadmin' 
7. In phpmyadmin page, create a new database from the left panel and name it as 'helsinki_bikes'
8. Open backend files in editor and run main.py
9. After the data are inserted to the database
10. Open the folder JourneysFront in terminal
11. Write 'npm run start' (it should connect to the database)
12. Open localhost:3000 in browser , you should see the Journeys list
13. For Stations repead the same from step 10, but with the folder SingleStationFront

# DATABASE STRUCTURE

![helsinki_bikes_structure](https://user-images.githubusercontent.com/105230372/215819132-10c70a02-85e6-4bbd-804c-b9f2b15999c6.jpg)

..to do

# FILES DESCRIPTIONS

- BACKEND
- FRONTEND

# TO DO
- tests
- deployment

JOURNEYS VIEW
![journeys view](https://user-images.githubusercontent.com/105230372/216556861-7457560e-32fe-4dd3-8d82-d2e2f027742d.jpg)


STATIONS VIEW

![stations view](https://user-images.githubusercontent.com/105230372/216557811-b1c604ba-05d4-47f4-821b-d6e94cc512fb.jpg)
