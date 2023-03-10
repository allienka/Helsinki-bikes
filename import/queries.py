#stations
createTableHslStations="CREATE OR REPLACE TABLE HSL_STATIONS (STATION_ID int PRIMARY KEY,STATION VARCHAR(100),ADDRESS VARCHAR(100),JOURNEYS_STARTED DOUBLE(10,2) DEFAULT 0,JOURNEYS_ENDED DOUBLE(10,2) DEFAULT 0,AVG_STARTING_JOURNEY_DIST DOUBLE(10,2) DEFAULT 0,TOTAL_STARTING_JOURNEY_DIST DOUBLE(10,2) DEFAULT 0,AVG_ENDING_JOURNEY_DIST DOUBLE(10,2) DEFAULT 0,TOTAL_ENDING_JOURNEY_DIST DOUBLE(10,2) DEFAULT 0,LAST_PROCESSED_TM timestamp DEFAULT '2021-01-01 00:00:00');"

insertIntoHslStations="INSERT INTO hsl_stations(STATION_ID, STATION,ADDRESS) SELECT FID,NAME,Osoite FROM insertedstations WHERE NOT EXISTS(SELECT STATION_ID,STATION,ADDRESS FROM hsl_stations WHERE insertedstations.FID = hsl_stations.STATION_ID);"
changeFID="ALTER TABLE `insertedstations` CHANGE `FID` `FID` INT(10) NOT NULL;"
changeName="ALTER TABLE `insertedstations` CHANGE `Name` `Name` VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL;"
insertMissingSt="INSERT INTO hsl_stations(STATION_ID, STATION) SELECT src.STATION_ID,src.STATION FROM (SELECT STATION_ID,STATION FROM(SELECT DISTINCT DEPARTURE_STATION_ID AS STATION_ID, DEPARTURE_STATION AS STATION FROM hsl_journeys UNION SELECT DISTINCT RETURN_STATION_ID AS STATION_ID,RETURN_STATION AS STATION FROM hsl_journeys) AS JR WHERE JR.STATION_ID NOT IN (SELECT STATION_ID FROM HSL_STATIONS)) AS src;"


#journeys
changeDTDeparture="ALTER TABLE `hsl_journeys` CHANGE `DEPARTURE` `DEPARTURE` TIMESTAMP NULL DEFAULT NULL"
changeDTReturn="ALTER TABLE `hsl_journeys` CHANGE `RETURN` `RETURN` TIMESTAMP NULL DEFAULT NULL"
changeDTDstID="ALTER TABLE `hsl_journeys` CHANGE `DEPARTURE_STATION_ID` `DEPARTURE_STATION_ID` INT(10) NULL DEFAULT NULL"
changeDTDstName="ALTER TABLE `hsl_journeys` CHANGE `DEPARTURE_STATION` `DEPARTURE_STATION` VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL"
changeDTRstID="ALTER TABLE `hsl_journeys` CHANGE `RETURN_STATION_ID` `RETURN_STATION_ID` INT(10) NULL DEFAULT NULL"
changeDTRstName="ALTER TABLE `hsl_journeys` CHANGE `RETURN_STATION` `RETURN_STATION` VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL;"
addJourneysID="ALTER TABLE hsl_journeys ADD `JOURNEYS_ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;"
#the journeys data for stations
journeysStarted="UPDATE HSL_STATIONS AS ST, (SELECT COUNT(DEPARTURE_STATION) AS CNT, DEPARTURE_STATION_ID FROM HSL_JOURNEYS AS HJ JOIN( SELECT NVL( MAX(LAST_PROCESSED_TM), '2021-01-01 00:00:00' ) AS LAST_PROCESSED_TM FROM HSL_STATIONS ) AS LPI WHERE HJ.DEPARTURE > LPI.LAST_PROCESSED_TM GROUP BY DEPARTURE_STATION_ID ) AS HS SET ST.JOURNEYS_STARTED = ST.JOURNEYS_STARTED + HS.CNT WHERE ST.STATION_ID = HS.DEPARTURE_STATION_ID;"
journeysEnded="UPDATE HSL_STATIONS AS ST, ( SELECT COUNT(RETURN_STATION_ID) AS CNT, RETURN_STATION_ID FROM HSL_JOURNEYS AS HJ JOIN (SELECT NVL(MAX(LAST_PROCESSED_TM),'2021-01-01 00:00:00') AS LAST_PROCESSED_TM FROM HSL_STATIONS) AS LPI WHERE HJ.DEPARTURE > LPI.LAST_PROCESSED_TM GROUP BY RETURN_STATION_ID ) AS HS SET ST.JOURNEYS_ENDED = ST.JOURNEYS_ENDED + HS.CNT WHERE ST.STATION_ID = HS.RETURN_STATION_ID;"          
totalStartingJourneyDist="UPDATE HSL_STATIONS AS ST, ( SELECT DEPARTURE_STATION_ID, SUM(DISTANCE) AS DISTANCE FROM HSL_JOURNEYS AS HJ JOIN (SELECT NVL(MAX(LAST_PROCESSED_TM),'2021-01-01 00:00:00') AS LAST_PROCESSED_TM FROM HSL_STATIONS) AS LPI WHERE HJ.DEPARTURE> LPI.LAST_PROCESSED_TM GROUP BY DEPARTURE_STATION_ID ) AS HS SET ST.TOTAL_STARTING_JOURNEY_DIST = NVL(ST.TOTAL_STARTING_JOURNEY_DIST, 0) + HS.DISTANCE WHERE ST.STATION_ID = HS.DEPARTURE_STATION_ID;"
totalEndingJourneyDist="UPDATE HSL_STATIONS AS ST, ( SELECT RETURN_STATION_ID, SUM(DISTANCE) AS DISTANCE FROM HSL_JOURNEYS AS HJ JOIN (SELECT NVL(MAX(LAST_PROCESSED_TM),'2021-01-01 00:00:00') AS LAST_PROCESSED_TM FROM HSL_STATIONS) AS LPI WHERE HJ.DEPARTURE> LPI.LAST_PROCESSED_TM GROUP BY RETURN_STATION_ID ) AS HS SET ST.TOTAL_ENDING_JOURNEY_DIST = NVL(ST.TOTAL_ENDING_JOURNEY_DIST, 0) + HS.DISTANCE WHERE ST.STATION_ID = HS.RETURN_STATION_ID;"
average="UPDATE HSL_STATIONS AS ST SET ST.AVG_STARTING_JOURNEY_DIST = ST.TOTAL_STARTING_JOURNEY_DIST / ST.JOURNEYS_STARTED , ST.AVG_ENDING_JOURNEY_DIST = ST.TOTAL_ENDING_JOURNEY_DIST / ST.JOURNEYS_ENDED;"
updateProcessedTM="UPDATE HSL_STATIONS AS ST SET ST.LAST_PROCESSED_TM = (SELECT MAX(DEPARTURE) AS LAST_PROCESSED_TM FROM HSL_JOURNEYS);"