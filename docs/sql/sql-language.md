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
