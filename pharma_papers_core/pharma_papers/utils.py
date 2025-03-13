"""Utility functions for the pharma-papers package."""

import logging
from typing import Any, Dict, List, Optional

import pandas as pd

logger = logging.getLogger(__name__)


def export_to_csv(
    data: List[Dict[str, Any]], filename: Optional[str] = None, debug: bool = False
) -> Optional[str]:
    """Export data to CSV file or return as string.

    Args:
        data: List of dictionaries to export
        filename: Optional filename to save to
        debug: Whether to enable debug logging

    Returns:
        CSV string if filename is None, otherwise None
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.debug(f"Exporting {len(data)} records to CSV")

    if not data:
        if debug:
            logger.debug("No data to export")
        return "" if filename is None else None

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Ensure all required columns are present (with empty values if needed)
    required_columns = [
        "pmid",
        "title",
        "publication_date",
        "non_academic_authors",
        "company_affiliations",
        "corresponding_author_email",
    ]

    for col in required_columns:
        if col not in df.columns:
            df[col] = ""

    # Reorder columns according to requirements
    df = df[required_columns]

    # Rename columns for the output
    df = df.rename(
        columns={
            "pmid": "PubmedID",
            "title": "Title",
            "publication_date": "Publication Date",
            "non_academic_authors": "Non-academic Author(s)",
            "company_affiliations": "Company Affiliation(s)",
            "corresponding_author_email": "Corresponding Author Email",
        }
    )

    if filename:
        df.to_csv(filename, index=False)
        if debug:
            logger.debug(f"Data exported to {filename}")
        return None
    else:
        return df.to_csv(index=False)
