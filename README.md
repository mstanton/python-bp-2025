# Python BP 2025

A Python project using `uv` for fast and reliable dependency management.

## Prerequisites

- Python 3.8 or higher
- `uv` package installer (recommended for development)

## Installation

1. Install `uv` globally (if you haven't already):
```bash
pip install uv
```

2. Clone the repository:
```bash
git clone https://github.com/yourusername/python-bp-2025.git
cd python-bp-2025
```

3. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

4. Install the package in development mode:
```bash
uv pip install -e .
```

## Development

### Project Structure

```
python-bp-2025/
├── .venv/              # Virtual environment (gitignored)
├── src/               # Source code
│   └── python_bp_2025/
│       ├── __init__.py
│       └── hello.py
├── tests/             # Test files
│   ├── __init__.py
│   └── test_hello.py
├── .gitignore         # Git ignore rules
├── pyproject.toml     # Project metadata and build configuration
├── setup.py          # Package installation configuration
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

### Running the Project

To run the main application:
```bash
python -m python_bp_2025.hello
```

### Running Tests

To run the test suite:
```bash
python -m unittest discover tests
```

### Development Tools

This project uses:
- `uv` for fast package management
- `ruff` for linting (configured in pyproject.toml)
- `hatchling` as the build backend

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests:
   ```bash
   python -m unittest discover tests
   ```
4. Submit a pull request

## License

[meh]

## Author

[Matthew Stanton] - [mrstanton81@gmail.com]
