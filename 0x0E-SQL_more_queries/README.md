# Project 0x0E. SQL - More queries 📚

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
| [0-privileges.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql) | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`). |
| [1-create_user.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql) | Creates the MySQL server user `user_0d_1`. |
| [2-create_read_user.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql) | Creates the database `hbtn_0d_2` and the user `user_0d_2`. |
| [3-force_name.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql) | creates the database `hbtn_0d_2` and the user `user_0d_2`. |
| [4-never_empty.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql) | Creates the table `id_not_null` on your MySQL server. |
| [5-unique_id.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/5-unique_id.sql) | Creates the table `unique_id` on your MySQL server. |
| [6-states.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql) | Creates the database `hbtn_0d_usa` and the table states (in the database `hbtn_0d_usa`) on your MySQL server. |
| [7-cities.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql) | creates the database `hbtn_0d_usa` and the table cities (in the database `hbtn_0d_usa`) on your MySQL server. |
| [8-cities_of_california_subquery.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql) | Llists all the cities of California that can be found in the database `hbtn_0d_usa`. |
| [9-cities_by_state_join.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql) | Lists all cities contained in the database `hbtn_0d_usa`. |
| [10-genre_id_by_show.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql) |  Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. |
| [11-genre_id_all_shows.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql) | Lists all shows contained in the database `hbtn_0d_tvshows`. |
| [12-no_genre.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql) | Lists all shows contained in `hbtn_0d_tvshows` without a genre linked. |
| [13-count_shows_by_genre.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/13-count_shows_by_genre.sql) | Lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. |
| [14-my_genres.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/14-my_genres.sql) | Uses the `hbtn_0d_tvshows` database to lists all genres of the show Dexter. |
| [15-comedy_only.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/15-comedy_only.sql) | Lists all Comedy shows in the database `hbtn_0d_tvshows`. |
| [16-shows_by_genre.sql](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/16-shows_by_genre.sql) | Lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. |
