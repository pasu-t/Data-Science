import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)

mycursor = mydb.cursor()
mycursor.execute("UPDATE customers SET address='Canyon 123' WHERE address='Valley 345'")
mydb.commit()

print(mycursor.rowcount, "record(s) affected")
