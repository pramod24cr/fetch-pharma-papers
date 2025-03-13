# Pharma Papers CLI

A command-line interface for fetching research papers from PubMed and identifying those with authors affiliated with pharmaceutical or biotech companies.

## Features

- Search PubMed using the full query syntax
- Identify papers with authors affiliated with pharmaceutical or biotech companies
- Export results to CSV or print to console
- User-friendly command-line interface with help and debug options

## Installation

### Prerequisites

- Python 3.9 or higher

### From Source

```bash
git clone https://github.com/yourusername/pharma-papers.git
cd pharma-papers/pharma_papers_cli
poetry install
```

## Usage

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

### Command Options

```
Arguments:
  QUERY  PubMed query string  [required]

Options:
  -d, --debug                 Enable debug output
  -f, --file TEXT             Output file path for CSV results
  --help                      Show this message and exit
```

### Query Syntax

This tool supports PubMed's full query syntax. Here are some examples:

- Simple keyword search: `cancer`
- Phrase search: `"breast cancer"`
- Boolean operators: `cancer AND therapy NOT surgery`
- Field-specific search: `Smith[Author] AND 2023[PDAT]`
- Complex queries: `(cancer OR tumor) AND (drug OR therapy) AND 2020:2023[PDAT]`

## Examples

### Example 1: Basic Search

```bash
get-papers-list "covid-19 AND vaccine"
```

### Example 2: Save Results to File

```bash
get-papers-list "breast cancer AND immunotherapy" --file breast_cancer_research.csv
```

### Example 3: Debug Mode

```bash
get-papers-list "alzheimer's disease AND treatment" --debug
```

## How It Works

The CLI tool uses the `pharma-papers-core` library to:

1. Search for papers on PubMed using the provided query
2. Fetch detailed information for each paper
3. Identify papers with at least one author affiliated with a pharmaceutical or biotech company
4. Export the results in CSV format

## Dependencies

- [pharma-papers-core](https://test.pypi.org/project/pharma-papers-core/): Core functionality
- [Typer](https://typer.tiangolo.com/): Command-line interface

## License

MIT