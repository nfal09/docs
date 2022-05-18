# CSS Language

CSS (Cascading Stylesheets) is used to define the style of a webpage. Think of it like the choice of paint, wood, window curtains, etc. when building a house. When you visit a website, the CSS is what the gives the webpage its fancy design!

We use CSS in the following courses at CWHQ:

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

In this section of our documentation, you'll find references to most of the core CSS language features that we use in our CodeWizardsHQ courses.

You'll also find many _Further reading_ sections, which pull from these excellent CSS resources:

-   [MDN CSS Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)
-   [web.dev Learn CSS](https://web.dev/learn/css/)

<hr>

## Including CSS In HTML Documents

In order for CSS style rules to apply to an HTML document, you must include them in the document in some way.

### Including CSS In The `<head>`

Generally, CSS is added in the `<head>` of an HTML document. You can link an external CSS file using a `<link>` tag, or you can write CSS directly in an HTML document using the `<style>` tag. Both methods are shown below.

```css
/* style.css */
h1 {
    color: red;
}
```

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Including CSS in HTML Documents</title>
        <!-- This is an external stylesheet -->
        <link rel="stylesheet" href="style.css" />
        <style>
            p {
                color: blue;
            }
        </style>
    </head>

    <body>
        <h1>This is red because of the CSS in style.css</h1>
        <p>This is blue because of the CSS in the style tag</p>
    </body>
</html>
```

<figure markdown>
![Including CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/including-css-in-html.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### Inline CSS

You can also write CSS style rules directly in an HTML tag using the `style` attribute, but this is generally discouraged.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Including CSS in HTML Documents</title>
    </head>

    <body>
        <h1 style="color: red;">
            This is red because of the CSS in this element's style attribute
        </h1>
    </body>
</html>
```

<figure markdown>
![Including inline CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/including-inline-css-in-html.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Comments

In CSS you can create comments between `/* */` blocks. They can be single line or multiline.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>CSS Comments</title>
        <style>
            /* This is a single line comment */

            /*
            This 
            spans 
            multiple lines
            */
        </style>
    </head>

    <body></body>
</html>
```

## CSS Rule Basics

CSS works by selecting one or more HTML elements and then applying styles to those HTML elements. The way to select elements can be as simple as writing the HTML tag name, targeting tags with a common class or id, or even targeting tags based on some state such as being hovered over.

The basic syntax is:

```css
selector {
    property: value;
    otherproperty: otherValue;
    anotherproperty: value1 value2 value3;
}
```

Notice that property/value pairs can be one-to-one or one-to-many.

Here's an example of targeting a few elements and applying styles to them:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>CSS Rule Basics</title>
        <style>
            #page-title {
                color: green;
                text-shadow: 20px 15px 4px black;
            }

            p {
                color: blue;
                text-decoration: underline;
                border: 10px solid red;
                padding: 24px;
                font-size: 42px;
            }
        </style>
    </head>

    <body>
        <h1 id="page-title">This text is green and has a text shadow added.</h1>
        <p>
            Each paragraph tag has the same styles because we targeted the "p"
            selector.
        </p>
        <p>See what I mean?</p>
    </body>
</html>
```

<figure markdown>
![Including inline CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/css-rule-basics.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Specificity And The Cascade

When applying styles to HTML elements there are two principles, specificity and the cascade, that can influence which styles are applied to a given element.

### Specificity

Specificity is calculated by _how_ you selected an element or group of HTML elements.

For example, the element with the id `danger` below has red text, even though there's a style rule selecting all `<p>` elements and turning them blue:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Specificity and the Cascade</title>
        <style>
            p {
                color: blue;
                font-size: 32px;
            }

            #danger {
                color: red;
            }
        </style>
    </head>

    <body>
        <p>This is blue.</p>
        <p id="danger">This is red!</p>
        <p>This is also blue.</p>
        <p>But, we're all the same size.</p>
    </body>
</html>
```

<figure markdown>
![Including inline CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/specificity.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

### The Cascade

The cascade applies to _where_ in the CSS styles a style rule lies. If you are targeting a selector in two places, the one furthest down the page wins for any style rules that are conflicting.

Note how there are no blue `<p>` tags in the example below because the second CSS rule overwrites the `color` property of the first:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Specificity and the Cascade</title>
        <style>
            p {
                color: blue;
                font-size: 32px;
            }

            p {
                color: red;
            }
        </style>
    </head>

    <body>
        <p>This is red, the blue color was overwritten!</p>
        <p>This is also red!</p>
        <p>But, we're all the same size.</p>
    </body>
</html>
```

<figure markdown>
![Including inline CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/cascade.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Inheritance

Some CSS properties are passed on to children of HTML elements. For example, the `color` property will be passed to child elements. You can still override styles that are inherited by using a more specific selector for a child element.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>inheritance</title>
        <style>
            div {
                color: blue;
                font-size: 32px;
            }

            .warning {
                color: red;
            }
        </style>
    </head>

    <body>
        <div>
            <p>This is blue because of inheritance!</p>
            <p class="warning">This is red because of specificity.</p>
        </div>
    </body>
</html>
```

<figure markdown>
![Including inline CSS in HTML](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/inheritance.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Selectors 

CSS Selectors allow you to access HTML elements to style. Below are some of the common CSS selectors you may use. 

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Selectors</title>
        <style>
             /* Element Selector*/
            div {
                border: 3px groove black;
            }
            /* Class Selector */
            .object {
                border-width: 10px;
                border-color: blueviolet;
            }
            /* ID Selector  */
            #heading {
                color: red;
            }
            /* Element+class */
            div.container{
                box-shadow: 10px 10px 10px black;
            }
            /* Attribute Selector */
            input[type="text"] {
                border: none;
                border-bottom: 2px solid black;
            }

            /* Targeting Multiple Selectors */
            em, span {
                color: rgb(252, 106, 206);
            }

            /* Combinators */

            /* Descendent Combinator */
            p em:hover {
                font-size: 30px;
            }
            /* Adjacent Sibling Combinator */
            li + li  {
                color: rgb(4, 255, 0);
            }

            /* Child Combinator */
            .combinator > p {
                color: red;
            }

        </style>
    </head>

    <body>
        <div class="container">

            <div class="object">
                <h1 id="heading">Hello!</h1>
                <p>Some text <em>goes here</em></p>
                <span>Hello</span>
            </div>

            <div class="list">
                <ol>
                    <li>One</li>
                    <li>Two </li>
                    <li>Three</li>
                </ol>
                <input type="text" placeholder="Name">
                <input type="submit" value="Enter">
            </div>

            <div class="combinator">
                <h2>Heading 2 </h2>
                <p>Some text <em>here</em> yay!</p>
            </div>  
        </div>
    </body>
</html>
```
<figure markdown>
![Selectors example](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/Selectors.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Styling Elements Based on State

CSS allows you to change the styling of an element depending on its `state`. When an element is hovered over or visited, you can modify its styling. 

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Styling based on state</title>
        <style>
            a:link {
                color: red;
            }
            a:hover{
                color: green;
                font-size: 65px;
            }
            a:visited{
                color: teal;
             }
        </style>
    </head>

    <body>
        <div class="container">
            <a href="page2.html"> Link </a>  
        </div>

    </body>
</html>
```

<figure markdown>
![changeState example](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/changestate.png?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>

## Responsive Design

You can use Media Queries to define styling based on the device type, such as device width. You may use the `@media` rule to make your websites responsive by creating conditions based on device breakpoints. The condition is created using the properties `min-width` and `max-width.`

     !!! note 

        Browsers by default zoom out the page to fit on the screen you open. For media queries to work, we don't want this zooming out. To disable this zooming out we need to use `<meta>` tag.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Responsive Design</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            #insect{
                height: 100%;
                background-size: contain;
                background-repeat: no-repeat;
                background-position: bottom;
                width:100px;
                margin: auto;
                margin-top:-100px;
                background-image: url('larve.png');
                transition: 1s all ease;
            }

            @media (min-width: 400px) and (max-width: 768px){
                #insect{
                    width:150px;
                    background-image: url('caterpillar.png');
                }
            }

            @media (min-width: 768px) and (max-width: 1100px){
                #insect{
                    width:170px;
                    background-image: url('butterfly1.png');
                }
            }

            @media (min-width: 1100px){
                #insect{
                    width: 250px;
                    background-image: url('butterfly2.png');
                }
            }
        </style>
    </head>

    <body>
        <div id="insect"></div>

    </body>
</html>
```

<figure markdown>
![responsive example](https://github.com/codewizardshq/docs/blob/main/docs/assets/css/responsive.gif?raw=true){ width="100%" }
<figcaption></figcaption>
</figure>