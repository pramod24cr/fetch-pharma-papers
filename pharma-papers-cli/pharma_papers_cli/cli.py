"""Command-line interface for pharma-papers."""

import logging
import sys
from typing import Optional

import typer
from pharma_papers_core.pharma_papers.api import PubMedAPI
from pharma_papers_core.pharma_papers.processor import PaperProcessor
from pharma_papers_core.pharma_papers.utils import export_to_csv

app = typer.Typer(help="Fetch research papers with authors from pharmaceutical companies")


@app.command()
def main(
        query: str = typer.Argument(..., help="PubMed query string"),
        debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output"),
        file: Optional[str] = typer.Option(None, "--file", "-f", help="Output file path for CSV results"),
) -> None:
    """Fetch research papers with authors from pharmaceutical companies."""
    # Set up logging
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(f"Debug mode enabled")
        logging.debug(f"Query: {query}")
        logging.debug(f"Output file: {file or 'stdout'}")

    try:
        # Initialize API client
        api_client = PubMedAPI(debug=debug)

        # Search for papers
        paper_ids = api_client.search_papers(query)

        if not paper_ids:
            print("No papers found matching the query.")
            sys.exit(0)

        # Fetch paper details
        papers = api_client.fetch_paper_details(paper_ids)

        # Process papers to filter for pharma/biotech authors
        processor = PaperProcessor(debug=debug)
        filtered_papers = processor.filter_pharma_papers(papers)

        if not filtered_papers:
            print("No papers found with pharmaceutical/biotech company authors.")
            sys.exit(0)

        # Export results
        result = export_to_csv(filtered_papers, file, debug)

        if file:
            print(f"Results saved to {file}")
        else:
            # Print to stdout
            print(result)

    except Exception as e:
        if debug:
            logging.exception("An error occurred:")
        else:
            print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    app()