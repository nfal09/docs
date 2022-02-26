# Browser APIs and jQuery

JavaScript is the language that powers the interactive web! We use JavaScript as the primary language in these courses at CodeWizardsHQ:

|Elementary                            | Middle School          |High School     |
|--------------------------------------|------------------------|----------------
| Interactive Websites with JavaScript | Interactive JavaScript | Fundamentals of Web Development
| Capstone 3                           | Web Interfaces         | User Interface Development
|                                      | Capstone 2             | Capstone 1
|                                      | Mastering APIs          | APIs and Databases
|                                      | Capstone 3             | Capstone 2
|                                      |                        | DevOps and Software Engineering
|                                      |                        | Capstone 3

In this section of our documentation, you'll find references on how to use the built-in browser APIs and the `jQuery` library to manipulate webpages.

You'll also find many *Further reading* sections, which pull from these excellent JavaScript resources:

- [MDN JavaScript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [The Modern JavaScript Tutorial](https://javascript.info/)
- [Eloquent JavaScript](https://eloquentjavascript.net/)
- [Learn jQuery](https://learn.jquery.com/)
- [jQuery API](https://api.jquery.com/)

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

*my-awesome-script.js*

```javascript
console.log("Hello, world!");
```

*index.html*

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

The `jQuery` library is not part of the core Browser APIs and must be loaded in the `<head>` of your HTML document. You can find the most recent version of the `jQuery` library on their [website](https://code.jquery.com/). Generally, you want the *minified* version of the library, as that has all the core functionality in a smaller payload (which improves browser load times).

```html
<!DOCTYPE html>
<html>

<head>
    <title>Adding jQuery to a webpage</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
</head>

<body>
    <h1>This is HTML</h1>
</body>

</html>
```









## Using The Browser's Dev Tools

When working with JavaScript, the developer tools (dev tools for short) are your best friend! You should spend some time reading the documentation for the dev tools in your browser of choice. We'll use Chrome in these examples, and they have excellent documentation [here](https://developer.chrome.com/docs/devtools/).


### The JavaScript console

Once you've opened the dev tools in your browser of choice (look up how to do it for your browser) you'll have access to a *Console* tab. You can write JavaScript code here to test things out:

<figure markdown>
![console example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/console.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Modifying the DOM from the console

You have access to the DOM on the page and can edit it from the *Console* tab, just like if you were in a JavaScript program:

<figure markdown>
![edit DOM example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/hot-dogs.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>


#### Debugging errors from the console

If something is not working as you expect, you should open the *Console* tab in the dev tools and see if there are any errors. This can save you hours of debugging time if you learn to do it well!

Often, you'll be given a link that opens the offending file and points at the exact line that caused the issue, as in this example:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Daniel's Homepage</title>
</head>

<body>

    <h1>Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler</h1>

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

You have access to any global variables and functions in the *Console* tab and can mess around with them to see if they are doing what you expect:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Daniel's Homepage</title>
</head>

<body>

    <h1>Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler</h1>

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
    <h1 id="page-title">Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler</h1>

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


#### Getting elements with `jQuery`

The `jQuery` library allows you to select elements with the `$()` function. You can add any valid CSS selector as the argument.

Here, we use the `id` attribute to select a single element:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Daniel's Homepage</title>
    <!-- Must include the jQuery library in the <head> -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
</head>

<body>

    <!-- This is the element we'll grab from our JavaScript program -->
    <h1 id="page-title">Daniel Schroeder - Code Wizard and Semi-Professional Pug Wrestler</h1>

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
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
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


### Styling DOM Nodes 

### Events

### Timers 
Javascript has two `time intervals` methods that allow us to execute code at a given time. 


The `setTimeout` function will execute a given function after waiting a certain amount of time. 

```html
<head>
    <title>Cat TakeOver!</title>
    <link href="style.css" rel="stylesheet" >
</head>

<body>
    <h1>Wait for it......</h1>
    <img id="cat" src="funny-cat.jpg">
</body>

  
  <script>
    
    function addCat() {
       var catImage = document.getElementById('cat');
       catImage.style.opacity = 1;
      
    }
     //setTimeout will call the function after 10000 ms or 10 seconds
    setTimeout(addCat, 10000)
    
    
  </script>
</html>
```

<figure markdown>
![setTimeout example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/catgif.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

The `setInterval` function will execute a given function repeatedly with a set time . 


```html
<!DOCTYPE html>
<html>
  <head>
    <title>Cat TakeOver!</title>
    <link
      href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined"
      rel="stylesheet"
    />
    <link href="style.css" rel="stylesheet" />
  </head>

  <body>
    <h1>Wait for it......</h1>
    <div>
      <img id="cat" src="funny cat.jpg" />
      <div id="t">
        <span id="cl" class="material-icons-outlined"> favorite </span>

        <p id="likes">0</p>
      </div>
    </div>
  </body>

  <script>
    var likes = 0;

    function catLikes() {
      likes++;
      document.getElementById("likes").innerHTML = likes;
    }
    //setInterval will call the function every 1000 ms or 1 second
    setInterval(catLikes, 5000);
  </script>
</html>
```

<figure markdown>
![setInterval example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/setInterval.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>
