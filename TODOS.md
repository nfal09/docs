# TODOs

## Browser APIs and jQuery

### Browser Dev Tools

-   Something about how to use the `Elements` tab to adjust HTML and styling

### jQuery's `val()` function

-   Can be in the same spot as the `attr()` stuff

<hr>

## HTML

### Directory Navigation

-   Show how to add different resources using `<img>` and `<video>` that live in different places in a project, such as:
    -   Project root
    -   Nested folder
    -   Parent folder

<hr>

## CSS

### The `Box` Model

[The Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

-   Two main categories: `block` and `inline`
    -   Can change an element's `display` to either.
-   Discuss how `width`, `height`, `padding`, `border`, and `margin` affect a box
    -   Can show shorthand/longhand versions of `margin`, `border`, and `padding`

[Inline Block](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#using_display_inline-block)

### Styling Text

[Styling Text](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)

-   Need to cover things like changing font size/color/family.
-   Could also show text decoration and text shadow.
-   Alignment would be good too.

### Layouts

[Layouts](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Introduction)

-   Should cover changing the `position` property.
-   Flexbox

<hr>

## SQL

### What Is A Relational Database?

-   Discuss how a relational DB is like a spreadsheet of rows/cols
-   Discuss different "flavors" of relational DBs (MySQL, Postgres, etc.) and talk about why we use SQLite at CWHQ

### Why Do We Need SQL?

-   It let's us ask questions about datasets in a concise way
-   Can maybe show some examples here of complex queries and their English equivalents, such as:
    -   English: "How many students in `Intro To Python` have a grade of 60 or below"
    -   SQL: SELECT COUNT(\*) FROM students WHERE course_name = "Intro To Python" AND grade <= 60;

### Why Do We Use Python and SQL Together?

-   Applications often need to store data in a DB and then retrieve/modify that data.
-   We use Python to interact with SQL DBs at CWHQ because we focus on application development
-   You can also use SQL directly with a DB instead of as part of a Python (or any other language) application.

### Example Table definitions for these docs

-   We should have a fairly straightforward definition of two to three tables here that students will see in all examples.

### `CREATE TABLE`

-   [Creating Tables](https://sqlbolt.com/lesson/creating_tables)
-   [SQLite Create Table](https://www.sqlitetutorial.net/sqlite-create-table/)
-   Should discuss column names, constraints, and data types
-   Don't forget to mention the pitfalls of `IF NOT EXISTS` and how to delete a DB and start over if you create a table with a bad table definition

### `INSERT`

-   [Inserting Rows](https://sqlbolt.com/lesson/inserting_rows)
-   [SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)
-   Make sure to show single row and multi row versions
-   Show that column list can leave out `PRIMARY KEY`

### `UPDATE`

-   [Updating Rows](https://sqlbolt.com/lesson/updating_rows)
-   [SQLite Update](https://www.sqlitetutorial.net/sqlite-update/)
-   Should show simple updates and updates that use `LIMIT` or `OFFSET`

### `DELETE`

-   [Deleting Rows](https://sqlbolt.com/lesson/deleting_rows)
-   [SQLite DELETE](https://www.sqlitetutorial.net/sqlite-delete/)

### `ALTER`

-   [Altering tables](https://sqlbolt.com/lesson/altering_tables)
-   [SQLite Alter table](https://www.sqlitetutorial.net/sqlite-alter-table/)
-   Show renaming a table, adding a new column, and renaming a column

### `DROP`

-   [Dropping Tables](https://sqlbolt.com/lesson/dropping_tables)
-   [SQLite Drop Table](https://www.sqlitetutorial.net/sqlite-drop-table/)
-   Make sure to talk about `IF EXISTS` here

### `SELECT`

-   [SELECT queries introduction](https://sqlbolt.com/lesson/select_queries_introduction)
-   [SQLite SELECT](https://www.sqlitetutorial.net/sqlite-select/)
-   Just focus on simple `SELECT` queries here, we'll cover all the different constraints one-by-one in dedicated sections

#### Order of execution of SELECT queries

-   [Order of execution](https://sqlbolt.com/lesson/select_queries_order_of_execution)
-   This is an important topic to cover, as it may be something we miss in courses

### `WHERE`

-   [Queries with constraints](https://sqlbolt.com/lesson/select_queries_with_constraints)
-   [Queries with constraints pt 2](https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2)
-   [SQLite WHERE](https://www.sqlitetutorial.net/sqlite-where/)
-   This is similar to a conditional statement
-   Used as a way to filter the result set from a `SELECT` statement
-   Show numerical and text data filters

### `DISTINCT`

-   [Filtering and sorting query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)
-   [SQLite Distinct](https://www.sqlitetutorial.net/sqlite-distinct/)
-   Used to remove duplicate row data

### `ORDER BY`

-   [Filtering and sorting query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)
-   [SQLite order by](https://www.sqlitetutorial.net/sqlite-order-by/)
-   Used to order results in `ASC` or `DESC` order
-   Show how to order by one or more than one column

### `LIMIT`

-   [Filtering and sorting query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)
-   [SQLite Limit](https://www.sqlitetutorial.net/sqlite-limit/)
-   Used to limit the number of results returned from a query

### `OFFSET`

-   [Filtering and sorting query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)
-   [SQLite Limit](https://www.sqlitetutorial.net/sqlite-limit/)
-   Used in conjunction with `LIMIT` to offset the result set

### `JOIN`

-   [Select queries with joins](https://sqlbolt.com/lesson/select_queries_with_joins)
-   [SQLite Join](https://www.sqlitetutorial.net/sqlite-join/)
-   [SQLite Inner Join](https://www.sqlitetutorial.net/sqlite-inner-join/)
-   Only need to show `INNER JOIN`, but use `JOIN` since that's all we use at CWHQ

### `NULL`

-   [Select queries with nulls](https://sqlbolt.com/lesson/select_queries_with_nulls)
-   [SQLite is null](https://www.sqlitetutorial.net/sqlite-is-null/)
-   Used to indicate we don't have a valid value for a piece of data
-   Used in the `WHERE` clause with `IS` or `IS NOT`

### `AS`

-   [Select Queries with expressions](https://sqlbolt.com/lesson/select_queries_with_expressions)
-   Basic way to alias some expression after a `SELECT` clause
-   Often combined with Aggregate functions

### `HAVING`

-   [Select queries with aggregates pt. 2](https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2)
-   [SQLite Having](https://www.sqlitetutorial.net/sqlite-having/)
-   Used to filter rows that have already been grouped with `GROUP BY` or by an aggregate function

### Aggregate Functions

-   COUNT, MIN, MAX, AVG, SUM

<hr>

## Jinja Templating

### Looping

### Conditionals

### Macros

### Assignments

-   This is the `set` keyword stuff

### Statements/Expressions/Comments

-   Difference between each beesting version

### Variables

### Filters

-   Just list a few of the common ones we use

### Template Inheritance
