import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursos object
с = conn.cursor()
# с.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
с.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

#Iterate over cursor
# for result in с:
#    print(result)

# Fetch One Result
# print(с.fetchone())

# Fetch all results as list
print(с.fetchall())

# commit changes
conn.commit()
conn.close()