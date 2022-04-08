# HTML Language

HTML (HyperText Markup Language) is used to define the structure of a webpage. Think of it like the frame of a house. When you visit a website, an HTML page is what the browser parses to display all of the content on the page!

We use HTML in the following courses at CWHQ:

| Elementary                           | Middle School              | High School                      |
| ------------------------------------ | -------------------------- | -------------------------------- |
| Fundamental Programming Concepts     | Webpages with HTML & CSS   | Fundamentals of Web Development  |
| Web Development For Kids - 1         | Capstone 1                 | User Interface Development       |
| Web Development For Kids - 2         | User Interface Development | Capstone 1                       |
| Creating Websites with HTML/CSS      | Responsive Web Development | APIs and Databases               |
| Responsive Websites with HTML/CSS    | Interactive JavaScript     | Professional Web App Development |
| Interactive Websites with JavaScript | Web Interfaces             | Modern CSS Frameworks            |
| Capstone 3                           | Capstone 2                 | Capstone 2                       |
|                                      | Mastering APIs             | Mastering MVC Framework          |
|                                      | Capstone 3                 | Object Relational Mapping        |
|                                      |                            | DevOps and Software Engineering  |
|                                      |                            | Capstone 3                       |

In this section of our documentation, you'll find references to most of the core HTML language features that we use in our CodeWizardsHQ courses.

You'll also find many _Further reading_ sections, which pull from this excellent HTML resource:

-   [MDN HTML Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)

<hr>

## Basic HTML Structure

HTML documents have a standard basic form which looks like this:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>[INSERT TILE HERE]</title>
    </head>

    <body>
        <!-- INSERT HTML CONTENT TAGS HERE -->
    </body>
</html>
```

#### The `DOCTYPE` tag

The `DOCTYPE` is the first tag in an HTML document, and it's required to ensure the browser parses an HTML document correctly. If you leave it out, strange things can happen depending on the user's browser settings:

```html
<!DOCTYPE html>
```

#### The `<html>` tag

The `<html>` tag is used to hold the contents of an HTML document, which will consist of a `<head>` and a `<body>`. The HTML document ends at the `</html>` tag.

```html
<!DOCTYPE html>

<html>
    <!-- Everything in here is part of the HTML document -->
</html>
```

#### The `<head>` tag

The `<head>` tag is used to hold information about the HTML document that shouldn't appear on the page (like the title, character encoding, etc.) and is also used to pull in external resources (like CSS or JavaScript).

```html
<!DOCTYPE html>

<html>
    <head>
        <!-- This is for information about the document or linking external resources -->
    </head>
</html>
```

#### The `<title>` tag

The `<title>` tag appears in the browser tab and should be included in all HTML documents.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>This appears in the browser tab</title>
    </head>
</html>
```

<figure markdown>
![Browser Tab Example](https://github.com/codewizardshq/docs/blob/main/docs/assets/html/browser-tab.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### The `<body>` tag

The `<body>` tag holds all of the HTML content that will appear on the page. This is the content you want the user to see.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>This appears in the browser tab</title>
    </head>

    <body>
        <h1>This appears on the page</h1>
        <p>So does this</p>
    </body>
</html>
```

<figure markdown>
![HTML On Page](https://github.com/codewizardshq/docs/blob/main/docs/assets/html/html-on-page.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Common Additions To The Basic HTML Structure

If you explore HTML documents on your favorite websites, you'll see that there are many variations on the basic HTML structure shown above. We'll discuss a few common additional tags that you'll see at CWHQ in this section, such as the `<style>`, `<link>`, `<script>`, and `<meta>` tags.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Common Additions To The Basic HTML Structure</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="style.css" />
        <script src="game-logic.js"></script>
        <style>
            h1 {
                color: red;
            }
        </style>
    </head>

    <body>
        <h1>This appears on the page, and is red!</h1>
        <p>
            This appears on the page and is black (the default color for text)
        </p>

        <script>
            var paragraphElement = document.createElement("p");
            paragraphElement.textContent = "I can build HTML from JavaScript!";

            document.body.append(paragraphElement);
        </script>
    </body>
</html>
```

<figure markdown>
![Common Additions To Basic HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/html/common-additions.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### The `<meta>` tag

The `<meta>` tag can be used to add different information about the document, such as the author, character encoding, whether it should be responsive to different screen sizes, etc. In the example below, we tell the browser that it should be responsive to different screen sizes using the `<meta>` tag:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Common Additions To The Basic HTML Structure</title>
        <!-- Please take into consideration the device I'm being viewed on 
        for sizing things! -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </head>

    <body></body>
</html>
```

#### The `<link>` tag

The `<link>` tag is commonly used to include an external CSS stylesheet, either from your own filesystem or externally from somewhere like Google Fonts. In the example below, we include a stylesheet from our filesystem called `style.css`:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Common Additions To The Basic HTML Structure</title>
        <!-- Include all the CSS style rules from `style.css` in this 
        HTML document -->
        <link rel="stylesheet" href="style.css" />
    </head>

    <body></body>
</html>
```

#### The `<script>` tag

You can include a `<script>` tag in the `<head>` or at the end of the `<body>` in an HTML document. If you use the `src` attribute, the `<script>` tag pulls JavaScript data from an external file. If you don't use the `src` attribute, you write the JavaScript directly in the HTML document.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Common Additions To The Basic HTML Structure</title>
        <!-- Please add the JavaScript code from `game-logic.js` into
        this file -->
        <script src="game-logic.js"></script>
    </head>

    <body>
        <!-- Add all HTML content here -->

        <script>
            // This JavaScript logic can be written directly in the HTML file
            var paragraphElement = document.createElement("p");
            paragraphElement.textContent = "I can build HTML from JavaScript!";

            document.body.append(paragraphElement);
        </script>
    </body>
</html>
```

#### The `<style>` tag

The `<style>` tag can be used to add CSS directly in an HTML document instead of pulling it from an external file.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Common Additions To The Basic HTML Structure</title>
        <!-- Please add these CSS styles to anything in the `<body>` that
        I target with a CSS selector -->
        <style>
            h1 {
                color: red;
            }
        </style>
    </head>

    <body>
        <h1>This appears on the page, and is red!</h1>
        <p>
            This appears on the page and is black (the default color for text)
        </p>
    </body>
</html>
```

## Elements Give Text Meaning

HTML elements (or tags) that you use in the `<body>` of an HTML document should be used to give text structure and meaning. Use the right tag for the right job!

For example, the `<p>` tag is used to display generic text while the `<h1>` tag is used to display the top-level title or headline of your page. You use the `<img>` tag to display images.

#### Well-Structured HTML

If we were making a page about tacos and wanted to have a title, some text, and an image, this would be a good structure:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Tacos - Homepage</title>
    </head>

    <body>
        <h1>My Favorite Taco</h1>
        <p>
            I think that all tacos are amazing, but my favorite is probably the
            Carne Asada taco. It's filled with steak, and you can add
            onions/cilantro/lime to the top. You can optionally add guacamole as
            well, which I highly recommend!
        </p>
        <img src="taco.jpg" />
    </body>
</html>
```

<figure markdown>
![Taco Example](https://github.com/codewizardshq/docs/blob/main/docs/assets/html/taco-example.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

#### Poorly-Structured HTML

In contrast, we could make the same page like this:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Tacos - Homepage</title>
        <style>
            p {
                font-size: 42px;
            }
            h1 {
                font-size: 16px;
            }
            #taco-image {
                background-image: url(taco.jpg);
                background-size: contain;
                background-repeat: no-repeat;
                width: 500px;
                height: 500px;
                display: block;
            }
        </style>
    </head>

    <body>
        <p>My Favorite Taco</p>
        <h1>
            I think that all tacos are amazing, but my favorite is probably the
            Carne Asada taco. It's filled with steak, and you can add
            onions/cilantro/lime to the top. You can optionally add guacamole as
            well, which I highly recommend!
        </h1>
        <span id="taco-image"></span>
    </body>
</html>
```

<figure markdown>
![Taco Bad HTML Example](https://github.com/codewizardshq/docs/blob/main/docs/assets/html/taco-bad-html.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

This is not well-structured HTML because we're not using the right element for the right job anywhere! Instead, we're trying to use CSS to make the `<p>` tag big and the `<h1>` tag small, and the `<span>` is holding an image instead of an `<img>` tag. Why use all of that CSS when you could use the natural element for the job? As a rule, always structure your page with the correct tags first, and then you can add CSS to style them later.
