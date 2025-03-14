# Pharma Papers Core

A Python library for fetching research papers from PubMed and identifying those with authors affiliated with pharmaceutical or biotech companies.

## Features

- Search PubMed using the full query syntax
- Identify papers with authors affiliated with pharmaceutical or biotech companies
- Export results to CSV or return as a string
- Comprehensive API for integration in other projects

## Installation

### From Test PyPI

```bash
pip install -i https://test.pypi.org/simple/ pharma-papers-core
```

### From Source

```bash
git clone https://github.com/pramod24cr/pharma-papers.git
cd pharma-papers/pharma_papers_core
poetry install
```

## Usage

### Basic Usage

```python
from pharma_papers.api import PubMedAPI
from pharma_papers.processor import PaperProcessor
from pharma_papers.utils import export_to_csv

# Initialize API client
api_client = PubMedAPI(debug=True)

# Search for papers
paper_ids = api_client.search_papers("cancer AND therapy")

# Fetch paper details
papers = api_client.fetch_paper_details(paper_ids)

# Process papers to filter for pharma/biotech authors
processor = PaperProcessor()
filtered_papers = processor.filter_pharma_papers(papers)

# Export results to CSV
export_to_csv(filtered_papers, "results.csv")
```

### API Reference

#### PubMedAPI

```python
class PubMedAPI:
    """Class for interacting with the PubMed API."""
    
    def __init__(self, debug: bool = False) -> None:
        """Initialize the PubMed API client."""
    
    def search_papers(self, query: str, max_results: int = 100) -> List[str]:
        """Search for papers matching the query."""
    
    def fetch_paper_details(self, pmid_list: List[str]) -> List[Dict[str, Any]]:
        """Fetch detailed information for a list of PubMed IDs."""
```

#### PaperProcessor

```python
class PaperProcessor:
    """Class for processing PubMed paper data."""
    
    def __init__(self, debug: bool = False) -> None:
        """Initialize the paper processor."""
    
    def filter_pharma_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter papers to include only those with pharma/biotech affiliations."""
```

#### Utility Functions

```python
def export_to_csv(data: List[Dict[str, Any]], 
                  filename: Optional[str] = None, 
                  debug: bool = False) -> Optional[str]:
    """Export data to CSV file or return as string."""
```

## Code Organization

The module is structured as follows:

- `pharma_papers/`: Main package directory
  - `__init__.py`: Package initialization and exports
  - `api.py`: PubMed API interaction
  - `processor.py`: Data processing logic
  - `utils.py`: Utility functions

## Development

### Running Tests

```bash
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

## Dependencies

- [Requests](https://docs.python-requests.org/): HTTP client for API calls
- [Pandas](https://pandas.pydata.org/): Data handling and CSV export

## License

MIT