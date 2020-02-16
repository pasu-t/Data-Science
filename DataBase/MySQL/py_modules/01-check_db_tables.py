import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="sys"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
print(dir(mycursor))

# mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)