"""Tests for the pharma-papers package."""

import pytest

from pharma_papers.processor import PaperProcessor


def test_filter_pharma_papers():
    """Test filtering of papers with pharma/biotech authors."""
    # Sample test data
    test_papers = [
        {
            "pmid": "12345678",
            "title": "Test Paper",
            "publication_date": "2023-01-01",
            "authors": [
                {
                    "fore_name": "John",
                    "last_name": "Doe",
                    "affiliations": ["Pharma Inc., New York, USA"],
                },
                {
                    "fore_name": "Jane",
                    "last_name": "Smith",
                    "affiliations": ["University of Science, Boston, USA"],
                    "email": "jane@university.edu",
                },
            ],
        },
        {
            "pmid": "87654321",
            "title": "Academic Paper",
            "publication_date": "2023-02-01",
            "authors": [
                {
                    "fore_name": "Alice",
                    "last_name": "Johnson",
                    "affiliations": ["University of Research, London, UK"],
                }
            ],
        },
    ]

    processor = PaperProcessor()
    filtered = processor.filter_pharma_papers(test_papers)

    # Should only include the first paper with pharma author
    assert len(filtered) == 1
    assert filtered[0]["pmid"] == "12345678"
    assert "John Doe" in filtered[0]["non_academic_authors"]
    assert "Pharma Inc" in filtered[0]["company_affiliations"]


def test_extract_company_name():
    """Test company name extraction from affiliation strings."""
    processor = PaperProcessor()

    # Test various company formats
    assert "Pharma Inc." in processor._extract_company_name(
        "Pharma Inc., New York, USA"
    )
    assert "BioTech Corp." in processor._extract_company_name(
        "BioTech Corp., San Francisco, CA"
    )
    assert "Molecular Systems" in processor._extract_company_name(
        "Molecular Systems Ltd., London, UK"
    )
