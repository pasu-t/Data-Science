import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)

mycursor = mydb.cursor()
# mycursor.execute("DROP TABLE users")
# mycursor.execute("DROP TABLE products")
mycursor.execute("DROP TABLE customers")