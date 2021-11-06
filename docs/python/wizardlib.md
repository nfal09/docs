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

- **filename**(*str*): The filename.

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

- **filename**(*str*): The filename.

<hr>

Example usage:

```python
add_background("flying-cats.png")
```

Example output:


<figure markdown>
![Taco Image](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/flying-cats.jpg?raw=true){ width="300" }
<figcaption></figcaption>
</figure>


<hr>

### add_image()

```python
add_image(filename, size=None)
```

Adds an image to the page.

Parameters:

- **filename**(*str*): The filename.
- **size**(*int*): The size, in pixels (optional).

Returns:

- The image element.

<hr>

Example usage:

```python
taco_image = add_image("taco.png")
```

Example output:

<figure markdown>
![Taco Image](https://github.com/codewizardshq/docs/blob/main/docs/assets/m11-wizardlib/taco.jpg?raw=true){ width="300" }
<figcaption></figcaption>
</figure>

<hr>

