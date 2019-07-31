import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
с = conn.cursor()

# execute some sql
# с.execute("CREATE TABLE friends (first_name TEXT, last name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
#                    VALUES ('Merriwether', 'Lewis', 7)'''

# BAD! DO NOT DO THIS!
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!
# form_first = "Mary-Todd"
# query = "INSERT INTO friends (first_name) VALUES (?)"
# с.execute(query, (form_first))

data = ("Steve", "Irwin", 9)
query = f"INSERT INTO friends VALUES (?, ?, ?)"
с.execute(query, data)

# commit changes
conn.commit()
conn.close()