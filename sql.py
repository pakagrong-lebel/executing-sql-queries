# Python script to execute SQL queries on a database
import sqlite3
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result