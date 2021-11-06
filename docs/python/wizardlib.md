# Wizardlib

Here, you'll find the documentation for CodeWizardHQ's <em>Wizardlib</em> Python library. We use this library in the following courses:

|Elementary              | Middle School
|------------------------|--------------
|Python Game Development |Introduction to Programming with Python

<hr>





### add_audio()

```python
add_audio(filename)
```

Adds an audio file.

Parameters:

- **filename** (*str*): The filename.

Returns:

- The audio element.

<hr>

Example usage:

```python
audio_element = add_audio("never-gonna-give-you-up.mp3")
```

<hr>





### add_background()

```python
add_background(filename)
```

Adds a background image.

Parameters:

- **filename** (*str*): The filename.

<hr>

Example usage:

```python
add_background("flying-cats.png")
```

Example output:


<figure markdown>
![add_background() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/flying-cats.jpg?raw=true){ width="300" }
<figcaption></figcaption>
</figure>


<hr>





### add_background_audio()

```python
add_background_audio(filename)
```

Adds background audio which plays when you click the "Start" button.

Parameters:

- **filename** (*str*): The filename.

<hr>

Example usage:

```python
add_background_audio("never-gonna-give-you-up.mp3")
```

<hr>




### add_button()

```python
add_image(text)
```

Adds a button.

Parameters:

- **text** (*str*): The text on the button.

Returns:

- The button element.

<hr>

Example usage:

```python
button = add_button("Click Me")
```

Example output:

<figure markdown>
![add_button() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/button.png?raw=true){ width="200" }
<figcaption></figcaption>
</figure>

<hr>






### add_image()

```python
add_image(filename, size=None)
```

Adds an image to the page.

Parameters:

- **filename** (*str*): The filename.
- **size** (*int*): The size, in pixels (optional).

Returns:

- The image element.

<hr>

Example usage:

```python
taco_image = add_image("taco.png")
```

Example output:

<figure markdown>
![add_image() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/taco.jpg?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>




### add_text()

```python
add_text(text, size=18)
```

Adds text to the page.

Parameters:

- **text** (*str*): The text to add to the page.
- **size** (*int*): The size, in pixels (optional).

Returns:

- The text element.

<hr>

Example usage:

```python
wizardlib_text = add_text("Wizardlib is cool!")
```

Example output:

<figure markdown>
![add_text() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/add-text-example.png?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>





### add_text_input()

```python
add_text_input(placeholder)
```

Adds a text input to the page.

Parameters:

- **placeholder** (*str*): The text to display in the input box.

Returns:

- The text input element.

<hr>

Example usage:

```python
text_input = add_text_input("Enter your password:")
```

Example output:

<figure markdown>
![add_text_input() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/add-text-input-example.png?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>




### animate_down()

```python
def animate_down(element, distance, time=8, loop=False)
```

Animates the element down by the given distance. Can optionally change the amount of time the animation takes and whether the element animates down and up repeatedly.

Parameters:

- **element** (*element*): An element to animate.
- **distance** (*int*): The distance the element should travel (in pixels).
- **time** (*int*): The amount of time the animations should take (optional).
- **loop** (*bool*): Whether to repeatedly animate down and up.

<hr>

Example usage:

```python
taco_image = add_image("taco.jpg")
animate_down(taco_image, 100)
```

Example output:

<figure markdown>
![animate_down() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/animate-down.gif?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>




### animate_left()

```python
def animate_left(element, distance, time=8, loop=False)
```

Animates the element left by the given distance. Can optionally change the amount of time the animation takes and whether the element animates left and right repeatedly.

Parameters:

- **element** (*element*): An element to animate.
- **distance** (*int*): The distance the element should travel (in pixels).
- **time** (*int*): The amount of time the animations should take (optional).
- **loop** (*bool*): Whether to repeatedly animate left and right.

<hr>

Example usage:

```python
taco_image = add_image("taco.jpg")
animate_left(taco_image, 100)
```

Example output:

<figure markdown>
![animate_left() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/animate-left.gif?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>




### animate_right()

```python
def animate_right(element, distance, time=8, loop=False)
```

Animates the element right by the given distance. Can optionally change the amount of time the animation takes and whether the element animates right and left repeatedly.

Parameters:

- **element** (*element*): An element to animate.
- **distance** (*int*): The distance the element should travel (in pixels).
- **time** (*int*): The amount of time the animations should take (optional).
- **loop** (*bool*): Whether to repeatedly animate right and left.

<hr>

Example usage:

```python
taco_image = add_image("taco.jpg")
animate_right(taco_image, 100)
```

Example output:

<figure markdown>
![animate_right() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/animate-right.gif?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>



### animate_up()

```python
def animate_up(element, distance, time=8, loop=False)
```

Animates the element up by the given distance. Can optionally change the amount of time the animation takes and whether the element animates up and down repeatedly.

Parameters:

- **element** (*element*): An element to animate.
- **distance** (*int*): The distance the element should travel (in pixels).
- **time** (*int*): The amount of time the animations should take (optional).
- **loop** (*bool*): Whether to repeatedly animate up and down.

<hr>

Example usage:

```python
taco_image = add_image("taco.jpg")
animate_up(taco_image, 100)
```

Example output:

<figure markdown>
![animate_up() example](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/animate-up.gif?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>

