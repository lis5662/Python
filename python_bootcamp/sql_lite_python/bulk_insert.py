import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]

# for person in people:
#    insert that one person

# c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?, ?, ?)", person)
    average += person[2]
print(average/len(people))

# c.execute(query, data)
# commit changes
conn.commit()
conn.close()