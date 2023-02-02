import mysql.connector

def createDbc():
    mydatabase = mysql.connector.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        database="helsinki_bikes"
    
    )
    return mydatabase
