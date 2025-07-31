#!/usr/bin/python3
"""
Script to lists all cities from given state name
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name, charset="utf8")

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))

    cursor.close()
    db.close()
