#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    serv = MySQLdb.connect(host="localhost",  port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])

    newList = []
    c = serv.cursor()
    stateName = sys.argv[4]
    c.execute("SELECT c.id, c.name, s.name\
                    FROM cities AS c\
                    JOIN states AS s \
                    ON c.state_id=s.id ORDER BY s.id;")
    rows = c.fetchall()
    for row in rows:
        if row[2] == stateName:
            newList.append(row[1])
    print(', '.join(newList))
    c.close()
    serv.close()
