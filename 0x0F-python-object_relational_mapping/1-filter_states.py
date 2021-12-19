#!/usr/bin/python3
""" Script that lists all states with a name starting with N from the database
hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    serv = MySQLdb.connect(host="localhost",  port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])

    c = serv.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    c.close()
    serv.close()
