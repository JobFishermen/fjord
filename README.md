# fjord
The backend server used by skiff and lagoon.

## Prechecks

1. Make sure you have Python 3.11 installed.
2. Make sure you have [poetry](https://python-poetry.org/) installed.

## Setup

```
poetry install
```

## Run

```
poetry run uvicorn app.main:app --reload --port 8000
```

## Packages

### App

- [fastapi](https://fastapi.tiangolo.com/)
  > FastAPI framework, high performance, easy to learn, fast to code, ready for production.
- [uvicorn](https://www.uvicorn.org/)
  > Uvicorn is an ASGI web server implementation for Python.
- [pydantic](https://docs.pydantic.dev/)
  > Data validation and settings management using Python type annotations.
- [aiohttp](https://docs.aiohttp.org/en/stable/)
  > Asynchronous HTTP Client/Server for [asyncio](https://docs.python.org/3/library/asyncio.html) and Python.
- [beanie](https://beanie-odm.dev/)
  > An asynchronous Python object-document mapper (ODM) for [MongoDB](https://www.mongodb.com/). Data models are based on [Pydantic](https://docs.pydantic.dev/).
- [motor](https://motor.readthedocs.io/en/stable/)
  > A coroutine-based API for non-blocking access to MongoDB from [asyncio](https://docs.python.org/3/library/asyncio.html).

### Dev

- [typer](https://typer.tiangolo.com/)
  > Typer, build great CLIs. Easy to code. Based on Python type hints.
- [mypy](https://mypy-lang.org/)
  > Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.
- [autopep8](https://pypi.org/project/autopep8/)
  > autopep8 automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.

### Testing

- [pytest](https://docs.pytest.org/en/7.2.x/)
  > The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- [pytest-asyncio](https://pypi.org/project/pytest-asyncio/)
  > pytest-asyncio is a pytest plugin. It facilitates testing of code that uses the asyncio library.
- [pytest-cov](https://pypi.org/project/pytest-cov/)
  > This plugin produces coverage reports. Compared to just using coverage run this plugin does some extras.
