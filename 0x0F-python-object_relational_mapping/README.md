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
| [0-select_states.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/0-select_states.py) | Lists all `states` from the database `hbtn_0e_0_usa`. |
| [1-filter_states.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/1-filter_states.py) | Lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`. |
| [2-my_filter_states.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/2-my_filter_states.py) | Takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. |
| [3-my_safe_filter_states.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py) | Takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. |
| [4-cities_by_state.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/4-cities_by_state.py) | Lists all `cities` from the database `hbtn_0e_4_usa`. |
| [5-filter_cities.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/5-filter_cities.py) | Takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`. |
| [model_state.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_state.py) | Python file that contains the class definition of a `State` and an instance `Base = declarative_base())` using the module `SQLAlchemy`. |
| [7-model_state_fetch_all.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py) | Lists all `State` objects from the database `hbtn_0e_6_usa`. |
| [8-model_state_fetch_first.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py) | Prints the first `State` object from the database `hbtn_0e_6_usa`. |
| [9-model_state_filter_a.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/9-model_state_filter_a.py) | Lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa` |
| [10-model_state_my_get.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/10-model_state_my_get.py) | Prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`. |
| [11-model_state_insert.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/11-model_state_insert.py) | Adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`. |
| [12-model_state_update_id_2.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/12-model_state_update_id_2.py) | Changes the name of a `State` object from the database `hbtn_0e_6_usa`. |
| [13-model_state_delete_a.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/13-model_state_delete_a.py) | Deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`. |
| [model_city.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/model_city.py) | Contains the class definition of a `City`. |
| [14-model_city_fetch_by_state.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py) | Prints all `City` objects from the database `hbtn_0e_14_usa`. |
