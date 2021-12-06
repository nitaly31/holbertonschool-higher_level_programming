# Project 0x0C. Python - Almost a circle 📚

### Requirements
***
#### Python Scripts
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files must be executable
* The length of your files will be tested using wc

#### Python Unit Tests
* All your test files should be inside a folder `tests`
* You have to use the `unittest module`
* All your test files should be python files (extension: `.py`)
* Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`

### 🎨 Style
***
* Code should use the PEP 8 style (version 2.7.*).

### 🎯 Tasks
***
#### Mandatory:

Inside `models/` folder:

| Files | Description |
| --- | --- |
| [__init__.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/__init__.py) | Script that converts the directory as a package. |
| [base.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py) | Base class of geometrical instances. |
| [rectangle.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py) | Class that inherits attributes references from `Base` class. |
| [square.py](https://github.com/nitaly31/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py) | Class that inherits attributes references from `Square` class. |

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.
