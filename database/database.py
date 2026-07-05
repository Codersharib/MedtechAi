import mysql.connector


def get_connection():

    connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="1234567720",

        database="medintel"

    )

    return connection