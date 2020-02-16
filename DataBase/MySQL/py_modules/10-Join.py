import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255), fav INT)")
mycursor.execute("CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(255))")

sql1 = "INSERT INTO users (id, name, fav) VALUES (%s, %s, %s)"
val1 = [
(1, 'John', 154),
(2, 'Peter', 154),
(3, 'Amy', 155),
(4, 'Hannah',None),
(5, 'Michael',None)
]

sql2 = "INSERT INTO products (id, name) VALUES (%s, %s)"
val2 = [
(154, 'Chocolate Heaven'),
(155, 'Tasty Lemons'),
(156, 'Vanilla Dreams')
]

mycursor.executemany(sql1, val1)
print(mycursor.rowcount, "was inserted.")
mycursor.executemany(sql2, val2)
print(mycursor.rowcount, "was inserted.")
mydb.commit()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("DROP TABLE users")
mycursor.execute("DROP TABLE products")