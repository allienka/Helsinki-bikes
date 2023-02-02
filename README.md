# Helsinki-citybikes

The aim of this project is to create a web application that uses a backend service to fetch the data. Backend can use a database, or it can be memory-based

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

1. Download and install XAMPP on your machine 
2. Clone or download the repository 
3. Extract all the files and move it to the 'htdocs' folder of your XAMPP directory. 
4. Start Apache and Mysql in your XAMPP control panel. 
5. Open your web browser and type 'localhost/phpmyadmin' 
6. In phpmyadmin page, create a new database from the left panel and name it as drones 
7. Create database 'helsinki_bikes'
8. Open a new tab and type 'localhost/folder

# DATABASE STRUCTURE

![helsinki_bikes_structure](https://user-images.githubusercontent.com/105230372/215819132-10c70a02-85e6-4bbd-804c-b9f2b15999c6.jpg)

..to do

# FILES DESCRIPTIONS
..to do
- VALIDATIONS
- BACKEND
- FRONTEND
