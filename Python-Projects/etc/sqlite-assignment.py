import sqlite3

# connection = sqlite3.connect(':memory:') # creates one-time-use database for testing purposes

# connection = sqlite3.connect("C:/Users/Ethan/Documents/GitHub/python-projects/sqlite-assignment/test_database.db") # path to connect to database
# c = connection.cursor() # instantiates a Cursor object. allows operations on a database.
# c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)") # creates a table "People", and adds three columns to it. 
# c.execute("INSERT INTO People VALUES ('Ron', 'Obvious', 42)") # inserts new data into the table's columns
# connection.commit() # commits the changes to the database
# c.execute("DROP TABLE IF EXISTS People") # deletes the People table and all data within it.
# connection.close() # closes the database, similar to closing a file

# with sqlite3.connect("test_database.db") as connection: # this allows for continous work with the database and no longer requires 'commit()', changes are saved automatically. 
# Keep in mind, however, that you will still need to commit() a change if you want to see the result of that change immediately (before closing the connection).
#    c = connection.cursor()
#    c.executescript("""DROP TABLE IF EXISTS People;
#                    CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT);
#                    INSERT INTO PEOPLE VALUES ('Ron','Obvious','42');
#                    """) # executescript() gives a string that represents a script- lines of SQL are separated by ;

# Can use executemany() and a tuple of tuples to execute many similiar statements
# peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur','Belling', 28)) # a tuple of tuples
# c.executemany("INSERT INTO People VALUES (?,?,?)", peopleValues) # question marks act as place-holders for the tuples in peopleValues. This is called a parameterized statement.

# Example of unsecure way to input information
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# 
# with sqlite3.connect('test_database.db') as connection:
#     c = connection.cursor()
#     line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
#     c.execute(line)

# updated version
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# personData = (firstName, lastName, age)
# 
# with sqlite3.connect('test_database.db') as connection:
#     c = connection.cursor()
#     c.execute("INSERT INTO People VALUES (?,?,?)", personData)
#     # or update the table:
#     c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
#                 (45,'Luigi','Vercotti'))

peopleValues = (('Ron','Obvious',42), ('Luigi','Vercotti', 43), ('Arthur','Belling',28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES (?,?,?)",
                    peopleValues)
    
    # fetching all
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30") # select query
    for row in c.fetchall(): # fetch all from c
        print(row) # print row

    # alternatively, use a loop to fetch one at a time
    while True:
        row = c.fetchone()
        if row is None: # if there is nothing in the row,
            break # stop this if
        print(row)