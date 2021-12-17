# Project 0x0F. Python - Object-relational mapping 📚

### :bookmark_tabs: Background Context
***
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

#### Without ORM:
```MYSQL
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
#### With an ORM:
```MYSQL
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

### 📋 Requirements
***
* Allowed editors: `vi`, `vim`, `emacs`.
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* Files will be executed with `MySQLdb` version `2.0.x`.
* Files will be executed with `SQLAlchemy` version `1.4.x`.
* Files must be executable.
* The length of your files will be tested using `wc`.
* You are not allowed to use `execute` with sqlalchemy.

### 🎨 Style
***
* Code should use the PEP 8 style (version 2.7.*).

### 🎯 Tasks
***
#### Mandatory:

| Files | Description |
| --- | --- |
| []() |  |
| []() |  |
| []() |  |
| []() |  |
| []() |  |
| []() |  |