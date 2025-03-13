"""Module for processing PubMed paper data."""

import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class PaperProcessor:
    """Class for processing PubMed paper data."""

    # Keywords that indicate academic affiliation
    ACADEMIC_KEYWORDS = {
        "university",
        "college",
        "institute",
        "school",
        "academia",
        "faculty",
        "department",
        "laboratory",
        "univ.",
        "inst.",
        "lab",
        "hospital",
        "medical center",
        "clinic",
        "foundation",
        "center for",
    }

    # Keywords that might indicate pharmaceutical/biotech companies
    PHARMA_BIOTECH_KEYWORDS = {
        "pharma",
        "biotech",
        "therapeutics",
        "biosciences",
        "inc",
        "corp",
        "llc",
        "ltd",
        "limited",
        "gmbh",
        "co.",
        "company",
        "laboratories",
        "research and development",
        "r&d",
        "biopharma",
        "life sciences",
    }

    def __init__(self, debug: bool = False) -> None:
        """Initialize the paper processor.

        Args:
            debug: Whether to enable debug logging
        """
        self.debug = debug
        if debug:
            logging.basicConfig(level=logging.DEBUG)

    def filter_pharma_papers(
        self, papers: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Filter papers to include only those with pharma/biotech affiliations.

        Args:
            papers: List of paper details from PubMed

        Returns:
            Filtered list of papers with pharma/biotech authors
        """
        filtered_papers = []

        for paper in papers:
            pharma_authors = []
            company_affiliations = set()
            corresponding_email = None

            if "authors" not in paper:
                continue

            for author in paper.get("authors", []):
                affiliations = author.get("affiliations", [])

                # Skip authors without affiliations
                if not affiliations:
                    continue

                # Check each affiliation for this author
                is_pharma_author = False
                author_companies = set()

                for affiliation in affiliations:
                    affiliation_lower = affiliation.lower()

                    # Check if this is a non-academic affiliation
                    is_academic = any(
                        keyword in affiliation_lower
                        for keyword in self.ACADEMIC_KEYWORDS
                    )
                    is_pharma = any(
                        keyword in affiliation_lower
                        for keyword in self.PHARMA_BIOTECH_KEYWORDS
                    )

                    if is_pharma and not is_academic:
                        is_pharma_author = True

                        # Extract company name (this is a simplified approach)
                        company = self._extract_company_name(affiliation)
                        if company:
                            author_companies.add(company)
                            company_affiliations.add(company)

                if is_pharma_author:
                    # Format author name
                    author_name = f"{author.get('fore_name', '')} {author.get('last_name', '')}".strip()
                    pharma_authors.append(author_name)

                    # Check for corresponding author email
                    if "email" in author and not corresponding_email:
                        corresponding_email = author["email"]

            # Only include papers with at least one pharma/biotech author
            if pharma_authors:
                filtered_paper = {
                    "pmid": paper.get("pmid", ""),
                    "title": paper.get("title", ""),
                    "publication_date": paper.get("publication_date", ""),
                    "non_academic_authors": "; ".join(pharma_authors),
                    "company_affiliations": "; ".join(company_affiliations),
                    "corresponding_author_email": corresponding_email or "",
                }
                filtered_papers.append(filtered_paper)

        if self.debug:
            logger.debug(
                f"Filtered to {len(filtered_papers)} papers with pharma/biotech authors"
            )

        return filtered_papers

    def _extract_company_name(self, affiliation: str) -> str:
        """Extract company name from affiliation string.

        Args:
            affiliation: Affiliation string

        Returns:
            Extracted company name or empty string
        """
        # This is a simplified approach - a more robust solution would use NLP or regex patterns
        # Try to extract company name based on common patterns
        affiliation = affiliation.strip()

        # Look for company indicators
        company_indicators = ["Inc.", "Corp.", "LLC", "Ltd.", "GmbH", "Co."]
        for indicator in company_indicators:
            if indicator in affiliation:
                # Try to extract the company name (this is simplified)
                parts = affiliation.split(indicator)
                if parts and parts[0]:
                    # Take words before the indicator as the company name
                    name_parts = parts[0].strip().split()
                    # Take up to 4 words before the indicator as company name
                    company_name = " ".join(name_parts[-4:]) + " " + indicator
                    return company_name.strip()

        # If no clear indicator, return the first part of the affiliation (simplified)
        parts = affiliation.split(",")
        if parts:
            return parts[0].strip()

        return ""
