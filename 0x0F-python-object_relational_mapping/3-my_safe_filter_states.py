#!/usr/bin/python3
""" Script  that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument preventing SQL
injection.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    serv = MySQLdb.connect(host="localhost",  port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])

    c = serv.cursor()
    stateName = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (
        stateName,))
    rows = c.fetchall()
    for row in rows:
        if row[1] == stateName:
            print(row)
    c.close()
    serv.close()
