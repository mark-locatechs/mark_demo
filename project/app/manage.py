import mysql.connector


config = {
        'user': 'mysql',
        'password': 'mysql',
        'host': 'db',
        'port': '3306'
    }
connection = mysql.connector.connect(**config)
