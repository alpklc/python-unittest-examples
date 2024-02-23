### How to make python virtual environment? (Windows)
`python -m venv venv`

### How to activate python virtual environment? (Windows)
`.\venv\Scripts\activate`

### How to print python version?
`python --version`

### How to print pip version?
`pip --version`

### How to list installed modules?
`pip list`

### How to upgrade pip? (Windows)
`python.exe -m pip install --upgrade pip`

### How to install requirement python modules?
`pip install -r requirements.txt`

### How to save new modules to requirements.txt?
`pip freeze > requirements.txt`

### How to run tests in the sample package?
`python .\src\sample\tests.py`

### Source
[https://www.pythontutorial.net/python-unit-testing/](https://www.pythontutorial.net/python-unit-testing/)

### Test Commands
`python -m unittest discover -v`

`python -m unittest test_package.test_module -v `

`python -m unittest test_package.test_module.TestClass -v`

`python -m unittest test_package.test_module.TestClass.test_method -v`

### Test Coverage
`pip install coverage`

`python -m coverage run -m unittest`

`python -m coverage report`

`python -m coverage html`

