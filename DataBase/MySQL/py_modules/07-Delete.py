import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM customers WHERE address='Mountain 21'")

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")