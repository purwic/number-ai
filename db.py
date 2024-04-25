"""

import random
import sqlite3 as sl

con = sl.connect('database.db')

sql = "INSERT INTO weights (id, layer, i, j, value) values(?, ?, ?, ?, ?)"

data = []

count = 0

# 2 layers of weights: layer = 1, 2 and then out
for layer in range(1, 2+1):
    print(layer)

    if layer == 1:
        for i in range(1, 324+1):
            for j in range(1, 100+1):

                value = random.uniform(0, 1)
                data.append((count, layer, i, j, value))
                count += 1

    if layer == 2:
        for i in range(1, 100+1):
            for j in range(1, 10+1):

                value = random.uniform(0, 1)
                data.append((count, layer, i, j, value))
                count += 1



"""
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

"""
# many = False, one = True
only_one = False


with con:

    if only_one:
        con.execute(sql)

    else:
        con.executemany(sql, data)
"""