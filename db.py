import random
import sqlite3 as sl

con = sl.connect('database.db')


def recreate(con_):
    with con_:
        con_.execute("DROP TABLE weights;")
        con_.execute(("CREATE TABLE weights"
                      "(id PRIMARY KEY,"
                      "layer INTEGER,"
                      "i INTEGER,"
                      "j INTEGER,"
                      "value FLOAT"
                      ");"))


sql = "INSERT INTO weights (id, layer, i, j, value) values(?, ?, ?, ?, ?)"

data = []

# recreate(con)


count = 0

# 2 layers of weights: layer = 1, 2 and then out
for layer in range(2):
    print(layer)

    if layer == 0:
        for j in range(10):
            for i in range(324):
                value = random.uniform(0, 1)
                data.append((count, layer, i, j, value))
                count += 1

    if layer == 21:
        for j in range(10):
            for i in range(100):
                value = random.uniform(0, 1)
                data.append((count, layer, i, j, value))
                count += 1

"""
sql = ("CREATE TABLE weights("
       "id PRIMARY KEY,"
       "layer INTEGER,"
       "i INTEGER,"
       "j INTEGER,"
       "value FLOAT"
       ");")
"""

"""
sql = "DROP TABLE weights;"
"""


# many = False, one = True
only_one = False

with con:
    if only_one:
        con.execute(sql)

    else:
        con.executemany(sql, data)
