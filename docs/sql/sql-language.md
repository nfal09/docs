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

| id  | username | password   |
| --- | -------- | ---------- |
| 1   | djs      | mypa$$word |
| 2   | django   | w0ff       |
| 3   | alecg    | c0de       |

_teachers table_

| id  | user_id | username | is_admin |
| --- | ------- | -------- | -------- |
| 1   | 1       | djs      | 1        |
| 2   | 3       | alecg    | 0        |

We could get the password of all users that are teachers and admins like this:

```sql
SELECT
    users.username, users.password
FROM
    users
JOIN
    teachers
USING
    (id)
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

con = sqlite3.connect("my-database.db")
sql = con.cursor()

query = """
    INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
"""

sql.execute(query)
con.commit()
```

The important thing to remember is that the `query` is just a `str` that you pass to `sql.execute()`. If you make a change to a table in the database (as we did above) then you use the `con.commit()` method to save the change. The semi-colon (`;`) isn't required when using a query from Python, but we'll keep it for consistency between the raw SQL examples.

## CREATE TABLE

Relational databases are made up of tables, and you'll need to create tables to hold your data if we don't provide one for you. We often use `IF NOT EXISTS` in CWHQ courses (except those that are full-stack **Flask** apps) when creating a table because we'll run the statement every time our Python script runs, and an error would occur if you tried to create a table that already existed. Most tables should also have a `PRIMARY KEY` integer to uniquely identify each row of data.

**Raw SQL**

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT UNIQUE NOT NULL
    );
"""

sql.execute(query)
```

## INSERT

Once you've created a table, you'll want to put data in it. The `INSERT` statement is used to add data to a SQL table. You list the column names in the `()` after the table name. If we're thinking of this table as the same `users` table from the previous section, you can notice we leave out the `id` in the `()` as this table has the `id` set to `AUTOINCREMENT`.

**Raw SQL**

```sql
INSERT INTO users (username, password) VALUES ("djs", "mypa$$word");
INSERT INTO users (username, password) VALUES ("django", "w0ff");
INSERT INTO users (username, password) VALUES ("alecg", "c0de");
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

con.commit()
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
```

## SELECT

To see what data is in a SQL table, you use the `SELECT` statement.

### Selecting all of the rows and columns from a table

You can `SELECT *` from a table and that'll give you all of the rows in that table along with all the columns.

**Raw SQL**

```sql
SELECT * FROM users;
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ djs      │ mypa$$word │
│ 2  │ django   │ w0ff       │
│ 3  │ alecg    │ c0de       │
└────┴──────────┴────────────┘
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
    # Using tuple unpacking to get the values from each row
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

If you only want certain columns returned, you can list them separated by commas after the `SELECT` keyword. Notice how the `id` column is not present in the result set in the query below.

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

## WHERE

To filter the results from a SQL query, use the `WHERE` clause.

**Raw SQL**

```sql
SELECT * FROM users WHERE username = "djs";
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ djs      │ mypa$$word │
└────┴──────────┴────────────┘
```

**Python + SQL**

```python
import sqlite3

con = sqlite3.connect("users-database.db")
sql = con.cursor()

query = """
    SELECT * FROM users WHERE username = "djs";
"""

result = sql.execute(query)
rows = result.fetchall()

print(rows)
```

**Output**

```text
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

## UPDATE

If you need to change data in a SQL table, the `UPDATE` statement is used. Make sure to use a `WHERE` clause so that you only update the rows you intend to change.

**Raw SQL**

```sql
SELECT * FROM users;
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ djs      │ mypa$$word │
│ 2  │ django   │ w0ff       │
│ 3  │ alecg    │ c0de       │
└────┴──────────┴────────────┘
UPDATE users SET username = "danielj" WHERE id = 1;
SELECT * FROM users;
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ danielj  │ mypa$$word │
│ 2  │ django   │ w0ff       │
│ 3  │ alecg    │ c0de       │
└────┴──────────┴────────────┘
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

## DELETE

To remove data in a SQL table, use the `DELETE` statement. Make sure to use a `WHERE` clause so that you only delete the rows you intend to.

**Raw SQL**

```sql
SELECT * FROM users;
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ djs      │ mypa$$word │
│ 2  │ django   │ w0ff       │
│ 3  │ alecg    │ c0de       │
└────┴──────────┴────────────┘
DELETE FROM users WHERE id = 3;
SELECT * FROM users;
┌────┬──────────┬────────────┐
│ id │ username │  password  │
├────┼──────────┼────────────┤
│ 1  │ djs      │ mypa$$word │
│ 2  │ django   │ w0ff       │
└────┴──────────┴────────────┘
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
