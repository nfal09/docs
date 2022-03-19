# Browser APIs and jQuery

JavaScript is the language that powers the interactive web! We use JavaScript as the primary language in these courses at CodeWizardsHQ:

| Elementary                           | Middle School          | High School                     |
| ------------------------------------ | ---------------------- | ------------------------------- |
| Interactive Websites with JavaScript | Interactive JavaScript | Fundamentals of Web Development |
| Capstone 3                           | Web Interfaces         | User Interface Development      |
|                                      | Capstone 2             | Capstone 1                      |
|                                      | Mastering APIs         | APIs and Databases              |
|                                      | Capstone 3             | Capstone 2                      |
|                                      |                        | DevOps and Software Engineering |
|                                      |                        | Capstone 3                      |

In this section of our documentation, you'll find references on how to use the built-in browser APIs and the `jQuery` library to manipulate webpages.

You'll also find many _Further reading_ sections, which pull from these excellent JavaScript resources:

-   [MDN JavaScript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
-   [The Modern JavaScript Tutorial](https://javascript.info/)
-   [Eloquent JavaScript](https://eloquentjavascript.net/)
-   [Learn jQuery](https://learn.jquery.com/)
-   [jQuery API](https://api.jquery.com/)

<hr>

## Adding JavaScript to Webpages

JavaScript programs at CWHQ are all run in a web browser, and they need to be included in an HTML document in order to run in the browser. There are several ways to do this, which will be outlined below.

#### Using a `<script>` tag in the `<body>`

The `<script>` tag is used to insert JavaScript programs directly into an HTML page. You should make the `<script>` tag the last tag in the `<body>` of an HTML document:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting JavaScript with a script tag in the body</title>
    </head>

    <body>
        <h1>This is HTML</h1>
        <script>
            // Everything in here is JavaScript
        </script>
    </body>
</html>
```

#### Using a `<script>` tag in the `<head>`

You can link an external JavaScript file to an HTML document using the `<script>` tag in the `<head>` of the document:

_my-awesome-script.js_

```javascript
console.log("Hello, world!");
```

_index.html_

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting JavaScript with a script tag in the head</title>
        <script src="my-awesome-script.js"></script>
    </head>

    <body>
        <h1>This is HTML</h1>
    </body>
</html>
```

## Adding jQuery to Webpages

The `jQuery` library is not part of the core Browser APIs and must be loaded in the `<head>` of your HTML document. You can find the most recent version of the `jQuery` library on their [website](https://code.jquery.com/). Generally, you want the _minified_ version of the library, as that has all the core functionality in a smaller payload (which improves browser load times).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Adding jQuery to a webpage</title>
        <script
            src="https://code.jquery.com/jquery-3.6.0.min.js"
            integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
            crossorigin="anonymous"
        ></script>
    </head>

    <body>
        <h1>This is HTML</h1>
    </body>
</html>
```

## Using The Browser's Dev Tools

When working with JavaScript, the developer tools (dev tools for short) are your best friend! You should spend some time reading the documentation for the dev tools in your browser of choice. We'll use Chrome in these examples, and they have excellent documentation [here](https://developer.chrome.com/docs/devtools/).

### The JavaScript console

Once you've opened the dev tools in your browser of choice (look up how to do it for your browser) you'll have access to a _Console_ tab. You can write JavaScript code here to test things out:

<figure markdown>
![console example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/console.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Modifying the DOM from the console

You have access to the DOM on the page and can edit it from the _Console_ tab, just like if you were in a JavaScript program:

<figure markdown>
![edit DOM example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/hot-dogs.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Debugging errors from the console

If something is not working as you expect, you should open the _Console_ tab in the dev tools and see if there are any errors. This can save you hours of debugging time if you learn to do it well!

Often, you'll be given a link that opens the offending file and points at the exact line that caused the issue, as in this example:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Daniel's Homepage</title>
    </head>

    <body>
        <h1>
            Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler
        </h1>

        <!-- HTML abbreviated since it's not important -->

        <script>
            function thisHasAnError() {
                // uh oh, this will throw an error!
                vra rightBehindThis;
            }
        </script>
    </body>
</html>
```

<figure markdown>
![console error example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/console-error.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Testing variables and functions from the console

You have access to any global variables and functions in the _Console_ tab and can mess around with them to see if they are doing what you expect:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Daniel's Homepage</title>
    </head>

    <body>
        <h1>
            Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler
        </h1>

        <!-- HTML abbreviated since it's not important -->

        <script>
            var myFavoriteFood = "Tacos";

            function sayHello(name) {
                console.log("Hello, " + name);
            }
        </script>
    </body>
</html>
```

<figure markdown>
![mess with variables/functions example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/variables-and-functions.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Selecting Elements From HTML Documents

The `document` object allows you to interact with HTML documents from a JavaScript program. The most important thing you'll use the `document` object for is querying an HTML document for an element or elements. There are several methods to do this using the native `document` object. `jQuery` also provides a way to query HTML documents, and we'll cover both methods below.

#### Getting an element by `id`

The `document.getElementById()` method allows you to select an HTML element by it's `id` attribute:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Daniel's Homepage</title>
    </head>

    <body>
        <!-- This is the element we'll grab from our JavaScript program -->
        <h1 id="page-title">
            Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler
        </h1>

        <!-- HTML abbreviated since it's not important -->

        <script>
            // Get the #page-title element and store it in a variable
            var pageTitleElement = document.getElementById("page-title");
            // Change the font color of the #page-title element
            pageTitleElement.style.color = "blue";

            // Can also do everything in one line
            document.getElementById("page-title").style.color = "blue";
        </script>
    </body>
</html>
```

<figure markdown>
![get element by id example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/get-element-by-id.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Getting an element by `class name`

The `document.getElementsByClassName()` method allows you to return the selected HTML elements by it's class attribute:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <div class="container">
            <div class="object"></div>
            <div class="object"></div>
            <div class="object"></div>
        </div>
        <script>
            // Return all elements with the class name of `object`
            var allObjects = document.getElementsByClassName("object");

            // changeBackground() will change the background color of the clicked box
            function changeBackgroundColor(event) {
                box = event.currentTarget;
                box.style.backgroundColor = "#003566";
            }
            // Here we are looping through each element and attaching an onclick event
            for (var object of allObjects) {
                object.onclick = changeBackgroundColor;
            }
        </script>
    </body>
</html>
```

<figure markdown>
![getElementsByClassName example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/className.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Getting an element by `tag name`

The `document.getElementsByTagName()` method allows you to return the selected HTML elements by it's tag name:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <div class="container">
            <div class="object"></div>
            <div class="object"></div>
            <div class="object"></div>
        </div>

        <script>
            //Return all elements with class name `object`
            var allObjects = document.getElementsByTagName("div");

            // Add border color to all div tags
            for (var object of allObjects) {
                object.style.borderColor = "#ffd60a";
            }
        </script>
    </body>
</html>
```

<figure markdown>
![getElementsByTagName example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/elementsByTagName.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### `querySelector()`

The `document.querySelector()` method allows you to return the first element with the given name:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <div class="container">
            <div class="object"></div>
            <div class="object"></div>
            <div class="object"></div>
        </div>
        <script>
            // Return first element with class name of `object`
            var firstElement = document.querySelector(".object");

            // Add color to border of first element with class `object`
            firstElement.style.borderColor = "red";
        </script>
    </body>
</html>
```

<figure markdown>
![querySelector example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/querySelector.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### `querySelectorAll()`

The `document.querySelectorAll()` method allows you to return a list of all elements with the given attribute:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <div class="container">
            <div class="object"></div>
            <div class="object"></div>
            <div class="object"></div>
        </div>
        <script>
            // Return all elements with the class name of `object`
            var allObjects = document.querySelectorAll(".object");

            // Here we are looping through each element to change the borderWidth
            for (var object of allObjects) {
                object.style.borderWidth = "20px";
            }
        </script>
    </body>
</html>
```

<figure markdown>
![querySelectorAll example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/querySelectorAll.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Getting elements with `jQuery`

The `jQuery` library allows you to select elements with the `$()` function. You can add any valid CSS selector as the argument.

Here, we use the `id` attribute to select a single element:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Daniel's Homepage</title>
        <!-- Must include the jQuery library in the <head> -->
        <script
            src="https://code.jquery.com/jquery-3.6.0.min.js"
            integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
            crossorigin="anonymous"
        ></script>
    </head>

    <body>
        <!-- This is the element we'll grab from our JavaScript program -->
        <h1 id="page-title">
            Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler
        </h1>

        <!-- HTML abbreviated since it's not important -->

        <script>
            // Get the #page-title element and store it in a variable
            var pageTitleElement = $("#page-title");
            // Change the font color of the #page-title element
            pageTitleElement.attr("style", "color: blue");

            // Can also do everything in one line
            $("#page-title").attr("style", "color: blue");
        </script>
    </body>
</html>
```

<figure markdown>
![jquery get element example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/get-element-by-id.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

You can select multiple elements as well. For example, elements that all share the same `class` can be edited together like this:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Daniel's Homepage</title>
        <!-- Must include the jQuery library in the <head> -->
        <script
            src="https://code.jquery.com/jquery-3.6.0.min.js"
            integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
            crossorigin="anonymous"
        ></script>
    </head>

    <body>
        <!-- Other HTML abbreviated since it's not important -->

        <div>
            <h2>About me</h2>
            <!-- We'll grab these elements from JavaScript -->
            <p class="likes">I like to code</p>
            <p class="likes">I like tacos</p>
            <p class="likes">I like pugs</p>
        </div>

        <script>
            // Get the .likes elements and store them in a variable
            var likesElements = $(".likes");
            // Change the font color of all the .likes elements
            likesElements.attr("style", "color: red");

            // Can also do everything in one line
            $(".likes").attr("style", "color: red");
        </script>
    </body>
</html>
```

<figure markdown>
![jquery get elements example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/get-elements-by-class-jquery.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Timers

There are two `timer` functions that allow us to execute code at a later time.

### `setTimeout()`

The `setTimeout()` function will execute a callback function after waiting for some amount time.

Function signature:

```javascript
var timeoutID = setTimeout(callbackFunction, milliseconds);
```

Parameters:

-   `callbackFunction` (`function`): The function you want to run after the given interval.
-   `milliseconds` (`number`): The amount of time before the `callbackFunction` should run.

Returns:

-   A numeric ID representing the eventual execution of the `callbackFunction`.

Example usage:

```javascript
function addCat() {
    var catImage = document.getElementById("cat");
    catImage.style.opacity = 1;
}

// Execute the `addCat()` function after 10,000 milliseconds (10 seconds).
setTimeout(addCat, 10000);
```

<figure markdown>
![setTimeout example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/catgif.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `setInterval()`

The `setInterval()` function will execute a given callback function repeatedly over a set time interval.

Function signature:

```javascript
var intervalID = setInterval(callbackFunction, milliseconds);
```

Parameters:

-   `callbackFunction` (`function`): The function to run every given `milliseconds`.
-   `milliseconds` (`number`): The amount of time between each execution of `callbackFunction`.

Returns:

-   A numeric ID representing the interval executing the `callbackFunction`.

Example Usage:

```javascript
var likes = 0;

function increaseCatLikes() {
    likes++;
    document.getElementById("likes").textContent = likes;
}

// Execute the `increaseCatLikes()` function every 5,000 milliseconds (5 seconds).
setInterval(increaseCatLikes, 5000);
```

<figure markdown>
![setInterval example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/setInterval.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `clearTimeout()`

If you need to cancel execution of a callback function setup by `setTimeout()` or `setInterval()` use `clearTimeout()`. This function will require an `intervalID` parameter for the timeout or interval you are trying to clear.

Function signature:

```javascript
clearTimeout(intervalID);
```

Parameters:

-   `intervalID` (`number`): The interval ID returned from `setTimeout()` or `setInterval()`.

Example usage:

Here's how you can cancel a function that `setTimeout()` is going to execute:

```javascript
function addCat() {
    var catImage = document.getElementById("cat");
    catImage.style.opacity = 1;
}

// Execute the `addCat()` function after 10,000 milliseconds (10 seconds).
var catTimeoutID = setTimeout(addCat, 10000);

/*
 *   This function could be run by another part of the script to cancel
 *   the execution fo the `addCat()` function. It would only work if the
 *   time interval (10 seconds) hand't already passed.
 */
function stopAddCat() {
    clearTimeout(catTimeoutID);
}
```

Here's how you can cancel a function that `setInterval()` is running:

```javascript
var likes = 0;

function increaseCatLikes() {
    likes++;
    document.getElementById("likes").textContent = likes;

    if (likes == 20) {
        alert("Interval cleared");
        // `clearInterval()` will stop executing `catLikes()` after 20 likes.
        clearInterval(catIntervalID);
    }
}

var catIntervalID = setInterval(increaseCatLikes, 5000);
```

<hr>

## jQuery Events

The following _event methods_ handle events on our webpage. They all have a similar function signature (except the `on()` method):

```javascript
$("cssSelector").methodName(callbackFunction);
```

### `change()`

The `change()` method will execute a function when the input value has changed.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function vanishInput() {
      $("form").fadeOut();
  }

  // Run the `vanishInput()` function when any `<input>` element in the `<form>` is changed.
  $("form").change(vanishInput);


</script>

</div>

</html>

```

<figure markdown>
![change method example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/change.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `click()`

The `click()` method allows you to execute a function when element is clicked.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function clickHeading() {
      $("#heading").show();
      $("form").show();
  }

  // When the button with the id of `name` is clicked, the `clickHeading()` function will run.
  $("#name").click(clickHeading);


</script>

</div>

</html>
```

<figure markdown>
![clickmethod example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/clickmethod.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `hover()`

The `hover()` method allows you to execute a function when the cursor hovers over an element.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function turnToGold() {
      var headingCSS = {
          color: "gold",
      };
      $("#heading").css(headingCss);
  }

  // When you hover over the element with the id of `#heading` call the `turnToGold()` function.
  $("#heading").hover(turnToGold);


</script>

</div>

</html>
```

<figure markdown>
![hover method example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/hover.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `mousemove()`

The `mousemove()` method allows you to execute a function when the mouse moves on top of the given element.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function changeLogo() {
      var changeLogoCSS = {
          color: "blue",
      };
      $("#wave").css(changeLogoCSS);
  }

  // When the mouse moves around the element with an id of `#wave`, run the `changeLogo()` function.
  $("#wave").mousemove(changeLogo);

</script>

</div>

</html>
```

<figure markdown>
![mousemove method example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/mousemove.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `mouseover()`

The `mouseover()` method allows you to execute a function when the mouse is over the element.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function changeLogo() {
      var changeLogoCSS = {
          fontSize: "100px",
      };
      $("#wave").animate(changeLogoCSS, "2s");
  }

  // When the mouse moves over the element with an id of `#wave`, run the `changeLogo()` function.
  $("#wave").mouseover(changeLogo);


</script>

</div>

</html>
```

<figure markdown>
![mouseover example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/mouseoverevent.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `submit()`

The `submit()` method allows you to submit form values.

```html
<!DOCTYPE html>
<html>

<head>
<title>Events!</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
<button id="name">Click</button>
<h1 id="heading">Welcome!</h1>
<span class="material-icons-outlined" id="wave">
    waving_hand
</span>
<form>
    <input type="text" placeholder="Enter Wizard Name" id="wizardName" autocomplete="off">
    <input id="sub" type="submit" value="Submit">
</form>


<script>

  function submitWizardName(event) {
      event.preventDefault();
      var wizardName = $("#wizardName").val();
      $("#heading").text(`Welcome ${wizardName}!`);
  }

  // When the `<form>` is submitted, run the the `submitWizardName()` function.
  $("form").submit(submitWizardName);


</script>

</div>

</html>
```

<figure markdown>
![submitevent example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/submitevent.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `on()`

The `on()` method allows you to run any event on an element.

Syntax:

```javascript
$("cssSelector").on("eventName", callbackFunction);
```

Example Output:

```javascript
function clickedBody() {
    alert("You clicked on the body!");
}

$("body").on("click", clickedBody);
```

<figure markdown>
![onMethod example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/onmethod.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### `off()`

To remove any events from an element use the `off()` method

```javascript
function removeEvent() {
    $("body").off("click");
    alert("Click has been deactivated!");
}

// setTimeout() will call removeEvent() after 5000 milliseconds(5 seconds)
setTimeout(removeEvent, 5000);
```

<figure markdown>
![offMethod example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/offmethod.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Getting and Setting attributes

### The `getAttribute()` function allows you to access the attribute of an element

```html
<!DOCTYPE html>
<html>

<head>
<title>Home</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>
  <div class="object" id="one"></div>
  <img class="object" id="two" src="">
  <input type="text" placeholder="Dog Name" id="three">
</div>

<script>

  var element = document.querySelector('#three');

  var elementAttribute = element.getAttribute('type');
  console.log("The input type is " + elementAttribute)

</script>
</html>
```

Example Output:

```javascript
The input type is : text
```

### The `setAttribute()` function allows you to set or update the attribute of an element

```html
<!DOCTYPE html>
<html>

<head>
<title>Home</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>

  <div class="object" id="one"></div>
  <img class="object" id="two" src="">

</div>
<script>

  var imageElement = document.getElementById('two');
  imageElement.setAttribute('src', 'dog.png');

</script>
</html>

```

Example Output:

<figure markdown>
![setAttribute example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/setAttribute.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### jQuery's `attr()` function allows you access or add the attribute to an element

```html
<!DOCTYPE html>
<html>

<head>
<title>Home</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

</head>

<body>

<div>

  <img class="object" id="one" src="">
  <img class="object" id="two" src="">

</div>
<script>

   function clickedPicture(event) {
      var clicked = event.target;

      // Here we are grabbing the id attribute of the clicked image
      var id = $(clicked).attr('id');

      if (id == 'one') {
        $('#one').attr('src', 'dog.jpg');
      } else if (id == 'two') {
        $('#two').attr('src', 'cat.jpg');
    }
  }
    $('.object').click(clickedPicture);

</script>
</html>

```

<figure markdown>
![attr example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/attr.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>
