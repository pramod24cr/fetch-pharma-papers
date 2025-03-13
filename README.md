# Pharma Papers

A Python tool for fetching research papers from PubMed and identifying those with authors affiliated with pharmaceutical or biotech companies.

## Project Overview

This project provides a command-line tool to search PubMed for research papers, identify papers with authors from pharmaceutical or biotech companies, and export the results as a CSV file. The project is structured as two separate packages:

1. **pharma-papers-core**: A core library implementing the business logic
2. **pharma-papers-cli**: A command-line interface that uses the core library

## Features

- Search PubMed using the full query syntax
- Identify papers with authors affiliated with pharmaceutical or biotech companies
- Export results to CSV or print to console
- Command-line interface with help and debug options

## Code Organization

The project follows a modular architecture, separating the core functionality from the user interface:

```
pharma-papers/
├── pharma_papers_core/         # Core library package
│   ├── pyproject.toml          # Poetry configuration for core library
│   ├── README.md               # Documentation for core library
│   ├── pharma_papers/          # Core library source code
│   │   ├── __init__.py         # Package initialization and exports
│   │   ├── api.py              # PubMed API interaction
│   │   ├── processor.py        # Data processing logic
│   │   └── utils.py            # Utility functions
│   └── tests/                  # Tests for core library
│       ├── __init__.py
│       └── test_pharma_papers.py
│
└── pharma_papers_cli/          # CLI tool package
    ├── pyproject.toml          # Poetry configuration for CLI tool
    ├── README.md               # Documentation for CLI tool
    └── pharma_papers_cli/      # CLI tool source code
        ├── __init__.py         # Package initialization
        └── cli.py              # Command-line interface
```

### Core Components

1. **API Module (`api.py`)**: Handles interaction with the PubMed API, including searching for papers and fetching paper details.

2. **Processor Module (`processor.py`)**: Processes paper data to identify authors affiliated with pharmaceutical or biotech companies.

3. **Utils Module (`utils.py`)**: Provides utility functions for exporting data to CSV.

4. **CLI Module (`cli.py`)**: Implements the command-line interface using Typer.

## Installation

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Option 1: Install from Test PyPI

The core library is published to Test PyPI, and the CLI tool can be installed from there:

```bash
# Install the core library
pip install -i https://test.pypi.org/simple/ pharma-papers-core

# Install the CLI tool
pip install -i https://test.pypi.org/simple/ pharma-papers-cli
```

### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/pramod24cr/pharma-papers.git
cd pharma-papers

# Install the core library
cd pharma_papers_core
poetry install

# Install the CLI tool
cd ../pharma_papers_cli
poetry install
```

## Usage

After installation, you can use the command-line tool to search for papers:

```bash
# Basic usage (prints results to console)
get-papers-list "cancer AND therapy"

# Save results to a file
get-papers-list "cancer AND therapy" --file results.csv

# Enable debug mode
get-papers-list "cancer AND therapy" --debug

# Get help
get-papers-list --help
```

## Example Output

The tool generates a CSV file with the following columns:

- **PubmedID**: Unique identifier for the paper
- **Title**: Title of the paper
- **Publication Date**: Date the paper was published
- **Non-academic Author(s)**: Names of authors affiliated with non-academic institutions
- **Company Affiliation(s)**: Names of pharmaceutical/biotech companies
- **Corresponding Author Email**: Email address of the corresponding author

## Tools and Libraries Used

### Development Tools

- [Poetry](https://python-poetry.org/): Dependency management and packaging
- [Claude](https://claude.ai/): AI pair programmer (assisted with development)
- [ChatGPT](https://openai.com/chatgpt): Used for generating boilerplate code and documentation

### Core Libraries

- [Requests](https://docs.python-requests.org/): HTTP client for API calls
- [Pandas](https://pandas.pydata.org/): Data handling and CSV export
- [Typer](https://typer.tiangolo.com/): Command-line interface
- [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html): XML parsing

### Development Dependencies

- [Pytest](https://pytest.org/): Testing framework
- [Black](https://black.readthedocs.io/): Code formatter
- [Mypy](https://mypy.readthedocs.io/): Static type checker
- [isort](https://pycqa.github.io/isort/): Import sorter

## Development

### Running Tests

```bash
cd pharma_papers_core
poetry run pytest
```

### Code Formatting

```bash
poetry run black pharma_papers tests
poetry run isort pharma_papers tests
```

### Type Checking

```bash
poetry run mypy pharma_papers
```

## License

MIT