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
![Flying Cats](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/flying-cats.jpg?raw=true){ width="300" }
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
![Button](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/button.jpg?raw=true){ width="200" }
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
![Taco](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/taco.jpg?raw=true){ width="300" }
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
![Wizardlib Text](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/add-text-example.jpg?raw=true){ width="300" }
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
![Wizardlib Text](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/add-text-input-example.jpg?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>
