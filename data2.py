import sqlite3

conn = sqlite3.connect('database1.db.db')
print("Opened database successfully");

cursor = conn.execute("SELECT * from MOVIES")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ACTOR'S NAME = ", row[2])
   print("RATING = ", row[3], "\n")
print("Operation done successfully");



cursor = conn.execute("SELECT * from MOVIES where RATING=8")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ACTOR'S NAME = ", row[2])
   print("RATING = ", row[3], "\n")
print("Operation done successfully");




conn.close()