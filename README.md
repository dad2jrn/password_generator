[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![image](https://img.shields.io/pypi/pyversions/pipenv.svg)](https://python.org/pypi/pipenv)


# Secure Password Generator
Just a simple app that will generate a strong password for the user based on a desired length.  This will call a free RESTful API to get a random dictionary based word with the desired length specified by the user.

The original unmodified word is provided to the user in order to prpvide for a better user experieince.

The word is then modified to be alphanumeric as well as ensuring it has at least two (2) special characters and two (2) numbers.

### TODO:
- add uppercase to the password generated.

## Prerequisites
Python 3.7 or higher

## Install
To install make sure you have PIPENV installed and then run the following commands in the terminal:

```bash
> pipenv install
```

This will install all the required modules.  Then run the following command to setup the virtual environment:

```bash
> pipenv shell
```

## Usage
To run this, run the following command in the terminal:

```bash
> python main.py
```

## Contributing to this project
See [Contributing](/CONTRIBUTING.md)
