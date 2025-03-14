# Project Report: PubMed Pharma Papers Tool

## Executive Summary

This report documents the approach, methodology, and results of developing a Python tool that fetches research papers from PubMed and identifies those with authors affiliated with pharmaceutical or biotech companies. The project has been implemented as two separate packages: a core library and a command-line interface (CLI), following modern Python development practices.

## Project Requirements

The assignment required the development of a tool that:
1. Fetches papers from PubMed using its API
2. Identifies papers with at least one author affiliated with a pharmaceutical or biotech company
3. Exports the results as a CSV file with specific columns
4. Provides a user-friendly command-line interface
5. Optionally separates the code into a module and CLI tool (bonus requirement)

## Approach and Architecture

### Modular Design

The project was structured with a clear separation of concerns:

- **Core Library (`pharma-papers-core`)**: Contains all business logic:
  - API interaction with PubMed
  - Paper processing and pharmaceutical company identification
  - Utility functions for exporting data

- **CLI Tool (`pharma-papers-cli`)**: Provides a user interface:
  - Command-line argument parsing
  - User feedback and error handling
  - Orchestration of core library components

This modular approach offers several advantages:
- Enhanced maintainability
- Improved testability
- Potential for reuse in other applications
- Clear separation of business logic from user interface

### Technical Choices

1. **Programming Language**: Python 3.9+ was chosen for its rich ecosystem of libraries, readability, and widespread use in scientific and data processing applications.

2. **Dependency Management**: Poetry was used for dependency management and packaging, providing a modern and user-friendly approach to managing project dependencies.

3. **API Client**: The Requests library was selected for HTTP interactions with the PubMed API due to its simplicity and widespread adoption.

4. **Data Processing**: Pandas was used for data manipulation and CSV export, offering powerful tools for working with structured data.

5. **CLI Framework**: Typer was chosen for building the command-line interface, providing a clean and intuitive way to define commands and arguments.

6. **XML Parsing**: ElementTree was used for parsing XML responses from PubMed, as it's included in the standard library and sufficient for the task.

7. **Type Checking**: The project uses Python's type hints throughout to enhance code readability and catch potential type-related errors.

## Implementation Details

### Core Components

1. **PubMedAPI Class**: Handles interaction with the PubMed API through the eUtils endpoints:
   - `search_papers()`: Searches for papers matching a query
   - `fetch_paper_details()`: Retrieves detailed information for papers
   - `_parse_pubmed_xml()`: Parses XML responses to extract relevant information

2. **PaperProcessor Class**: Processes paper data to identify pharmaceutical company affiliations:
   - `filter_pharma_papers()`: Filters papers based on author affiliations
   - `_extract_company_name()`: Attempts to extract company names from affiliation strings

3. **Utility Functions**:
   - `export_to_csv()`: Formats data and exports it to CSV

### CLI Implementation

The CLI tool provides a user-friendly interface with the following features:
- Query argument for specifying the search query
- Debug flag for enabling verbose output
- File option for specifying an output file
- Help documentation for usage instructions

### Author Affiliation Identification

A key challenge was identifying pharmaceutical/biotech company affiliations. The solution uses a combination of:

1. Keyword lists to distinguish academic from non-academic affiliations
2. Heuristics to identify company names within affiliation strings
3. Pattern matching to extract corresponding author emails

### Error Handling

The implementation includes robust error handling for various scenarios:
- API request failures
- Invalid query syntax
- XML parsing errors
- Missing data in responses

## Results and Evaluation

### Functionality

The implemented solution successfully meets all the requirements:
- It searches PubMed using the provided query
- It identifies papers with authors from pharmaceutical or biotech companies
- It exports the results to a CSV file with the required columns
- It provides a user-friendly command-line interface
- It separates the code into a module and CLI tool (bonus requirement)

### Code Quality

The codebase adheres to high standards of quality:
- Comprehensive type annotations throughout
- Clear documentation including docstrings and comments
- Logical organization of code into modules and classes
- Consistent naming conventions and code style
- Efficient API usage, minimizing unnecessary requests

### Performance

The tool performs efficiently for typical use cases:
- Processes search results in batches to handle large result sets
- Uses efficient data structures for filtering and processing
- Minimizes memory usage by processing data incrementally

### Testing

A comprehensive test suite was developed to ensure the correctness of the implementation:
- Unit tests for core components
- Mock tests for API interactions
- Integration tests for the entire workflow

All tests pass, demonstrating the reliability of the implementation.

## Challenges and Solutions

### Challenge 1: Identifying Non-Academic Affiliations

Distinguishing between academic and pharmaceutical/biotech affiliations proved challenging due to the variety of formats and naming conventions.

**Solution**: A combination of keyword matching, pattern recognition, and heuristics was used to identify company affiliations with reasonable accuracy.

### Challenge 2: XML Parsing Complexity

The XML responses from PubMed contain complex nested structures that require careful parsing.

**Solution**: A dedicated XML parsing function was implemented to extract relevant information in a structured manner.

### Challenge 3: Handling Missing Data

Author affiliations and emails are not always present or structured consistently in PubMed data.

**Solution**: The implementation includes robust handling of missing or incomplete data, ensuring that the tool works with real-world PubMed responses.

## Future Improvements

Several enhancements could be made to improve the tool:

1. **Improved Company Identification**: Implementing more sophisticated natural language processing techniques could enhance the accuracy of company identification.

2. **Caching**: Adding a caching layer could improve performance for repeated queries.

3. **Parallel Processing**: Implementing parallel API requests could speed up the retrieval of large result sets.

4. **User Interface Enhancements**: A web-based interface would make the tool accessible to a wider audience.

5. **Additional Filtering Options**: Allowing users to filter by publication date, journal, or other criteria would enhance the tool's utility.

## Conclusion

The implemented solution successfully meets all the requirements of the assignment, providing a robust and user-friendly tool for identifying research papers with pharmaceutical company authors. The modular architecture ensures maintainability and extensibility, while the comprehensive testing ensures reliability.

The completion of the bonus requirement—separating the code into a module and CLI tool—demonstrates a commitment to best practices in software development and provides additional flexibility for users.

This project showcases the ability to design and implement a complex, real-world application that integrates with external APIs, processes data efficiently, and provides a user-friendly interface.
