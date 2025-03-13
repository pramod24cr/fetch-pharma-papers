"""Module for interacting with the PubMed API."""

import logging
from typing import Any, Dict, List, Optional
from urllib.parse import quote

import requests

logger = logging.getLogger(__name__)


class PubMedAPI:
    """Class for interacting with the PubMed API."""

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    def __init__(self, debug: bool = False) -> None:
        """Initialize the PubMed API client.

        Args:
            debug: Whether to enable debug logging
        """
        self.debug = debug
        if debug:
            logging.basicConfig(level=logging.DEBUG)

    def search_papers(self, query: str, max_results: int = 100) -> List[str]:
        """Search for papers matching the query.

        Args:
            query: The search query in PubMed syntax
            max_results: Maximum number of results to return

        Returns:
            List of PubMed IDs
        """
        url = f"{self.BASE_URL}/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json",
        }

        if self.debug:
            logger.debug(f"Searching PubMed with query: {query}")

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        if self.debug:
            logger.debug(
                f"Found {len(data.get('esearchresult', {}).get('idlist', []))} results"
            )

        return data.get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, pmid_list: List[str]) -> List[Dict[str, Any]]:
        """Fetch detailed information for a list of PubMed IDs.

        Args:
            pmid_list: List of PubMed IDs

        Returns:
            List of paper details
        """
        if not pmid_list:
            return []

        url = f"{self.BASE_URL}/efetch.fcgi"
        params = {"db": "pubmed", "id": ",".join(pmid_list), "retmode": "xml"}

        if self.debug:
            logger.debug(f"Fetching details for {len(pmid_list)} papers")

        response = requests.get(url, params=params)
        response.raise_for_status()

        xml_data = response.text

        # Parse XML data
        papers = self._parse_pubmed_xml(xml_data)

        return papers

    def _parse_pubmed_xml(self, xml_data: str) -> List[Dict[str, Any]]:
        """Parse PubMed XML data to extract paper details.

        Args:
            xml_data: XML data from PubMed API

        Returns:
            List of parsed paper details
        """

        import xml.etree.ElementTree as ET

        papers = []
        root = ET.fromstring(xml_data)

        # Find all PubmedArticle elements
        for article in root.findall(".//PubmedArticle"):
            paper = {}

            # Extract PubMed ID
            pmid_elem = article.find(".//PMID")
            if pmid_elem is not None and pmid_elem.text:
                paper["pmid"] = pmid_elem.text

            # Extract title
            title_elem = article.find(".//ArticleTitle")
            if title_elem is not None and title_elem.text:
                paper["title"] = title_elem.text

            # Extract publication date
            pub_date = article.find(".//PubDate")
            if pub_date is not None:
                year = pub_date.find("Year")
                month = pub_date.find("Month")
                day = pub_date.find("Day")

                date_parts = []
                if year is not None and year.text:
                    date_parts.append(year.text)
                if month is not None and month.text:
                    date_parts.append(month.text)
                if day is not None and day.text:
                    date_parts.append(day.text)

                if date_parts:
                    paper["publication_date"] = "-".join(date_parts)

            # Extract authors and affiliations
            authors = []
            author_list = article.find(".//AuthorList")

            if author_list is not None:
                for author_elem in author_list.findall(".//Author"):
                    author = {}

                    # Get author name
                    last_name = author_elem.find("LastName")
                    fore_name = author_elem.find("ForeName")

                    if last_name is not None and last_name.text:
                        author["last_name"] = last_name.text
                    if fore_name is not None and fore_name.text:
                        author["fore_name"] = fore_name.text

                    # Get author affiliations
                    affiliations = []
                    for affiliation in author_elem.findall(".//Affiliation"):
                        if affiliation.text:
                            affiliations.append(affiliation.text)

                    author["affiliations"] = affiliations

                    # Check for corresponding author email
                    email = None
                    for aff in affiliations:
                        if "@" in aff:
                            # Extract email with simple regex-like approach
                            start_idx = aff.find("@")
                            # Look backward for the start of the email
                            email_start = start_idx
                            while email_start > 0 and aff[email_start - 1] not in [
                                " ",
                                ",",
                                ";",
                                "(",
                                ")",
                            ]:
                                email_start -= 1

                            # Look forward for the end of the email
                            email_end = start_idx
                            while email_end < len(aff) - 1 and aff[
                                email_end + 1
                            ] not in [" ", ",", ";", "(", ")"]:
                                email_end += 1

                            email = aff[email_start : email_end + 1]
                            break

                    if email:
                        author["email"] = email

                    authors.append(author)

            paper["authors"] = authors
            papers.append(paper)

        if self.debug:
            logger.debug(f"Parsed {len(papers)} papers from XML")

        return papers
