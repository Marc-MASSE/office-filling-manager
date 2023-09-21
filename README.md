# Office Filling Manager

## Description
Office Filling Manager is a MVC application allows you to manage the filling of a society's offices.

Offices are of 2 types: commercial or developer. Each type contains the appropriate materials for the employees working on it.

## Installation

Install Python `3.11+`.

## Usage

```bash
python main.py  # or python3 main.py
```
The application will add employees randomly, either a commercial or a developer.
To add a new employee, press the enter key.
The application automatically stops when the society can no longer accept a new employee.

## Tests

```bash
pytest -v tests\
```

## Data

The number of offices and their composition can be found in the file :
**constants/data_for_initialisation.py**

