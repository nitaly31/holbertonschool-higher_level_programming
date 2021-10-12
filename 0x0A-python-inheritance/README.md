# Project 0x0A. Python - Inheritance 📚

### Requirements
***
#### Python Scripts
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files must be executable
* The length of your files will be tested using wc

#### Python Test Cases
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`

### 🎨 Style
***
* Code should use the PEP 8 style (version 2.7.*).

### 🎯 Tasks
***
Mandatory:
| Files | Description |
| --- | --- |
| [0-lookup.py]() | Function that returns the list of available attributes and methods of an object. |
| [1-my_list.py]() | Creation of a class that inherits a list. |
| [2-is_same_class.py]() | Function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`. |
| [3-is_kind_of_class.py]() | Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`. |
| [4-inherits_from.py]() | Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`. |
| [5-base_geometry.py]() | Empty class `BaseGeometry`. |
| [6-base_geometry.py]() | Class `BaseGeometry` with public instance method `def area(self):`. |
| [7-base_geometry.py]() | Integer validator, based on `6-base_geometry.py`. |
| [8-rectangle.py]() | Class `Rectangle` that inherits from `BaseGeometry`, based on `7-base_geometry.py`. |
| [9-rectangle.py]() | Full rectangle, based on `8-rectangle.py`. |
| [10-square.py]() | Class `Square` that inherits from `Rectangle`, the `area()` method must be implemented, based on `9-rectangle.py`. |
| [11-square.py]() |Class `Square` that inherits from `Rectangle`(`9-rectangle.py`), `str()` should return , based on `10-square.py`. |

| Folder | Description |
| --- | --- |
| [Tests]() | Folder containing the test files. |