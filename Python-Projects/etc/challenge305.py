import sqlite3

# table values
rosterValues = (('Jean-Baptiste Zorg', 'Human', '122'), ('Korben Dallas', 'Meat Popsicle', '100'), ('Ak\'not', 'Mangalore', '-5'))

with sqlite3.connect(':memory:') as conn: # creates database in memory/RAM / Step 1
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ROSTER (Name TEXT, Species TEXT, IQ INT)") # Step 1, create table/columns
    cur.executemany("INSERT INTO Roster VALUES (?,?,?)", rosterValues) # Step 2, insert values from tuple variable
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human','Korben Dallas','100')) # Step 3, update one
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'") # Step 4, print results
    for row in cur.fetchall():
        print(row)