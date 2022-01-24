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

You have access to the DOM on the page and can edit it from the *Console* tab, just like if you were in a JavaScript program:

<figure markdown>
![edit DOM example](https://github.com/codewizardshq/docs/blob/main/docs/assets/browser-apis-and-jquery/hot-dogs.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>