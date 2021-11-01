# Python Language

Python is a beginner-friendly language that we use in these courses at CodeWizardsHQ:

|Elementary              | Middle School                          |High School     |
|------------------------|----------------------------------------|----------------|
|Python Game Development |Introduction to Programming with Python |Intro to Python
|                        |Mastering Databases                     |APIs and Databases
|                        |Application Programming Interfaces      |Professional Web App Development
|                        |                                        |Mastering MVC Frameworks
|                        |                                        |Object Relational Mapping

In this section of our documentation, you'll find references to most of the core Python language features and built-in functions that we use in our CodeWizardsHQ courses.

<hr>

### The `for` statement

A `for` statement is generally used to loop over a sequence, such as a `list`:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Example output:

```text
apple
banana
cherry
```

You can also use a `for` statement to loop over the characters in a `str`:

```python
name = "Daniel"

for letter in name:
    print(letter)
```

Example output:

```text
D
a
n
i
e
l
```

You can combine the `range()` function and the `for` statement to create a counter-controlled loop:

```python
for num in range(1, 4):
    print(f"{num} potato")
```

Example output:

```text
1 potato
2 potato
3 potato
```


