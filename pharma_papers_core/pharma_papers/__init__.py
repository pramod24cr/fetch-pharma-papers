"""Pharma Papers Core - Find research papers with authors from pharmaceutical companies."""

__version__ = "0.1.0"

from pharma_papers.api import PubMedAPI
from pharma_papers.processor import PaperProcessor
from pharma_papers.utils import export_to_csv

__all__ = ["PubMedAPI", "PaperProcessor", "export_to_csv"]