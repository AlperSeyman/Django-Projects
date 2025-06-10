import mysql.connector

dataBase = mysql.connector.connect(host='', user='', passwd='', auth_plugin='')

# Prepare a cursor object 
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE moin")

print("All Done!")