# JavaScript Language

JavaScript is the language that powers the interactive web! JavaScript is the primary language in these courses at CodeWizardsHQ:

|Elementary                        | Middle School                           |High School     |
|----------------------------------|-----------------------------------------|----------------
| Intro to Real World Programming  | Interactive Web with JavaScript         | Fundamentals of Web Development
| Capstone I Minecraft             | Capstone I Virtual Reality Game         | User Interface Development
| Fundamental Programming Concepts | User Interface Development              | APIs and Databases
| Web Development for Kids – 2     | Application Programming Interfaces      | 
|                                  | Capstone II Online Multiplayer Gaming   |

In this section of our documentation, you'll find references to most of the core JavaScript language features and built-in functions that we use in our CodeWizardsHQ courses.

You'll also find many *Further reading* sections, which pull from these excellent JavaScript resources:

- [MDN JavaScript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [The Modern JavaScript Tutorial](https://javascript.info/)
- [Eloquent JavaScript](https://eloquentjavascript.net/)

<hr>




## Comments

Programmers use comments to make notes in their source code for themselves or other programmers that will read their code later. They can also be used to "deactivate" lines of code that you don't want to run while you're working on a program.

### Single Line Comments

Single line comments are denoted by the `//` characters. You can put them above or to the right of the line of code they reference:

```javascript
// Validate the user is logged in and redirect them to the appropriate page.
if (isLoggedIn(user)) {
    redirectToHomepage();
} else {
    redirectToLogin();
}


var minHeight = 60  // This is measured in inches, not feet!
```

### Deactivating Code

You can deactivate sections of code with comments:

```javascript
if (age < 18) {
    // Turning this off for now
    // prompt_user();
    redirectToKidZone();
} else {
    loginUser();
}

```

### Multiline Comments

Multiline comments start with `/*` and end with `*/`

```javascript
/*
This calculates the hypotenuse of a right triangle when given the sides
of the right triangle. It's the Pythagorean Theorem. The ** is how you
write exponents in JavaScript, and fractional exponents are like roots,
so 0.5 is the square root.
*/
var hypotenuse = ((sideA ** 2) + (sideB ** 2)) ** 0.5
```

Many programmers perfer to put `*` on each line of a multiline comment and indent a bit for clarity:

```javascript
/*
*   This calculates the hypotenuse of a right triangle when given the sides
*   of the right triangle. It's the Pythagorean Theorem. The ** is how you
*   write exponents in JavaScript, and fractional exponents are like roots,
*   so 0.5 is the square root.
*/
var hypotenuse = ((sideA ** 2) + (sideB ** 2)) ** 0.5
```

### Further reading

- [MDN - JavaScript Basics: Comments](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics#comments)
- [Eloquent JavaScript - Comments](https://eloquentjavascript.net/02_program_structure.html#h_/OBuIOX390)
- [The Modern JavaScript Tutorial - Comments](https://javascript.info/comments)

<hr>






## Conditional Statements

Conditional statements allow you to run a block of code when a boolean condition is true. 

### `if`

The `if` statement is the simplest form of conditional statement. If the expression to the right of the `if` keyword is `true`, the indented code block will execute:

```javascript
var isHungry = true;

if (isHungry) {
    console.log("You should eat!");
}
```

Example Output:

```text
You should eat!
```

Usually, a conditional expression uses [comparison operators](#comparison-operators) to generate a `boolean` result:

```javascript
var age = 19;

if (age >= 18) {
    console.log("You are legally an adult, congrats!");
}
```

Example Output:

```text
You are legally an adult, congrats!
```

### `else if`

The `else if` conditional statement is used to group *logically related* conditional statements together. The first conditional expression that evaluates to `true` will run:

```javascript
var favoriteFood = "Tacos";

if (favoriteFood == "Sushi") {
    console.log("We're going out for Japanese food to night!");
} else if (favoriteFood == "Pasta") {
    console.log("How about we eat some Italian food tonight?");
} else if (favoriteFood == "Tacos") {
    console.log("Time for some Mexican food!");
} else if (favoriteFood == "Samosa") {
    console.log("Let's eat Indian food tonight!");
}
```

Example Output:

```text
Time for some Mexican food!
```

### `else`

The `else` conditional statement runs when all other conditional statements in a group are `false`. You can think of it as the *default* option:

```javascript
var favoriteFood = "Hot Dogs with Cream Cheese";

if (favoriteFood == "Sushi") {
    console.log("We're going out for Japanese food to night!");
} else if (favoriteFood == "Pasta") {
    console.log("How about we eat some Italian food tonight?");
} else if (favoriteFood == "Tacos") {
    console.log("Time for some Mexican food!");
} else if (favoriteFood == "Samosa") {
    console.log("Let's eat Indian food tonight!");
} else {
    console.log("I don't know what that favorite_food is!");
}
```

```text
I don't know what that favorite_food is!
```


### `Comparison Operators`

Here are the comparison operators that you can use in conditional expressions to generate a `boolean` value:


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

```javascript
var age = 15;
var heightInFeet = 4.6;

if (age >= 13 && heightInFeet > 5) {
    console.log("You may ride the roller coaster.");
} else {
    console.log("You may NOT ride the roller coaster.");
}
```

Example Output:

```text
You may NOT ride the roller coaster.
```

You can string as many logical operators together as you want to build more complex conditional statements:

```javascript
var isHungry = false;
var isThirsty = true;

var foodAmount = 10;
var drinkAmount = 0;

if (isHungry and foodAmount > 0 or isThirsty and drinkAmount > 0) {
    enterKitchen();
} else {
    playVideoGames();
}
```


### `Logical Operators`

Logical operators allow you to combine multiple conditional expressions in a single conditional statement:

|Operator    | Description                                         |
|------------|-----------------------------------------------------|
| `&&` (and) | `true` when both conditional expressions are `true` |
| `||` (or)  | `true` when either conditional expression is `true` |
| `!`  (not) | Reverses the value of a conditional expression      |

#### Using the `&&` operator

The `&&` (and) operator evaluates to `true` when both conditional expressions are `true`:

```javascript
var age = 15;
var heightInFeet = 5.2;

if (age >= 13 && heightInFeet > 5) {
    console.log("You may ride the roller coaster.");
} else {
    console.log("You may NOT ride the roller coaster.");
}
```

Example Output:

```text
You may ride the roller coaster.
```

#### Using the `||` operator

The `||` (or) operator evaluates to `true` when either conditional expression is `true`:

```javascript
var isHungry = true;
var isThirsty = false;

if (isHungry || isThirsty) {
    console.log("You should go to the kitchen.");
} else {
    console.log("Do whatever, you're good!");
}
```

Example Output:

```text
You should go to the kitchen.
```

#### Using the `!` operator

The `!` (not) operator reverses a conditional expression:

```javascript
var isTired = true;

if (!isTired) {
    console.log("Let's go outside and play.");
} else {
    console.log("Let's take a nap.");
}
```

Example Output:

```text
Let's take a nap.
```

### Nested Conditional Statements

Conditional statements can be nested inside other conditional statements. Use indentation to make the nesting obvious at a glance:

```javascript
var role = "admin";

if (role == "admin" || role == "developer") {
    console.log("You can see the secret stuff in this app.");
    if (role == "admin") {
        console.log("You can also see the SUPER secret stuff in this app.");
    }
}
```

Example Output:

```text
You can see the secret stuff in this app.
You can also see the SUPER secret stuff in this app.
```


### Further reading

- [MDN - JavaScript Building Blocks: Conditionals](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)
- [Eloquent JavaScript - Conditional Execution](https://eloquentjavascript.net/02_program_structure.html#h_wpz5oi2dy7)
- [The Modern JavaScript Tutorial - Conditional Branching](https://javascript.info/ifelse)


<hr>







## Data Types

Every value has a data type in JavaScript. The data type determines what kinds of operations you can perform on the value.


### `boolean`

The `boolean` data type represents a `true` or a `false` value:

```javascript
var isHungry = true;
var isThirsty = false;
```

#### Generating `boolean` values in a conditional statement

You normally won't use a `boolean` directly, but instead will generate a `boolean` in a conditional statement:

```javascript
var age = 19;

// This generates `true`
if (age >= 18) {
    console.log("You are an adult!");
}

// This generates `false`
if (age < 18) {
    console.log("You are a child.");
}
```

#### Truthy and falsy values

Booleans are not the only values that can be True/False. Every value in JavaScript is either *truthy* or *falsy*, which means they can be used in conditional statements without a boolean comparison operation. Empty strings and the number 0 are *falsy*, and all other strings and numbers are *truthy*.

Here's an example of a *falsy* value:

```javascript
var username = "";

if (username) {
    console.log(`Hello, ${username}!`);
} else {
    console.log("The username is blank");
}
```

Example Output:

```text
The username is blank
```

Here's an example of a *truthy* value:

```javascript
var numBananas = 2;

if (numBananas) {
    console.log("We have bananas!");
} else {
    console.log("We have no bananas!");
}
```

Example Output:

```text
We have bananas!
```



### `number`

The `number` data type represents any number:

```javascript
var totalCost = 29.99;
var numBananas = 2;
```

#### Converting `str` to `int`

You can use the `parseInt()` function to convert a `string` to an integer `number`:

```javascript
var age = parseInt("13");
```

This is often combined with the `prompt()` function when you prompt the user for a numeric data type:

```javascript
var age = parseInt(prompt("How old are you? "));
```

### `string`

The `string` data type represents a text value:

```javascript
var name = "Daniel";
```

#### String concatenation

If you need to combine a variable and a `string`, you can use the `+` operator. This technique is called __string concatenation__:

```javascript
var name = "Daniel";
var greeting = "Hello, " + name;

console.log(greeting);  // Hello, Daniel
```

#### String interpolation

Another way to combine a variable and a `string` is using `template-literal` strings. This technique is called __string interpolation__, and it is the preferred way to combine variables and `strings`. Note that the string must be surrounded by backtick quotes, which are usually near the 1 key on your keyboard:

```javascript
var name = "Daniel";
var age = 35;

console.log(`I'm ${name} and I'm ${age} years old.`);
```

Example Output:

```text
I'm Daniel and I'm 35 years old.
```

#### Multiline strings

Template literal strings allow you to write large blocks of text in a single `console.log()` statement:

```javascript
var menu = `
    Welcome to Dan's Taco Stand!

    Tacos       $2
    Burritos    $5
    Nachos      $3

    Place your order by clicking *Order Now*
`

console.log(menu);
```

Example Output:

```text

    Welcome to Dan's Taco Stand!

    Tacos       $2
    Burritos    $5
    Nachos      $3

    Place your order by clicking *Order Now*
```

#### Getting the number of characters in a `str`

You can use the `string.length` property to get the number of characters in a `string`:

```javascript
var name = "Daniel";

name.length  // 6
```

#### Checking if a `string` ends with a set of characters

The `string.endsWith()` method lets you check if a `string` ends with a given pattern:

```javascript
var emailAddresses = ["djs@cwhq.com", "alecg@auburn.edu", "samh@bridges.com"];

for (var emailAddress of emailAddresses) {
    if (emailAddress.endsWith(".edu")) {
        console.log(`${emailAddress} is a school address`);
    } else if (emailAddress.endsWith("cwhq.com")) {
        console.log(`${emailAddress} is a CWHQ employee address`);
    } else {
        console.log(`I don't know what ${emailAddress} is for`);
    }
}
```

Example Output:

```text
djs@cwhq.com is a CWHQ employee address
alecg@auburn.edu is a school address
I don't know what sam@bridges.com is for
```

#### Sanitizing user input

User's do strange things, but using `string.toLowerCase()` and `string.trim()` can help your program to validate `string` data types.

`string.toLowerCase()` makes a `string` lowercase:

```javascript
// Imagine a user entered "Pizza" with an uppercase P
var favoriteFood = "Pizza";

if (favoriteFood.toLowerCase() == "pizza") {
    console.log("That's my favorite food!");
}
```

Example Output:

```text
That's my favorite food!
```

`string.trim()` removes leading or trailing whitespace from a `string`:

```javascript
// Imagine a user entered " pizza" with a leading space character
var favoriteFood = " pizza";

if (favoriteFood.trim() == "pizza") {
    console.log("That's my favorite food!");
}
```

Example Output:

```text
That's my favorite food!
```

You can chain these methods together to sanitize a `string` completely:

```javascript
// What a mess! Extra spaces before/after and odd capitalization
var favoriteFood = " PIzZa  ";

if (favoriteFood.trim().toLowerCase() == "pizza") {
    console.log("That's my favorite food!");
}

```

Example Output:

```text
That's my favorite food!
```


### Further reading

- [MDN - JavaScript Data Types and Data Structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [The Modern JavaScript Tutorial - Data Types](https://javascript.info/data-types)
- [Eloquent JavaScript - Values, Types, and Operators](https://eloquentjavascript.net/01_values.html)
- [MDN - Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
- [MDN - Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
- [MDN - JavaScript Reference: Template Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
- [MDN - JavaScript Reference: String.prototype.trim()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Trim)
- [MDN - JavaScript Reference: String.prototype.toLowerCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)

<hr>









## Data Structures

Data structures allow you to efficiently store and access groups of items. Think of them like different storage containers you may use around the house.


### `array`

The `array` data structure is used to store data in ordered *slots*. It is known as *mutable sequence type*, which means it can be modified after creation.

Usually, the items in a `array` are homogeneous, which means they represent a group of similar items of the same data type:

```javascript
var names = ["alecg", "danielj", "dimas"];
var menuPrices = [4.50, 5.75, 3.00];
var ids = [184, 294, 832, 98, 4];
```

You can write an `array` on multiple lines if you want. The trailing comma is recommended but not required:

```javascript
var foods = [
    "tacos", 
    "pizza", 
    "nachos",
    "ice cream",
    "asparagus",
];
```

#### Accessing items in an `array`

You can access individual items in an `array` using the `[]` characters and the index number of the item. The index numbers start at 0:

```javascript
var names = ["alecg", "danielj", "dimas"];

console.log(names[0]);  // alecg
console.log(names[1]);  // danielj
console.log(names[2]);  // dimas
```



#### Adding an item to an `array`

To add an item to an `array` after it has been created, you can use the `array.push()` method. The `array.push()` method adds the item to the end of the `array`:

```javascript
var names = ["alecg", "danielj", "dimas"];

names.push("samh");

console.log(names);  // ['alecg', 'danielj', 'dimas', 'samh'];
```



#### Updating an item in an `array`

To update an `array` item, replace the value at the index:

```javascript
var names = ["alecg", "danielj", "dimas"];

names[1] = "django";

console.log(names);  // ['alecg', 'django', 'dimas']
```


#### Removing an item from an `array`

To remove an item from an `array`, you can use the `array.splice()` method. You tell `array.splice` the index number to start removing items from and the number of items to remove:

```javascript
array.splice(indexToRemove, numItemsToRemove);
```

Here's an example that removes the first item from an `array`:

```javascript
var names = ["alecg", "danielj", "dimas"];

names.splice(0, 1);

console.log(names)  // ['danielj', 'dimas']
```

If you want to remove an item from the end of an `array`, use the `array.pop()` method:

```javascript
var names = ["alecg", "danielj", "dimas"];;

names.pop();

console.log(names)  // ['alecg', 'danielj'];
```

#### Looping through an `array`

To loop through the items in an `array`, use a [`for...of`](#for...of) loop. Note the convention of using the plural `names` for the `array` and the singular `name` for the loop-iteration variable:

```javascript
var names = ["alecg", "danielj", "dimas"];

console.log("This documentation is brought to you by:");
for (var name of names) {
    console.log(name);
}
```

Example Output:

```text
This documentation is brought to you by:
alecg
danielj
dimas
```

You can also loop through an array using a traditional [`for`](#for) loop if you need to use the index number of each item for something:

```javascript
var names = ["alecg", "danielj", "dimas"];

console.log("This documentation is brought to you by:");
for (var i = 0; i < names.length; i++) {
    console.log(names[i]);
}
```

Example Output:

```text
This documentation is brought to you by:
alecg
danielj
dimas
```


#### Getting the number of items in an `array`

To get the number of items in an `array`, use the `array.length()` method:

```javascript
var names = ["alecg", "danielj", "dimas"];

var numNames = names.length;

console.log(numNames);  // 3
```

#### Checking if an item is contained in an `array`

To check if an item is contained in an `array`, use the `array.includes()` method:

```javascript
var names = ["alecg", "danielj", "dimas"];

console.log(names.includes("alecg"));  // True
console.log(names.includes("samh"));  // False
```



#### Further reading

- [MDN - The JavaScript Reference - Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Eloquent JavaScript - Data Structures: Objects and Arrays](https://eloquentjavascript.net/04_data.html)
- [The Modern JavaScript Tutorial - Arrays](https://javascript.info/arrays)
- [MDN - The JavaScript Reference - Array.push()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
- [MDN - The JavaScript Reference - Array.pop()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
- [MDN - The JavaScript Reference - Array.splice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
- [MDN - The JavaScript Reference - Array.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)









### `object`

The `object` data structure is used to store data in key/value pairs. 

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};
```

You can use strings for the keys as well, but we'll follow the above form in these docs:

```javascript
var staff = {
    "danielj": "Curriculum Developer",
    "alecg": "Curriculum Instructor",
    "dimas": "Designer",
};
```


#### Accessing items in an `object`

You have to know the key to access an individual item in an `object`:

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

var danielJob = staff.danielj;
console.log(`Daniel is a ${danielJob}.`);  // Daniel is a Curriculum Developer.

var alecJob = staff.alecg;
console.log(`Alec is a ${alecJob}.`);  // Alec is a Curriculum Instructor.

var dimaJob = staff.dimas.;
console.log(`Dima is a ${dimaJob}.`);  // Dima is a Designer.
```


#### Adding an item to an `object`

You can add an item to an `object` by providing the key/value pair (it's the same syntax as updating an item):


```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

staff.django = "Director Of Pug Snorts";

console.log(staff);  // {danielj: 'Curriculum Developer', alecg: 'Curriculum Instructor', dimas: 'Designer', django: 'Director Of Pug Snorts'}
```



#### Updating an item in an `object`

To update an item in an `object`, you must know the key:

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

staff.danielj = "Burrito Taste-Tester"

console.log(staff);  // {danielj: 'Burrito Taste-Tester', alecg: 'Curriculum Instructor', dimas: 'Designer'}
```



#### Removing an item from an `object`

To remove an item from an `object`, use the `delete` operator:

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
}; 

delete staff.danielj;

console.log(staff)  // {alecg: 'Curriculum Instructor', dimas: 'Designer'}
```


#### Looping through an `object`

To loop through an `object`, you use the `for...in` loop like this:

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

for (var key in staff) {
    // Note the [] used to access the value in the object
    console.log(`${key} is a ${staff[key]}.`);
}
```

Example Output:

```text
danielj is a Curriculum Developer.
alecg is a Curriculum Instructor.
dimas is a Designer.
```




#### Getting the keys from an `object`

If you need to get all of the keys from an `object`, use the `object.keys()` method. Note that the keys will be returned as an `array`:


```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

var names = staff.keys();

console.log(`Here are all the names in the staff object: ${names}`);
```

Example Output:

```text
Here are all the names in the staff object: ['danielj', 'alecg', 'dimas']
```

#### Getting the values from an `object`

If you need to get all of the values from an `object`, use the `object.values()` method. Note, the values will be returned as an `array`:


```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

var jobs = staff.values();

console.log(`Here are all the jobs in the staff object: ${jobs}`);
```

Example Output:

```text
Here are all the jobs in the staff object: ['Curriculum Developer', 'Curriculum Instructor', 'Designer']
```

#### Getting the number of items in an `object`

You can get the keys from an `object` and then use the `array.length` method to get the number of items in an `object`:

```javascript
var staff = {
    danielj: "Curriculum Developer",
    alecg: "Curriculum Instructor",
    dimas: "Designer",
};

var numberOfStaff = staff.keys().length;

console.log(`We have ${numberOfStaff} people on our staff.`);  // We have 3 people on our staff.
```




#### Further reading

- [MDN - The JavaScript Reference - Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [Eloquent JavaScript - Objects and Arrays](https://eloquentjavascript.net/04_data.html)
- [The Modern JavaScript Tutorial - Objects](https://javascript.info/object)
- [MDN - The JavaScript Reference - for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
- [MDN - The JavaScript Reference - Object.values()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)
- [MDN - The JavaScript Reference - Object.keys()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
- [MDN - The JavaScript Reference - delete operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)

<hr>












## Functions

Functions allow you to group related statements together to perform a task. They help to implement the __D.R.Y.__(Don't Repeat Yourself) principle because they reduce unnecessary repetition.


### Built-in functions

JavaScript comes with many built-in functions. We'll cover some of the most common that you'll see in CodeWizardsHQ courses below. 

##### `parseFloat()`

The `parseFloat()` function converts data to a `number` data type with a decimal point:

```javascript
var pi = parseFloat("3.14");

console.log(pi);  // 3.14
typeof pi;  // 'number

var two = parseFloat(2);

console.log(two)  // 2.0
typeof two;  // 'number'
```

##### `prompt()`

The `prompt()` function allows you to prompt a user. The user's response is returned as a `string`, which you can store in a variable:

```javascript
var name = prompt("What is your name? ");
console.log(`Nice to meet you, ${name}!`);
```

Example Output:

```text
What is your name? Daniel
Nice to meet you, Daniel!
```

##### `parseInt()`

The `parseInt()` function converts data to a `number` data type without a decimal point:

```javascript
var intPI = parseInt(3.14);

console.log(intPI);  // 3
typeof intPI;  // 'number'

var meaningOfLife = parseInt("42");

console.log(meaningOfLife);  // 42
typeof meaningOfLife;  // 'number'
```


##### `console.log()`

The `console.log()` function displays text in the developer console:

```javascript
console.log("Hello, world!");  // Hello, world!
```

###### Using special characters with `console.log()`

You can use special characters such as `\n` and `\t` to format the text a bit. The `\n` adds a newline (like hitting __enter__ on your keyboard) and the `\t` adds a tab:

```javascript
console.log("Line 1\nLine 2\nLine 3\n");
console.log("\tThis is tabbed over\n\tThis too.");
```

Example Output:

```text
Line 1
Line 2
Line 3

        This is tabbed over
        This too.
```




#### Further reading


- [MDN - Web APIs: console.log()](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)
- [MDN - The JavaScript Reference: parseInt()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
- [MDN - The JavaScript Reference: parseFloat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)
- [MDN - The JavaScript Reference: window.prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)





### User-defined functions

You define a function using the `function` keyword. Functions definitions can go anywhere in your file, but it helps to keep them all organized in a single area for readability:

```javascript
function sayHello() {
    console.log("Hello!");
}
```

#### Calling a function

Defining a function does not run the statements in the body of the function. To run a function, you *call* it like this:

```javascript
function sayHello() {
    console.log("Hello!");
}

sayHello();  // Hello!
```

#### Adding parameters to a function

When you define a function, you can add parameters that the function caller should pass in. Parameters are like variables, but the value of the variable is set by the function caller, not the function definer:

```javascript
function sayHello(name) {
    console.log(`Hello, ${name}!`);
}
```

#### Passing arguments to a function

If a function accepts parameters, you need to pass them in when you call the function. The values you pass to the function are called the *arguments* to the function:


```javascript
function sayHello(name) {
    console.log(`Hello, ${name}!`);
}

sayHello("Daniel");  // Hello, Daniel!
```

#### Returning a value from a function

You can return a value from a function by using the `return` keyword:

```javascript
function add(number1, number2) {
    var total = number1 + number2;
    return total;
}
```

#### Capturing a function's return value

If a function returns a value, you can capture it in a varible:

```javascript
function add(number1, number2) {
    var total = number1 + number2
    return total;
}

var total = add(2, 3);
console.log(total);  // 5
```

You can also use the value immediately in another function, like `console.log()`:

```javascript
function add(number1, number2) {
    var total = number1 + number2;
    return total;
}

console.log(add(2, 3))  // 5
console.log(`2 + 3 = ${add(2, 3)}`);  // 2 + 3 = 5
```


#### Indentation in functions

Indentation is not required in JavaScript, but you should do it for readability. If you have another statement inside your function that also requires indentation (like a conditional statement or loop), you should also indent the body of that statement:

```javascript
function sayHello(name) {
    console.log(`Hello, ${name}!`);
    if (name == "Daniel") {
        console.log("That's a cool name!");
    } else {
        console.log("Nice to meet you!");
    }
}


sayHello("Daniel");
sayHello("Alec");
```

Example Output:

```text
Hello, Daniel!
That's a cool name!

Hello, Alec!
Nice to meet you!
```


#### Using an early `return` statement to exit a function

A `return` statement can be used to exit a function. This is normally used when you want to verify (with a conditional statement) that some preconditions are valid before continuing to execute a function body:

```javascript
function greetCodewizard(name) {
    var staff = ["danielj", "alecg", "dimas"];
    if !staff.includes(name):
        console.log("I don't know you!");
        return;
    
    console.log(`Hello, ${name}!`);
}


greetCodewizard("danielj");  // Hello, danielj!
greeCodewizard("django");   // I don't know you!
```



#### Further reading

- [MDN - JavaScript Building Blocks: Functions](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)
- [EloquentJavaScript - Functions](https://eloquentjavascript.net/03_functions.html)
- [The Modern JavaScript Tutorial - Functions](https://javascript.info/function-basics)

<hr>