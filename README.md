# CodeWizardsHQ Documentation

Welcome to the CodeWizardsHQ documentation page! 

This documentation is a reference for most of the libraries and languages we use in CodeWizardsHQ courses. It is not meant to be an exhaustive reference, but rather a handy tool that covers the basics. You'll find links to further reading throughout if you want to explore a topic in more detail. 

## Usage

Visit the site [here](https://codewizardshq.github.io/docs/) to browse the documentation. 


## Running Locally

If you'd like to run this project locally (mainly for folks that want to contribute), you'll need to clone the repo onto your machine:

```bash
➜  ~ git clone git@github.com:codewizardshq/docs.git
```

This project uses Python, so locate your Python interpreter and make sure you have Python 3 installed:

```bash
➜  ~ which python
/usr/bin/python
➜  ~ python --version
Python 3.10.0
```

Then, enter the directory of the repo and create and activate a virtual environment:

```bash
➜  docs git:(main) python -m venv .venv
➜  docs git:(main) source .venv/bin/activate
(.venv) ➜  docs git:(main) 
```
Install the dependencies in the `requirements.txt` file:

```bash
(.venv) ➜  docs git:(main) python -m pip install -r requirements.txt 
```

Then, you're ready to open your project in your favorite text editor (I'm using VS Code here) and fire up the local server:

```bash
(.venv) ➜  docs git:(main) code . 
(.venv) ➜  docs git:(main) mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.34 seconds
INFO     -  [12:17:18] Serving on http://127.0.0.1:8000/
```

Navigate to the provided URL (http://127.0.0.1:8000/ in this case) in your web browser, and you can see any changes you make as soon as you save a file.


## Contributing

This documentation is open source, which means you can contribute directly if you find and issue or want to add a missing topic. The core documentation is written in [Markdown](https://www.markdownguide.org/) and you can edit the styles in the [/docs/stylesheets/extra.css](https://github.com/codewizardshq/docs/blob/main/docs/stylesheets/extra.css) file.

If you're not sure how to contribute via GitHub, there are excellent resources such as [First Contributions](https://github.com/firstcontributions/first-contributions) or [Open Source Guides - How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

If you're not comfortable with making changes yourself on GitHub, you can file an issue [here](https://github.com/codewizardshq/docs/issues) and someone will either implement your suggestions or reject them with comments.
