import sqlite3

conn = sqlite3.connect('database1.db.')
print("Opened database successfully");

conn.execute('''CREATE TABLE MOVIES
         (ID INT PRIMARY KEY     NOT NULL,
         MOVIE_NAME           TEXT    NOT NULL,
         ACTOR_NAME     TEXT   NOT NULL,
         RATING          INT    NOT NULL);''')
print("Table created successfully");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (1,'Shawshank Redemption','Morgan Freeman',8)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (2,'Die Hard','Bruce Willis',7)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (3,'Batman Begins','Christian Bale',8)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (4,'Spiderman','Tobey Maguire',9)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (5,'Lucy','Morgan Freeman',7)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (6,'The Dark Knight','Christian Bale',9)");

conn.execute("INSERT INTO MOVIES (ID,MOVIE_NAME,ACTOR_NAME,RATING) \
      VALUES (7,'The Dark Knight Rises','Christian Bale',8)");

conn.commit()
print("Records created successfully");

conn.close()