# TODOs

## Browser APIs and jQuery

### Browser Dev Tools

-   Something about how to use the `Elements` tab to adjust HTML and styling

### jQuery's `val()` function

-   Can be in the same spot as the `attr()` stuff

<hr>

## HTML

### Images (in progress)

-   `<img>`

### Video (in progress)

-   `<video>`

### Line Breaks (in progress)

-   `<br>`
-   `<hr>`

### Tables (in progress)

-    `<table>`


### Directory Navigation

-   Show how to add different resources using `<img>` and `<video>` that live in different places in a project, such as:
    -   Project root
    -   Nested folder
    -   Parent folder



<hr>

## CSS

### What is CSS for?

-   Styling webpages
    -   Not limited to colors/sizes, but can also use it for layout

### CSS Comments

[Comments](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#comments)

### Ways To Include CSS In HTML

[Applying CSS to HTML](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#applying_css_to_html)

-   In the `<head>`
    -   As an external stylesheet with the `<link>` tag
        -   Talk about the path to the file and show examples
    -   Using the `<style>` tag
        -   When is this useful? When a page has unique content
        -   When is this not useful? When pages need to share styles
-   Inline styles
    -   Should avoid this

### CSS Rule Basics

[CSS Syntax](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS#css_syntax)

[Properties and Values](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#properties_and_values)

[Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#selectors)

[Shorthands](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#shorthands)

-   Selectors
-   Body
    -   Declarations
        -   Property/Value pairs
        -   Shorthand properties
            -   `animation`
            -   `padding`
            -   `background`
-   A note about memorization: don't, as you can look everything up.

### Specificity and the Cascade

[Specificity](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured#specificity)

[Cascade and Inheritance](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

-   Show examples of how classes can override element styles
-   Show how if you give the same style to an element later in the doc, it overrides the earlier one
-   Show how inheritance works
    -   Give example of setting font color on parent element that affects children

### Selectors

[Styling HTML elements](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started#styling_html_elements)

[Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

-   Element
-   Class
-   ID
-   Element+class (`span.my-class`)
-   Targeting multiple selectors (`p, li {}`)
-   Combinators
    -   Descendent combinator (`p em`)
    -   Adjacent sibling combinator (`h1 + p`)
    -   Child combinator (`div > p`)

### Changing Elements Based On State

[Styling things based on state](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started#styling_things_based_on_state)

-   `:link`
-   `:hover`
-   `:visited`

### Responsive Design

[Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)

[The building blocks of responsive design](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Responsive/responsive_design_building_blocks)

### The `Box` Model

[The Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model)

-   Two main categories: `block` and `inline`
-   Discuss how `width`, `height`, `padding`, `border`, and `margin` affect a box
    -   Can show shorthand/longhand versions of `margin`, `border`, and `padding`

[Inline Block](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#using_display_inline-block)

### Values and Units

[Values and units](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units)

-   Really only need to discuss `px` and maybe `%` for lengths.
-   Could also show how to use seconds (for animations)
-   Should also show that you can use raw numbers for some things (like `opacity`)
-   Can show some of the different ways to calculate color
-   The different `position` keywords (`top`, `bottom`, `left`, `right`)

### Backgrounds

[Background and Border](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Backgrounds_and_borders)

-   Show how to add backgrounds using `background-color` and `background: url()`.
    -   Can show named colors and `rgba()`
    -   How to contain images with `background-size`
    -   Controlling repeat with `background-repeat`
    -   Rounding corners with `border-radius`

### Overflow

[Overflowing Content](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Overflowing_content)

-   You'll have to deal with it when you constrain a box's width/height.




<hr>

## Jinja Templating

### Looping

### Conditionals

### Macros

### Assignments

-   This is the `set` keyword stuff

### Statements/Expressions/Comments

-   Difference between each beesting version

### Variables

### Filters

-   Just list a few of the common ones we use

### Template Inheritance
