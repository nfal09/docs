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

You'll also find many *Further reading* sections, which pull from these excellent Python resources:

- [Python.org Documentation](https://www.python.org/doc/)
- [RealPython.com](https://realpython.com/)
- [Think Python](https://greenteapress.com/wp/think-python-2e/)
<hr>


## Conditional Statements

Conditional statements allow you to run a block of code when a boolean condition is true. 

<hr>

### `if`

The `if` statement is the simplest form of conditional statement. If the expression to the right of the `if` keyword is `True`, the indented code block will execute:

```python
is_hungry = True

if is_hungry:
    print("You should eat!")

```

Example Output:

```text
You should eat!
```

Usually, a conditional expression uses [comparison operators](#comparison-operators) to generate a `bool` result:

```python
age = 19

if age >= 18:
    print("You are legally an adult, congrats!")

```

Example Output:

```text
You are legally an adult, congrats!
```

### `elif`

The `elif` conditional statement is used to string a group of *logically related* conditional statements together. The first conditional expression that evaluates to `True` will run:

```python
favorite_food = "Tacos"

if favorite_food == "Sushi":
    print("We're going out for Japanese food to night!")
elif favorite_food == "Pasta":
    print("How about we eat some Italian food tonight?")
elif favorite_food == "Tacos":
    print("Time for some Mexican food!")
elif favorite_food == "Samosa":
    print("Let's eat Indian food tonight!")
```

Example Output:

```text
Time for some Mexican food!
```

### `else`

The `else` conditional statement runs when all other conditional statements in a group are `False`:

```python
favorite_food = "Hot Dogs with Cream Cheese"

if favorite_food == "Sushi":
    print("We're going out for Japanese food to night!")
elif favorite_food == "Pasta":
    print("How about we eat some Italian food tonight?")
elif favorite_food == "Tacos":
    print("Time for some Mexican food!")
elif favorite_food == "Samosa":
    print("Let's eat Indian food tonight!")
else:
    print("I don't know what that favorite_food is!")
```

```text
I don't know what that favorite_food is!
```


### `Comparison Operators`

Here are the comparison operators that you can use in conditional expressions to generate a `bool` value:


|Operator| Description               |
|--------|---------------------------|
| `>`    | Greater-than              |
| `>=`   | Greater-than or equal-to  |
| `<`    | Less-than                 |
| `<=`   | Less-than or equal-to     |
| `==`   | Equal-to                  |
| `!=`   | Not equal-to              |


### `Complex Conditional Statements`

Complex conditional statements involve combining more than one conditional expression with [logical operators](#logical-operators):

```python
age = 15
height_in_feet = 4.6

if age >= 13 and height_in_feet > 5:
    print("You may ride the roller coaster.")
else:
    print("You may NOT ride the roller coaster.")
```

Example Output:

```text
You may NOT ride the roller coaster.
```

### `Logical Operators`

Logical operators allow you to combine multiple conditional expressions in a single conditional statement:

|Operator| Description                                         |
|--------|-----------------------------------------------------|
| `and`  | `True` when both conditional expressions are `True` |
| `or`   | `True` when either conditional expression is `True` |
| `not`  | Reverses the value of a conditional expression      |

#### Using the '`and`' operator

The `and` operator evaluates to `True` when both conditional expressions are `True`:

```python
age = 15
height_in_feet = 5.2

if age >= 13 and height_in_feet > 5:
    print("You may ride the roller coaster.")
else:
    print("You may NOT ride the roller coaster.")
```

Example Output:

```text
You may ride the roller coaster.
```

#### Using the '`or`' operator

The `or` operator evaluates to `True` when either conditional expression is `True`:

```python
is_hungry = True
is_thirsty = False

if is_hungry or is_thirsty:
    print("You should go to the kitchen.")
else:
    print("Do whatever, you're good!")
```

Example Output:

```text
You should go to the kitchen.
```

#### Using the '`not`' operator

The `not` operator reverses a conditional expression:

```python
is_tired = True

if not is_tired:
    print("Let's go outside and play.")
else:
    print("Let's take a nap.")
```

Example Output:

```text
Let's take a nap.
```

### Further reading

- [Real Python - Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
- [Real Python - Using the `not` Boolean Operator in Python](https://realpython.com/python-not-operator/)
- [Real Python - Using the `and` Boolean Operator in Python](https://realpython.com/python-and-operator/)
- [Real Python - How to use the Python `or` Operator ](https://realpython.com/python-or-operator/)
- [The Python Library Reference - Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [The Python Library Reference - Boolean Values](https://docs.python.org/3/library/stdtypes.html#boolean-values)
- [The Python Library Reference - Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
- [The Python Library Reference - Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [The Python Tutorial - `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Think Python - Conditionals and Recursion](https://greenteapress.com/thinkpython2/html/thinkpython2006.html)





## Data Types

Every value has a data type in Python. The data type determines what kinds of operations you can perform on the value.

<hr>

### `bool`

The `bool` data type represents a `True` or a `False` value:

```python
is_hungry = True
is_thirsty = False
```

You normally won't use a `bool` directly, but instead will generate a `bool` through a conditional expression:

```python
age = 19

# This generates `True`
if age >= 18:
    print("You are an adult!")


# This generates `False`
if age < 18:
    print("You are a child.")
```

### `float`

The `float` data type represents a decimal number:

```python
total_cost = 29.99
```

### `int`

The `int` data type represents a whole number:

```python
num_tacos_eaten = 12
```

### `str`

The `str` data type represents a text value:

```python
my_name = "Daniel"
```

### Further reading

- [The Python Library Reference - Text Sequence Type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [The Python Library Reference - Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Think Python - Values and Types](https://greenteapress.com/thinkpython2/html/thinkpython2002.html#sec10)
- [Think Python - Strings](https://greenteapress.com/thinkpython2/html/thinkpython2009.html)



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



#### Accessing items in a list

You can access individual items in a `list` using the `[]` characters and the index number of the item. The index numbers start at 0:

```python
names = ["alecg", "danielj", "dimas"]

print(names[0])  # alecg
print(names[1])  # danielj
print(names[2])  # dimas
```



#### Adding an item to a list

To add an item to a `list` after it has been created, you can use the `list.append()` method. This adds the item to the end of the list:

```python
names = ["alecg", "danielj", "dimas"]

names.append("samh")

print(names)  # ['alecg', 'danielj', 'dimas', 'samh']
```



#### Updating an item in a list

To update a `list` item, replace the value at the index:

```python
names = ["alecg", "danielj", "dimas"]

names[1] = "django"

print(names)  # ['alecg', 'django', 'dimas']
```


#### Removing an item from a list

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



#### Further reading

- [The Python Library Reference - Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [The Python Library Reference - Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [The Python Library Reference - `len()`](https://docs.python.org/3/library/functions.html#len)
- [The Python Tutorial - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Think Python - Lists](https://greenteapress.com/thinkpython2/html/thinkpython2011.html)

<hr>


### `dict`

The `dict` data structure is used to store data in key/value pairs:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}
```

#### Accessing items in a dict

You have to know the key to access an individual item in a `dict`:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

daniel_job = staff["danielj"]
print(f"Daniel is a {daniel_job}.")  # Daniel is a Curriculum Developer.

alec_job = staff["alecg"]
print(f"Alec is a {alec_job}.")  # Alec is a Curriculum Instructor.

dima_job = staff["dimas"]
print(f"Dima is a {dima_job}.")  # Dima is a Designer.
```


#### Adding an item to a dict

You can add an item to a `dict` by providing the key/value pair (it's the same syntax as updating an item):


```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

staff["django"] = "Director Of Pug Snorts"

print(staff)  # {'danielj': 'Curriculum Developer', 'alecg': 'Curriculum Instructor', 'dimas': 'Designer', 'django': 'Director Of Pug Snorts'}
```


#### Updating an item in a dict

To update an item in a `dict`, you must know the key:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

staff["danielj"] = "Burrito Taste-Tester"

print(staff)  # {'danielj': 'Burrito Taste-Tester', 'alecg': 'Curriculum Instructor', 'dimas': 'Designer'}
```



#### Removing an item from a dict

To remove an item from a `dict`, use the `dict.pop()` method:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

staff.pop("danielj")

print(staff)  # {'alecg': 'Curriculum Instructor', 'dimas': 'Designer'}
```


#### Looping through a dict

The previous example would be easier if we used a loop to print each user's job. To loop through a `dict`, you generally use the `dict.items()` method like this:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

for name, job in staff.items():
    print(f"{name} is a {job}.")

```

Example Output:

```text
danielj is a Curriculum Developer.
alecg is a Curriculum Instructor.
dimas is a Designer.
```






#### Getting the keys from a dict

If you need to get all of the keys from a `dict`, use the `dict.keys()` method. Note, you'll need to cast the result to a `list`, which is why the `list()` function is used here:


```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

names = list(staff.keys())

print(f"Here are all the names in the staff dict: {names}")
```

Example Output:

```text
Here are all the names in the staff dict: ['danielj', 'alecg', 'dimas']
```

#### Getting the values from a dict

If you need to get all of the keys from a `dict`, use the `dict.values()` method. Note, you'll need to cast the result to a `list`, which is why the `list()` function is used here:


```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

jobs = list(staff.values())

print(f"Here are all the jobs in the staff dict: {jobs}")
```

Example Output:

```text
Here are all the jobs in the staff dict: ['Curriculum Developer', 'Curriculum Instructor', 'Designer']
```

#### Getting the number of items in a dict

You can use the `len()` function to get the number of items in a `dict`:

```python
staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

number_of_staff = len(staff)

print(f"We have {number_of_staff} people on our staff.")  # We have 3 people on our staff.
```



#### Further reading

- [Real Python - Dictionaries in Python](https://realpython.com/python-dicts/)
- [The Python Library Reference - Mapping Types: `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [The Python Tutorial - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Think Python - Dictionaries](https://greenteapress.com/thinkpython2/html/thinkpython2012.html)


<hr>


## Functions

Functions allow you to group related statements together to perform a task. 

<hr>

### Built-in functions

Python comes with many built-in functions. We'll cover some of the most common that you'll see in CodeWizardsHQ courses below. 

##### `float()`

The `float()` function converts data to a `float`:

```python
pi = float("3.14")

print(pi)  # 3.14
type(pi)  # <class 'float'>

two = float(2)

print(two)  # 2.0
type(two)  # <class 'float'>
```

##### `input()`

The `input()` function allows you to prompt a user. The user's response is returned as a `str`, which you can store in a variable:

```python
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
```

Example Output:

```text
What is your name? Daniel
Nice to meet you, Daniel!
```

##### `int()`

The `int()` function converts data to an `int`:

```python
int_pi = int(3.14)

print(int_pi)  # 3
type(int_pi)  # <class 'int'>

meaning_of_life = int("42")

print(meaning_of_life)  # 42
type(meaning_of_life)  # <class 'int'>
```

##### `len()`

The `len()` function returns the length of a sequence such as a `list` or `str`:

```python
number_of_characters = len("How many characters are in this str?")
print(number_of_characters)  # 36

favorite_foods = ["tacos", "pizza", "nachos", "burritos"]

number_of_foods = len(favorite_foods)
print(number_of_foods)  # 4
```


##### `list()`

The `list()` function creates a list from a sequence such as the result of `dict.keys()`, `dict.values()`, or a `str`:

```python
character_list = list("Hello!")
print(character_list)  # ['H', 'e', 'l', 'l', 'o', '!']

staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
}

names = list(staff.keys())
print(names)  # ['danielj', 'alecg', 'dimas']

jobs = list(staff.values())
print(jobs)  # ['Curriculum Developer', 'Curriculum Instructor', 'Designer']
```


##### `print()`

The `print()` function displays text on the screen:

```python
print("Hello, world!")  # Hello, world!
```


##### `range()`

The `range()` function is mainly used for [counter-controlled repetition](#counter-controlled-repetition) with a `for` loop:

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


##### `sorted()`

The `sorted()` function is used to sort a `list`:

```python
names = ["danielj", "alecg", "dimas"]
sorted_names = sorted(names)

print(sorted_names)  # ['alecg', 'danielj', 'dimas']
```

You can pass keyword arguments to the `sorted()` function to customize the way the `list` is sorted.

For example, the `key` argument can be a function to run on each item of the `list` before sorting:

```python
names = ["Danielj", "alecg", "Dimas"]
sorted_names = sorted(names)

# Notice how these aren't sorted correctly? Uppercase letters are "smaller"
# than lowercase letters in the sorting algorithm that `sort()` uses!
print(sorted_names)  # ['Danielj', 'Dimas', 'alecg']

sorted_names = sorted(names, key=str.lower)

# Now, everything is sorted correctly, and the original values haven't been
# changed. `sort()` only uses the `key` function during the sorting process.
print(sorted_names)  # ['alecg', 'Danielj', 'Dimas']
```
The `reverse` keyword argument of `sort()` is used to sort from high-to-low instead of low-to-high. It expects a `bool` value:

```python
names = ["danielj", "alecg", "dimas"]
reverse_sorted_names = sorted(names, reverse=True)

print(reverse_sorted_names)  # ['dimas', 'danielj', 'alecg']
```

##### `str()`

The `str()` function turns its argument into a `str` data type. This comes in handy if you have a number but want to treat it like a `str`:

```python
meaning_of_life = 42
print("The meaning of life is " + str(meaning_of_life)) 
```

Example Output:

```text
The meaning of life is 42
```

If you use `f-strings`, you don't have to worry about converting numbers to `str` when working with `str` data:

```python
meaning_of_life = 42
print(f"The meaning of life is {meaning_of_life}")
```

Example Output:

```text
The meaning of life is 42
```


#### Further reading

- [The Python Library Reference - Built-in Functions](https://docs.python.org/3/library/functions.html)




<hr>

### User-defined functions

You define a function using the `def` keyword:

```python
def say_hello():
    print("Hello!")


```

#### Calling a function

Defining a function does not run the statements in the body of the function. To run a function, you *call* it like this:

```python
def say_hello():
    print("Hello!")


say_hello()  # Hello!

```

#### Adding parameters to a function

When you define a function, you can add parameters that the function caller should pass in. Parameters are like variables, but the value of the variable is set by the function caller, not the function definer:

```python
def say_hello(name):
    print(f"Hello, {name}!")

```

#### Passing arguments to a function

If a function accepts parameters, you need to pass them in when you call the function:


```python
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Daniel")  # Hello, Daniel!
```

#### Returning a value from a function

You can return a value from a function by using the `return` keyword:

```python
def add(number_1, number_2):
    total = number_1 + number_2
    return total

```

#### Capturing a function's return value

If a function returns a value, you should capture it in a varible:

```python
def add(number_1, number_2):
    total = number_1 + number_2
    return total


total = add(2, 3)
print(total)  # 5
```

You can also use the value immediately in a `print()` statement:

```python
def add(number_1, number_2):
    total = number_1 + number_2
    return total


print(add(2, 3))  # 5
print(f"2 + 3 = {add(2, 3)}")  # 2 + 3 = 5
```

#### Further reading

- [Real Python - Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
- [The Python Tutorial - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Think Python - Functions](https://greenteapress.com/thinkpython2/html/thinkpython2004.html)
- [Think Python - Fruitful Functions](https://greenteapress.com/thinkpython2/html/thinkpython2007.html)

<hr>





## Loops

If you need to repeat something in your programs, you'll need to use one of Python's looping mechanisms.

<hr>

### `for`

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

#### Further reading

- [Real Python - Python `for` Loops](https://realpython.com/python-for-loop/)
- [The Python Tutorial - `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [The Python Tutorial - The `range()` function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
- [Think Python - Traversal with a `for` loop](https://greenteapress.com/thinkpython2/html/thinkpython2009.html#sec94)

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

#### Further reading

- [Real Python - Python `while` Loops](https://realpython.com/python-while-loop/)
- [Think Python - The `while` statement](https://greenteapress.com/thinkpython2/html/thinkpython2008.html#sec84)
