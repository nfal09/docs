# JavaScript Language

JavaScript is the language that powers the interactive web! We use JavaScript in these courses at CodeWizardsHQ:

|Elementary                        | Middle School                           |High School     |
|----------------------------------|-----------------------------------------|----------------
| Intro to Real World Programming  | Interactive Web with JavaScript         | Fundamentals of Web Development
| Capstone I Minecraft             | Capstone I Virtual Reality Game         | User Interface Development
| Fundamental Programming Concepts | User Interface Development              | APIs and Databases
| Web Development for Kids – 2     | Application Programming Interfaces      | 
|                                  | Capstone II Online Multiplayer Gaming   |

In this section of our documentation, you'll find references to most of the core JavaScript language features and built-in functions that we use in our CodeWizardsHQ courses.

You'll also find many *Further reading* sections, which pull from these excellent Python resources:

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


MIN_HEIGHT = 60  // This is measured in inches, not feet!
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
hypotenuse = ((sideA ** 2) + (sideB ** 2)) ** 0.5
```

Many programmers perfer to put `*` on each line of a multiline comment and indent a bit for clarity:

```javascript
/*
*   This calculates the hypotenuse of a right triangle when given the sides
*   of the right triangle. It's the Pythagorean Theorem. The ** is how you
*   write exponents in JavaScript, and fractional exponents are like roots,
*   so 0.5 is the square root.
*/
hypotenuse = ((sideA ** 2) + (sideB ** 2)) ** 0.5
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
isHungry = true;

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
age = 19;

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
favoriteFood = "Tacos";

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
favoriteFood = "Hot Dogs with Cream Cheese";

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
age = 15;
heightInFeet = 4.6;

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
isHungry = false;
isThirsty = true;

foodAmount = 10;
drinkAmount = 0;

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
age = 15;
heightInFeet = 5.2;

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
isHungry = true;
isThirsty = false;

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
isTired = true;

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
role = "admin";

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
isHungry = true;
isThirsty = false;
```

#### Generating `boolean` values in a conditional statement

You normally won't use a `boolean` directly, but instead will generate a `boolean` in a conditional statement:

```javascript
age = 19;

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
username = "";

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
numBananas = 2;

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
totalCost = 29.99;
numBananas = 2;
```

#### Converting `str` to `int`

You can use the `parseInt()` function to convert a `string` to an integer `number`:

```javascript
age = parseInt("13");
```

This is often combined with the `prompt()` function when you prompt the user for a numeric data type:

```javascript
age = parseInt(prompt("How old are you? "));
```

### `string`

The `string` data type represents a text value:

```javascript
name = "Daniel";
```

#### String concatenation

If you need to combine a variable and a `string`, you can use the `+` operator. This technique is called __string concatenation__:

```javascript
name = "Daniel";
greeting = "Hello, " + name;

console.log(greeting);  // Hello, Daniel
```

#### String interpolation

Another way to combine a variable and a `string` is using `template-literal` strings. This technique is called __string interpolation__, and it is the preferred way to combine variables and `strings`. Note that the string must be surrounded by backtick quotes, which are usually near the 1 key on your keyboard:

```javascript
name = "Daniel";
age = 35;

console.log(`I'm ${name} and I'm ${age} years old.`);
```

Example Output:

```text
I'm Daniel and I'm 35 years old.
```

#### Multiline strings

Template literal strings allow you to write large blocks of text in a single `console.log()` statement:

```javascript
menu = `
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
name = "Daniel";

name.length  // 6
```

#### Checking if a `string` ends with a set of characters

The `string.endsWith()` method lets you check if a `string` ends with a given pattern:

```javascript
emailAddresses = ["djs@cwhq.com", "alecg@auburn.edu", "samh@bridges.com"];

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
favoriteFood = "Pizza";

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
favoriteFood = " pizza";

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
favoriteFood = " PIzZa  ";

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