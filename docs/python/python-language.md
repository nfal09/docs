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


## Data Structures

Data structures allow you to efficiently store and access groups of items.

### `list`

The `list` data structure is used to store data in ordered "slots". It is known as *mutable sequence type*, which means it can be modified after creation.

Usually, the items in a `list` are homogeneous, which means they represent a group of similar items of the same data type:

```python
names = ["alecg", "danielj", "dimas"]
menu_prices = [4.50, 5.75, 3.00]
ids = [184, 294, 832, 98, 4]
```

You can access individual items in a `list` using the `[]` characters and the index number of the item. The index numbers start at 0:

```python
names = ["alecg", "danielj", "dimas"]

print(names[0])  # alecg
print(names[1])  # danielj
print(names[2])  # dimas
```

To add an item to a `list` after it has been created, you can use the `list.append()` method. This adds the item to the end of the list:

```python
names = ["alecg", "danielj", "dimas"]

names.append("samh")

print(names)  # ['alecg', 'danielj', 'dimas', 'samh']
```

Further Reading

- [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [The Python Library Reference - Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [The Python Library Reference - Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

<hr>

## Loops

If you need to repeat something in your programs, you'll need to use one of Python's looping mechanisms.

### `for`

A `for` loop is generally used to loop over a sequence, such as a `list`:


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

You can also use a `for` loop to loop over the characters in a `str`:

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

You can combine the `range()` function and the `for` loop to create a counter-controlled loop:

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

Further Reading

- [The Python Tutorial - for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [The Python Tutorial - The range() function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
- [Real Python - Python "for" Loops](https://realpython.com/python-for-loop/)


<hr>

### `while`

A `while` loop is generally used to perform indefinite repetition (when you don't know how many times you want to loop).

For example, you can use a `while` loop to ask a user something until they answer correctly:

```python
keep_looping = True  # This variable controls whether we loop or not.

while keep_looping:
    user_guess = input("What is the meaning of life? ")
    
    if user_guess == "42":
        print("That's correct!")
        keep_looping = False  # Stops the loop.
    else:
        print("That's incorrect! Please try again.")
```

Example output:

```text
What is the meaning of life? To make money
That's incorrect! Please try again.
What is the meaning of life? To eat tacos
That's incorrect! Please try again.
What is the meaning of life? 42
That's correct!
```

You can also use a `break` statement instead of using a variable to control how many times an indefinite `while` loop runs:

```python
while True:
    user_guess = input("What is the meaning of life? ")
    
    if user_guess == "42":
        print("That's correct!")
        break  # Stops the loop.
    else:
        print("That's incorrect! Please try again.")
```

Example output:

```text
What is the meaning of life? To make money
That's incorrect! Please try again.
What is the meaning of life? To eat tacos
That's incorrect! Please try again.
What is the meaning of life? 42
That's correct!
```

You can use a `while` loop to perform counter-controlled repetition as well, but
the `for` loop with the `range()` function is generally preferred:

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1  # If you forget this, you'll have an infinite loop!
```

Example output:

```text
0
1
2
3
4
```

Further Reading

- [Real Python - Python "while" Loops](https://realpython.com/python-while-loop/)
