#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="username",
                         passwd="password", db="database", port=3306)
    cursor = db.cursor()
    cur.execute(SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
