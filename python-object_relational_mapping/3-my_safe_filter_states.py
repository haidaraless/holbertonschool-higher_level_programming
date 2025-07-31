#!/usr/bin/python3
"""
Script to lists all states where name matches the argument
from the database hbtn_0e_0_usa
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

    cursor.execute("SELECT * FROM states WHERE name LIKE %s \
        ORDER BY id ASC", (sys.argv[4]),)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
