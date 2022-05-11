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
