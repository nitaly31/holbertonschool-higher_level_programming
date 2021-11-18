# Project 0x0D. SQL - Introduction 📚

### 📋 Requirements
***
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
* The length of your files will be tested using `wc`

### :bangbang: More Info
***
#### Comments for your SQL file:

```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### 🎯 Tasks
***
#### Mandatory:
| Files | Description |
| --- | --- |
| [`0-list_databases.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql) | Script that lists all databases of your MySQL server. |
| [`1-create_database_if_missing.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql) | Script that creates the database `hbtn_0c_0` in your MySQL server. |
| [`2-remove_database.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql) | Script that deletes the database hbtn_0c_0 in your MySQL server. |
| [`3-list_tables.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql) | Script that lists all the tables of a database in your MySQL server. |
| [`4-first_table.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql) | Script that creates a table called first_table in the current database in your MySQL server. |
| [`5-full_table.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql) | Script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. |
| [`6-list_values.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql) | Script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. |
| [`7-insert_value.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql) | Script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. |
| [`8-count_89.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql) | Script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`9-full_creation.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql) | Script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows. |
| [`10-top_score.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql) | Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`11-best_score.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql) | Script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`12-no_cheating.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql) | Script that updates the score of Bob to `10` in the table `second_table`. |
| [`13-change_class.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql) | script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`14-average.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql) | script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`15-groups.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql) | script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |
| [`16-no_link.sql`](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql) | script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. |

#### Advanced:
| Files | Description |
| --- | --- |
| [100-move_to_utf8.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql) | Converts hbtn_0c_0 database to UTF8. |
| [101-avg_temperatures.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql) | Displays the average temperature (Fahrenheit). |
| [102-top_city.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql) | Displays the top 3 of cities temperature during July and August. |
| [103-max_state.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql) | Displays the max temperature of each state. |