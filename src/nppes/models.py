"""Data models for NPPES provider information."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Provider:
    """Represents a healthcare provider from NPPES."""
    
    npi: str
    name: str
    specialty: Optional[str]
    taxonomy_code: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    zip_code: Optional[str]
    entity_type: str  # "Individual" or "Organization"
    raw_data: dict  # Full NPPES response

