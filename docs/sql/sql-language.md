# SQL Language

SQL (Structured Query Language) is a language used to interact with databases. We use SQL in the following courses at CodeWizardsHQ:

| Middle School       | High School                      |
| ------------------- | -------------------------------- |
| Intro to Databases  | APIs and Databases               |
| Mastering APIs      | Professional Web App Development |
| Mastering Databases | Capstone 2                       |
| Capstone 3          | Mastering MVC Framework          |
|                     | Object Relational Mapping        |
|                     | Capstone 3                       |

In this section of our documentation, you'll find references to most of the core SQL language features that we use in our CodeWizardsHQ courses. All of our courses interact with databases using Python + SQL, so we'll show the core SQL syntax first and then give a working example in Python.

You'll also find many _Further reading_ sections, which pull from these excellent SQL/Python resources:

-   [SQLBolt](https://sqlbolt.com/lesson/introduction)
-   [SQLite Tutorial](https://www.sqlitetutorial.net/)
-   [Python.org Documentation](https://www.python.org/doc/)

<hr>

## What Is A Relational Database?

In a relational database, you structure your data in tables made up of rows and columns, kind of like an Excel spreadsheet. You can combine data from multiple tables using `JOIN`s or just pull data from a single table.

For example, consider the two tables below:

_users table_

| user_id | username | password   |
| ------- | -------- | ---------- |
| 1       | djs      | mypa$$word |
| 2       | django   | w0ff       |
| 3       | alecg    | c0de       |

_teachers table_

| teacher_id | user_id | username | is_admin |
| ---------- | ------- | -------- | -------- |
| 1          | 1       | djs      | 1        |
| 2          | 3       | alecg    | 0        |

We could get the username and password of all users that are teachers and admins like this:

```sql
SELECT
    users.username, users.password
FROM
    users
JOIN
    teachers
USING
    (user_id)
WHERE
    teachers.is_admin = 1;
┌──────────┬────────────┐
│ username │  password  │
├──────────┼────────────┤
│ djs      │ mypa$$word │
└──────────┴────────────┘
```

There are many different relational database implementations (MySQL, Postgres, etc.) but we use SQLite at CodeWizardsHQ because it is easy to work with and supports most of the common SQL features.

## Why Do We Need SQL?

When working with a database, you need a way to talk to the database and get data into/out of it. SQL is the language we use to do this in a SQLite database. SQL allows you to express relationships in a database in a structured way.

## Why Do We Use Python And SQL Together?

Although you can use raw SQL commands to talk to a SQL database, we use Python at CodeWizardsHQ because often you'll interact with databases this way in the real world. Think about apps you've used that store data about you between visits. That's using a database and a programming language (like Python) to interact with the database!

The SQL portions of a Python DB query will be a Python `str`. Consider this `INSERT` statement in raw SQL:

```text
INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
```

To run that from Python, we would do this:

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
"""

sql.execute(query)
con.commit()
```

The important thing to remember is that the `query` is just a `str` that you pass to `sql.execute()`. If you make a change to a table in the database (as we did above) then you use the `con.commit()` method to save the change (although in some CWHQ courses you merely view the results without changing the database). The semi-colon (`;`) isn't required when using a query from Python, but we'll keep it for consistency between the raw SQL examples.

### Bounded Parameters

When accepting user input in a Python program that modifies a SQL database, you'll use `?` as placeholders for any user-entered data and then pass the data to `sql.execute()` as a `list` like this:

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

# Use `?` for any user-entered data
query = """
    INSERT INTO users (username, password) VALUES (?, ?);
"""

# The `username` and `password` are bound to the `?` in the `query`
sql.execute(query, [username, password])
con.commit()
```

## ALTER TABLE

After creating a table, you may need to add or rename a column. The `ALTER TABLE` command allows you to do this.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

-- Renaming a column
ALTER TABLE users RENAME username TO teacher_name;

SELECT * FROM users;
┌─────────┬──────────────┬────────────┐
│ user_id │ teacher_name │  password  │
├─────────┼──────────────┼────────────┤
│ 1       │ djs          │ mypa$$word │
│ 2       │ django       │ w0ff       │
│ 3       │ alecg        │ c0de       │
└─────────┴──────────────┴────────────┘

-- Adding a new column with a default value for each row
ALTER TABLE users ADD is_admin INTEGER DEFAULT 0;

SELECT * FROM users;
┌─────────┬──────────────┬────────────┬──────────┐
│ user_id │ teacher_name │  password  │ is_admin │
├─────────┼──────────────┼────────────┼──────────┤
│ 1       │ djs          │ mypa$$word │ 0        │
│ 2       │ django       │ w0ff       │ 0        │
│ 3       │ alecg        │ c0de       │ 0        │
└─────────┴──────────────┴────────────┴──────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

def display_all_users_and_column_names():
    # Don't worry about this, it just shows us the column names
    query = """
        SELECT name FROM PRAGMA_TABLE_INFO('users');
    """

    result = sql.execute(query)
    print("\nColumn names:")
    print(*result.fetchall())

    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print("\nRows:")
    print(rows)


display_all_users_and_column_names()

query = """
    ALTER TABLE users RENAME username TO teacher_name;
"""

sql.execute(query)
display_all_users_and_column_names()

query = """
    ALTER TABLE users ADD is_admin INTEGER DEFAULT 0;
"""

sql.execute(query)
display_all_users_and_column_names()

# Make sure to commit the changes to the DB
con.commit()
```

**Output**

```text
Column names:
('user_id',) ('username',) ('password',)

Rows:
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]

Column names:
('user_id',) ('teacher_name',) ('password',)

Rows:
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]

Column names:
('user_id',) ('teacher_name',) ('password',) ('is_admin',)

Rows:
[(1, 'djs', 'mypa$$word', 0), (2, 'django', 'w0ff', 0), (3, 'alecg', 'c0de', 0)]
```

## CREATE TABLE

Relational databases are made up of tables, and you'll need to create tables to hold your data if we don't provide one for you. We often use `IF NOT EXISTS` in CWHQ courses when creating a table because we'll run the statement every time our Python script runs, and an error would occur if you tried to create a table that already existed. Most tables should also have a `PRIMARY KEY` integer to uniquely identify each row of data.

The general format of a `CREATE TABLE` statement is:

```sql
CREATE TABLE IF NOT EXISTS table_name (
    column_one DATATYPE OPTIONAL_CONSTRAINTS...,
    column_two DATATYPE OPTIONAL_CONSTRAINTS...,
    column_three DATATYPE OPTIONAL_CONSTRAINTS...
    -- etc...
);
```

Note that each column definition is separated by a comma (`,`) but the final column definition should _not_ have a comma.

Here's an example of a `CREATE TABLE` statement for the `users` table from the [What Is A Relational Database?](#what-is-a-relational-database) section earlier in these docs:

**Raw SQL**

```sql
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
"""

sql.execute(query)
```

### Column Datatypes

When writing column definitions, your column can be one of 5 storage classes (which are a generic datatype) in SQLite:

-   `NULL`: Represents "nothingness"
-   `INTEGER`: Whole numbers
-   `REAL`: Decimal numbers
-   `TEXT`: Text data
-   `BLOB`: Binary data (like images, music, etc.)

You'll mainly use `INTEGER` and `TEXT` for CWHQ projects.

### Column Constraints

Besides the datatype, you can also put additional constraints on a column definition to enforce that a column is `UNIQUE`, or `NOT NULL`, or even a `PRIMARY KEY`. You can see all of those at work in this example:

```sql
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

## DELETE

To remove data in a SQL table, use the `DELETE` statement. Make sure to use a `WHERE` clause so that you only delete the rows you intend to.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

DELETE FROM users WHERE user_id = 3;

SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
└─────────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

# We'll use this twice, so it makes sense to be a function
def display_all_users():
    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


display_all_users()

query = """
    DELETE FROM users WHERE id = 3;
"""

sql.execute(query)

# Make sure to commit the changes to the DB
con.commit()

display_all_users()
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff')]
```

### Deleting all rows from a table

If you leave out the `WHERE` clause in a `DELETE` statement, you remove all rows from the table. This is a handy way to clear out all the rows if you need to start with a fresh table:

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

DELETE FROM users;

SELECT * FROM users;
-- nothing returned because the table is empty
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

# We'll use this twice, so it makes sense to be a function
def display_all_users():
    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


display_all_users()

query = """
    DELETE FROM users;
"""

sql.execute(query)

# Make sure to commit the changes to the DB
con.commit()

display_all_users()
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
[]
```

## DISTINCT

If you want to get unique column values for a set of rows, use the `DISTINCT` clause of a `SELECT` query

For example, in the `products` table below, it may be hard at a glance to see what categories are present, but with `DISTINCT` it's easy to see we only have three!

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get only the unique categories for our products.
SELECT DISTINCT product_category FROM products;
┌──────────────────┐
│ product_category │
├──────────────────┤
│ Computers        │
│ Microphones      │
│ Accessories      │
└──────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

query = """
    SELECT * FROM products;
"""

result = sql.execute(query)
rows = result.fetchall()

# Easier to read if we loop then print each row since there are 8 rows.
for row in rows:
    print(row)

query = """
    SELECT DISTINCT product_category FROM products;
"""

result = sql.execute(query)
rows = result.fetchall()

print("\nDistinct categories:")
print(rows)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Distinct categories:
[('Computers',), ('Microphones',), ('Accessories',)]
```

## DROP TABLE

The `DROP TABLE` query deletes an entire table and it's definition from the database. You should usually use the `IF EXISTS` clause with this query to ensure an error isn't thrown if the table you're trying to drop doesn't exist.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

DROP TABLE IF EXISTS users;

SELECT * FROM users;
-- Error: no such table: users
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

# We'll use this twice, so it makes sense to be a function
def display_all_users():
    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


display_all_users()

query = """
    DROP TABLE IF EXISTS users;
"""

sql.execute(query)

# This will throw an error since the `users` table doesn't exist.
display_all_users()
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
Traceback (most recent call last):
  File "/home/daniel/documentation-examples/main.py", line 27, in <module>
    display_all_users()
  File "/home/daniel/documentation-examples/main.py", line 12, in display_all_users
    result = sql.execute(query)
sqlite3.OperationalError: no such table: users
```

## INSERT

Once you've created a table, you'll want to put data in it. The `INSERT` statement is used to add data to a SQL table. You list the column names in the `()` after the table name.

Consider this `users` table definition:

```sql
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
```

If we wanted to fill this table with a few users, we would leave out the `user_id` in the `()` as this table has the `user_id` set to `AUTOINCREMENT`. We would need to add the other two column names in whatever order we wished, though.

**Raw SQL**

```sql
INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
INSERT INTO users (username, password) VALUES ("django", "w0ff");
INSERT INTO users (username, password) VALUES ("alecg", "c0de");

SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
"""
sql.execute(query)

query = """
    INSERT INTO users (username, password) VALUES ("django", "w0ff");
"""
sql.execute(query)

query = """
    INSERT INTO users (username, password) VALUES ("alecg", "c0de");
"""
sql.execute(query)

# Make sure the changes are saved to the DB.
con.commit()

query = """
    SELECT * FROM users;
"""

result = sql.execute(query)
rows = result.fetchall()

print(rows)
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
```

### Inserting multiple rows into a table

If you want to insert multiple rows into a database table, you can use a single `INSERT` statement and group each row in `()`.

**Raw SQL**

```sql
INSERT INTO users (username, password)
VALUES
    ("djs", "mypa$$word"),
    ("django", "w0ff"),
    ("alecg", "c0de");


SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    INSERT INTO users (username, password)
    VALUES
        ("djs", "mypa$$word"),
        ("django", "w0ff"),
        ("alecg", "c0de");
"""

sql.execute(query)
con.commit()

query = """
    SELECT * FROM users;
"""

result = sql.execute(query)
rows = result.fetchall()

print(rows)
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
```

## LIMIT

Sometimes, you may want to get a limited number of rows back from a `SELECT` query. The `LIMIT` clause allows you to do this:

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Only get the first 3 products in the table (by `product_id`)
SELECT * FROM products LIMIT 3;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

# We'll use this a few times so it makes sense for it to be a function
def fetch_and_display_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

fetch_and_display_rows(query)

query = """
    SELECT * FROM products LIMIT 3;
"""

print("\nThe first three products in the table:")
fetch_and_display_rows(query)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

The first three products in the table:
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
```

## OFFSET

If you've ever visited a website like Amazon.com, you know that when you search for a particular product, there are multiple pages of results. The `OFFSET` clause allows you to move the starting point of the returned rows from a query. It's usually used in conjunction with a `LIMIT` clause for things like pagination (as in the Amazon example).

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Only get the first 3 products in the table (by `product_id`)
SELECT * FROM products LIMIT 3;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get the next 3 products in the table
SELECT * FROM products LIMIT 3 OFFSET 3;
┌────────────┬────────────────┬───────────────┬──────────────────┐
│ product_id │  product_name  │ product_price │ product_category │
├────────────┼────────────────┼───────────────┼──────────────────┤
│ 4          │ Logitech M1    │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16 │ 2100.5        │ Computers        │
└────────────┴────────────────┴───────────────┴──────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

# We'll use this a few times so it makes sense for it to be a function
def fetch_and_display_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

fetch_and_display_rows(query)

query = """
    SELECT * FROM products LIMIT 3;
"""

print("\nThe first three products in the table:")
fetch_and_display_rows(query)

query = """
    SELECT * FROM products LIMIT 3 OFFSET 3;
"""

print("\nThe second group of three products in the table:")
fetch_and_display_rows(query)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

The first three products in the table:
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')

The second group of three products in the table:
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
```

## ORDER BY

The `ORDER BY` clause allows you to order rows in ascending (`ASC`) or descending (`DESC`) order alphanumerically. You use it with a `SELECT` query to order the output.

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Ordering products from lowest price to highest price
SELECT * FROM products ORDER BY product_price;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- ASC is the default, so it's the the same as doing nothing after ORDER BY
SELECT * FROM products ORDER BY product_price ASC;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Ordering products from highest price to lowest price
SELECT * FROM products ORDER BY product_price DESC;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

# We'll use this a few times so it makes sense for it to be a function
def fetch_and_display_all_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products ORDER BY product_price;
"""

print("\nProducts ordered from price lowest to highest price:")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products ORDER BY product_price DESC;
"""

print("\nProducts ordered from price highest to lowest price:")
fetch_and_display_all_rows(query)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Products ordered from price lowest to highest price:
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(1, 'Dell XPS 17', 1599.99, 'Computers')
(6, 'MacBook Pro 16', 2100.5, 'Computers')

Products ordered from price highest to lowest price:
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(1, 'Dell XPS 17', 1599.99, 'Computers')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(4, 'Logitech M1', 34.99, 'Accessories')
```

## SELECT

To see what data is in a SQL table, you use the `SELECT` statement.

### Selecting all of the rows and columns from a table

You can `SELECT *` from a table and that'll give you all of the rows in that table along with all the columns. Be aware that the `*` means "Give me all the columns" not "Give me all the rows". All rows are returned from a `SELECT` query unless you begin using filters like `WHERE`, `LIMIT`, or `DISTINCT`.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘
```

When selecting data from Python, you can fetch all of the rows by using the `fetchall()` method of the query result. Note that `fetchall()` returns a `list` of `tuples`, so you would need to do further processing from Python to get the individual rows from this `list`, such as looping through the rows.

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    SELECT * FROM users;
"""

result = sql.execute(query)
rows = result.fetchall()

print(rows)

for row in rows:
    # Using multiple assignment to get the values from each row
    user_id, username, password = row
    print(f"User ID: {user_id}")
    print(f"Username: {username}")
    print(f"Password: {password}")

```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
User ID: 1
Username: djs
Password: mypa$$word
User ID: 2
Username: django
Password: w0ff
User ID: 3
Username: alecg
Password: c0de
```

### Selecting specific columns from a table

If you only want certain columns returned, you can list them separated by commas after the `SELECT` keyword. Notice how the `user_id` column is not present in the result set in the query below.

**Raw SQL**

```sql
SELECT username, password FROM users;
┌──────────┬────────────┐
│ username │  password  │
├──────────┼────────────┤
│ djs      │ mypa$$word │
│ django   │ w0ff       │
│ alecg    │ c0de       │
└──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    SELECT username, password FROM users;
"""

result = sql.execute(query)
rows = result.fetchall()

print(rows)
```

**Output**

```text
[('djs', 'mypa$$word'), ('django', 'w0ff'), ('alecg', 'c0de')]
```

## UPDATE

If you need to change data in a SQL table, the `UPDATE` statement is used. Make sure to use a `WHERE` clause so that you only update the rows you intend to change.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

-- The `djs` user will now have `danielj` as their username.
UPDATE users SET username = "danielj" WHERE user_id = 1;

SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ danielj  │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

# We'll use this twice, so it makes sense to be a function
def display_all_users():
    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


display_all_users()

query = """
    UPDATE users SET username = "danielj" WHERE id = 1;
"""

sql.execute(query)

# Make sure to commit the changes to the DB
con.commit()

display_all_users()
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
[(1, 'danielj', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
```

### Updating multiple columns

If you need to update multiple columns, you can separate the `SET` clauses with commas. We've also put each new SQL command on a new line and added some indentation to make this longer query easier to read.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘

UPDATE users
SET
    username = "danielj", -- note the comma here
    password = "b3tTerpa$$w0rd"
WHERE user_id = 1;

SELECT * FROM users;
┌─────────┬──────────┬────────────────┐
│ user_id │ username │    password    │
├─────────┼──────────┼────────────────┤
│ 1       │ danielj  │ b3tTerpa$$w0rd │
│ 2       │ django   │ w0ff           │
│ 3       │ alecg    │ c0de           │
└─────────┴──────────┴────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

# We'll use this twice, so it makes sense to be a function
def display_all_users():
    query = """
        SELECT * FROM users;
    """

    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


display_all_users()

query = """
    UPDATE users
    SET
        username = "danielj",
        password = "b3tTerpa$$w0rd"
    WHERE user_id = 1;
"""

sql.execute(query)

# Make sure to commit the changes to the DB
con.commit()

display_all_users()
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
[(1, 'danielj', 'b3tTerpa$$w0rd'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
```

## WHERE

To filter the results from a SQL query, use the `WHERE` clause.

**Raw SQL**

```sql
SELECT * FROM users;
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
│ 2       │ django   │ w0ff       │
│ 3       │ alecg    │ c0de       │
└─────────┴──────────┴────────────┘


SELECT * FROM users WHERE username = "djs";
┌─────────┬──────────┬────────────┐
│ user_id │ username │  password  │
├─────────┼──────────┼────────────┤
│ 1       │ djs      │ mypa$$word │
└─────────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

def run_query_and_display_results(query):
    result = sql.execute(query)
    rows = result.fetchall()

    print(rows)


query = """
    SELECT * FROM users;
"""

run_query_and_display_results(query)

query = """
    SELECT * FROM users WHERE username = "djs";
"""

run_query_and_display_results(query)
```

**Output**

```text
[(1, 'djs', 'mypa$$word'), (2, 'django', 'w0ff'), (3, 'alecg', 'c0de')]
[(1, 'djs', 'mypa$$word')]
```

#### Getting a single row from Python when using `WHERE`

If you only need a single row from a `SELECT` statement using a `WHERE` clause in your Python programs, use `fetchone()`. This returns a `tuple` of the data in each column, and you can use techniques like tuple unpacking or indexing to pull the individual values from the `tuple`.

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    SELECT * FROM users WHERE username = "djs";
"""

result = sql.execute(query)
row = result.fetchone()

# This will be a tuple
print(row)

# Getting the values from the row with tuple unpacking
user_id, username, password = row

print(f"User ID: {user_id}")
print(f"Username: {username}")
print(f"Password: {password}")
```

**Output**

```text
(1, 'djs', 'mypa$$word')
User ID: 1
Username: djs
Password: mypa$$word
```

#### Using conditional logic with `WHERE` clauses

There are many operators available to use in a `WHERE` clause. The ones that you can use with numerical data are shown below (`=`, `IN`, and `NOT IN` can also be used with `TEXT` data):

| Operator          | Description                           |
| ----------------- | ------------------------------------- |
| =                 | Equality (works for numbers and TEXT) |
| >                 | Greater-than                          |
| <                 | Less-than                             |
| >=                | Greater-than or equal-to              |
| <=                | Less-than or equal-to                 |
| BETWEEN...AND     | Number is between two values          |
| NOT BETWEEN...AND | Number is not between two values      |
| IN (...)          | Number/Text exists in a list          |
| NOT IN (...)      | Number/Text does not exist in a list  |

Here are examples of a few of the operators on a table of `products`:

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get the product where the `product_name` is "Lenovo ThinkPad".
SELECT * FROM products WHERE product_name = "Lenovo ThinkPad";
┌────────────┬─────────────────┬───────────────┬──────────────────┐
│ product_id │  product_name   │ product_price │ product_category │
├────────────┼─────────────────┼───────────────┼──────────────────┤
│ 8          │ Lenovo ThinkPad │ 950.75        │ Computers        │
└────────────┴─────────────────┴───────────────┴──────────────────┘

-- Get the products that cost less than $1000.
SELECT * FROM products WHERE product_price < 1000;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get the products that cost more than $1000.
SELECT * FROM products WHERE product_price > 1000;
┌────────────┬────────────────────┬───────────────┬──────────────────┐
│ product_id │    product_name    │ product_price │ product_category │
├────────────┼────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17        │ 1599.99       │ Computers        │
│ 3          │ System76 Thelio B1 │ 1255.55       │ Computers        │
│ 6          │ MacBook Pro 16     │ 2100.5        │ Computers        │
└────────────┴────────────────────┴───────────────┴──────────────────┘

-- Get the products whose prices are between $50 and $300 (inclusive).
SELECT * FROM products WHERE product_price BETWEEN 50 AND 300;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get the products that are in the "Microphones" and "Computers" categories.
SELECT * FROM products WHERE product_category IN ("Microphones", "Computers");
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

# We'll use this a few times so it makes sense for it to be a function
def fetch_and_display_all_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products WHERE product_name = "Lenovo ThinkPad";
"""

print("\nLooking for the 'Lenovo ThinkPad':")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products WHERE product_price < 1000;
"""

print("\nProducts cheaper than $1000:")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products WHERE product_price > 1000;
"""

print("\nProducts more expensive than $1000:")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products WHERE product_price BETWEEN 50 AND 300;
"""

print("\nProducts between $50 and $300 (inclusive):")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products WHERE product_category IN ("Microphones", "Computers");
"""

print("\nProducts in the 'Microphones' and 'Computers' categories:")
fetch_and_display_all_rows(query)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Looking for the 'Lenovo ThinkPad':
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Products cheaper than $1000:
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Products more expensive than $1000:
(1, 'Dell XPS 17', 1599.99, 'Computers')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(6, 'MacBook Pro 16', 2100.5, 'Computers')

Products between $50 and $300 (inclusive):
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(7, 'Rode Z28', 275.99, 'Microphones')

Products in the 'Microphones' and 'Computers' categories:
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')
```

#### Complex conditional logic with `WHERE` clauses

You can join multiple `WHERE` clauses with the logical `AND` and `OR` operators to make complex conditional statements, just like in a programming language like Python or JavaScript.

**Raw SQL**

```sql
SELECT * FROM products;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 1          │ Dell XPS 17              │ 1599.99       │ Computers        │
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 3          │ System76 Thelio B1       │ 1255.55       │ Computers        │
│ 4          │ Logitech M1              │ 34.99         │ Accessories      │
│ 5          │ Seagate S1 SSD           │ 88.75         │ Accessories      │
│ 6          │ MacBook Pro 16           │ 2100.5        │ Computers        │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get all microphones less than $200.
SELECT * FROM products
WHERE product_category = "Microphones" AND product_price < 200;
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

-- Get any microphones or computers less than $1000.
SELECT * FROM products
WHERE product_price < 1000 AND product_category IN ("Computers", "Microphones");
┌────────────┬──────────────────────────┬───────────────┬──────────────────┐
│ product_id │       product_name       │ product_price │ product_category │
├────────────┼──────────────────────────┼───────────────┼──────────────────┤
│ 2          │ Blue Snowball Microphone │ 99.5          │ Microphones      │
│ 7          │ Rode Z28                 │ 275.99        │ Microphones      │
│ 8          │ Lenovo ThinkPad          │ 950.75        │ Computers        │
└────────────┴──────────────────────────┴───────────────┴──────────────────┘

```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("products-database.db")
sql = con.cursor()

# We'll use this a few times so it makes sense for it to be a function
def fetch_and_display_all_rows(query):
    result = sql.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)


query = """
    SELECT * FROM products;
"""

fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products
    WHERE product_category = "Microphones" AND product_price < 200;
"""

print("\nGetting microphones less than $200:")
fetch_and_display_all_rows(query)

query = """
    SELECT * FROM products
    WHERE product_price < 1000 AND product_category IN ("Computers", "Microphones");
"""

print("\nComputers and Microphones cheaper than $1000:")
fetch_and_display_all_rows(query)
```

**Output**

```text
(1, 'Dell XPS 17', 1599.99, 'Computers')
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(3, 'System76 Thelio B1', 1255.55, 'Computers')
(4, 'Logitech M1', 34.99, 'Accessories')
(5, 'Seagate S1 SSD', 88.75, 'Accessories')
(6, 'MacBook Pro 16', 2100.5, 'Computers')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')

Getting microphones less than $200:
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')

Computers and Microphones cheaper than $1000:
(2, 'Blue Snowball Microphone', 99.5, 'Microphones')
(7, 'Rode Z28', 275.99, 'Microphones')
(8, 'Lenovo ThinkPad', 950.75, 'Computers')
```
