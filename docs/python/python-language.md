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

You'll also find many *Further Reading* sections, which pull from these excellent Python resources:

- [Python.org Documentation](https://www.python.org/doc/)
- [RealPython.com](https://realpython.com/)
<hr>


## Data Structures

Data structures allow you to efficiently store and access groups of items.

<hr>

### `list`

The `list` data structure is used to store data in ordered "slots". It is known as *mutable sequence type*, which means it can be modified after creation.

Usually, the items in a `list` are homogeneous, which means they represent a group of similar items of the same data type:

```python
names = ["alecg", "danielj", "dimas"]
menu_prices = [4.50, 5.75, 3.00]
ids = [184, 294, 832, 98, 4]
```

#### Accessing individual list items

You can access individual items in a `list` using the `[]` characters and the index number of the item. The index numbers start at 0:

```python
names = ["alecg", "danielj", "dimas"]

print(names[0])  # alecg
print(names[1])  # danielj
print(names[2])  # dimas
```

#### Adding items to a list

To add an item to a `list` after it has been created, you can use the `list.append()` method. This adds the item to the end of the list:

```python
names = ["alecg", "danielj", "dimas"]

names.append("samh")

print(names)  # ['alecg', 'danielj', 'dimas', 'samh']
```

#### Removing items from a list

To remove an item from a `list`, you can use the `list.remove()` method:

```python
names = ["alecg", "danielj", "dimas"]

names.remove("alecg")

print(names)  # ['danielj', 'dimas']
```

If you want to remove an item from a `list` by its index number, use the `list.pop()` method:

```python
names = ["alecg", "danielj", "dimas"]

names.pop(0)

print(names)  # ['danielj', 'dimas']
```

#### Getting the number of items in a list

To get the number of item in a list, use the `len()` function:

```python
names = ["alecg", "danielj", "dimas"]

num_names = len(names)

print(num_names)  # 3
```

#### Checking if an item is contained in a list

To check if an item is contained in a list, use the `in` operator:

```python
names = ["alecg", "danielj", "dimas"]

"alecg" in names  # True
"samh" in names   # False
```

The `in` operator is generally used as part of a conditional statement:

```python
names = ["alecg", "danielj", "dimas"]

if "alecg" in names:
    print("alecg is in the 'names' list")
else:
    print("alecg is NOT in the 'names' list")

if "samh" in names:
    print("samh is in the 'names' list")
else:
    print("samh is NOT in the 'names' list")
```

Example Output:

```text
alecg is in the 'names' list
samh is NOT in the 'names' list
```

#### Looping through a list

To loop through the items in a `list`, use a [`for`](#for) loop. Note the convention of a plural `list` (names) and a singular loop-iteration variable (name):

```python
names = ["alecg", "danielj", "dimas"]

print("This documentation is brought to you by:")
for name in names:
    print(name)
```

Example Output:

```text
This documentation is brought to you by:
alecg
danielj
dimas
```

#### Further Reading

- [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [The Python Library Reference - Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [The Python Library Reference - Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [The Python Library Reference - `len()`](https://docs.python.org/3/library/functions.html#len)

<hr>

## Loops

If you need to repeat something in your programs, you'll need to use one of Python's looping mechanisms.

<hr>

### `for`

#### Looping over a sequence

A `for` loop is generally used to loop over a sequence, such as a `list`:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Example Output:

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

Example Output:

```text
D
a
n
i
e
l
```

#### Counter-controlled repetition

You can combine the `range()` function and the `for` loop to create a counter-controlled loop:

```python
for num in range(1, 4):
    print(f"{num} potato")
```

Example Output:

```text
1 potato
2 potato
3 potato
```

#### Further Reading

- [The Python Tutorial - for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [The Python Tutorial - The range() function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
- [Real Python - Python "for" Loops](https://realpython.com/python-for-loop/)


<hr>

### `while`

#### Indefininte repetition

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

Example Output:

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

Example Output:

```text
What is the meaning of life? To make money
That's incorrect! Please try again.
What is the meaning of life? To eat tacos
That's incorrect! Please try again.
What is the meaning of life? 42
That's correct!
```

#### Counter-controlled repetition

You can use a `while` loop to perform counter-controlled repetition as well, but
the `for` loop with the `range()` function is generally preferred:

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1  # If you forget this, you'll have an infinite loop!
```

Example Output:

```text
0
1
2
3
4
```

#### Further Reading

- [Real Python - Python "while" Loops](https://realpython.com/python-while-loop/)
