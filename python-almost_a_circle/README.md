# Python - Almost a Circle

This project is a comprehensive review of Object-Oriented Programming (OOP) concepts in Python, JSON serialization/deserialization, unit testing using `unittest`, and file I/O operations (JSON & CSV).

## Project Structure

```
python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
└── README.md
```

## Classes

| Class | Description | Inherits From |
|-------|-------------|---------------|
| `Base` | Manages `id` attribute, JSON/CSV serialization and deserialization | - |
| `Rectangle` | Manages width, height, x, y attributes with validation and display methods | `Base` |
| `Square` | Manages size, x, y attributes (special Rectangle where width == height) | `Rectangle` |

## Unit Testing

To run all unit tests:

```bash
python3 -m unittest discover tests
```

To run pycodestyle:

```bash
pycodestyle models/*.py tests/test_models/*.py
```

## Author
Kingsley Kipkoech
