import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passward="root")

my_cursor = mydb.cursor()
