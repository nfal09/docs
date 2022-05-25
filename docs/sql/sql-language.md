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

For example, consider the two tables below (which we'll reference throughout these docs):

_users table_

| id  | username | password   |
| --- | -------- | ---------- |
| 1   | djs      | myp@$$word |
| 2   | django   | w0ff       |
| 3   | alecg    | c0de       |

_teachers table_

| id  | user_id | username | is_admin |
| --- | ------- | -------- | -------- |
| 1   | 1       | djs      | true     |
| 2   | 3       | alecg    | false    |

We could get the password of all users that are admins like this:

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
    teachers.is_admin = "true";
┌──────────┬────────────┐
│ username │  password  │
├──────────┼────────────┤
│ djs      │ myp@$$word │
└──────────┴────────────┘
```

There are many different relational database implementations (MySQL, Postgres, etc.) but we use SQLite at CodeWizardsHQ because it is easy to work with and supports most of the common SQL features.

## Why Do We Need SQL?

When working with a database, you need a way to talk to the database and get data into/out of it. SQL is the language we use to do this in a SQLite database. Without SQL, you'd have no way to express relationships in a database in a structured way.

## Why Do We Use Python And SQL Together?

Although you can use raw SQL commands to talk to a SQL database, we use Python at CodeWizardsHQ because often you'll interact with databases this way in the real world. Think about apps you've used that store data about you between visits. That's using a database and a programming language (like Python) to interact with the database!

The SQL portions of a Python DB query will be a Python `str`. Consider this `INSERT` statement in raw SQL:

```text
INSERT INTO users (username, password) VALUES ("djs", "myp@$$word");
```

To run that from Python, we would do this:

```python
import sqlite3

con = sqlite3.connect("my-database.db")
sql = con.cursor()

query = """
    INSERT INTO users (username, password) VALUES ("djs", "myp@$$word");
"""

sql.execute(query)
con.commit()
```

The important thing to remember is that the `query` is just a `str` that you pass to `sql.execute()`. If you make a change to a table in the database (as we did above) then you use the `con.commit()` method to save the change.

## CREATE TABLE

Relational databases are made up of tables, and you'll need to create tables to hold your data if we don't provide one for you. We use `IF NOT EXISTS` because we'll run the statement every time our Python script runs, and an error would occur if you tried to create a table that already existed. Most tables should also have a `PRIMARY KEY` integer to uniquely identify each row of data.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL
);
```

## INSERT

Once you've created a table, you'll want to put data in it. The `INSERT` statement is used to add data to a SQL table. You list the column names in the `()` after the table name, and notice that we leave out the `id` as this table has the `id` set to `AUTOINCREMENT`:

```sql
INSERT INTO users (username, password) VALUES ("djs", "myp@$$word");
INSERT INTO users (username, password) VALUES ("django", "w0ff ");
INSERT INTO users (username, password) VALUES ("alecg", "c0de");
```

## UPDATE

If you need to change data in a SQL table, the `UPDATE` statement is used. Make sure to use a `WHERE` clause so that you only update the rows you intend to change:

```sql
UPDATE users SET username = "DJS" WHERE id = 1;
```
