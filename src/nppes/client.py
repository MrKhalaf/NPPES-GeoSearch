"""NPPES API client for searching healthcare providers."""

import httpx
from typing import List, Optional
from .models import Provider


class NPPESClient:
    """Client for interacting with the NPPES API."""
    
    BASE_URL = "https://npiregistry.cms.hhs.gov/api"
    
    def __init__(self, timeout: float = 30.0):
        """Initialize the NPPES client.
        
        Args:
            timeout: Request timeout in seconds
        """
        self.timeout = timeout
        self.client = httpx.Client(timeout=timeout)
    
    def search_providers(
        self,
        zip_code: str,
        taxonomy_code: Optional[str] = None,
        limit: int = 20,
        entity_type: Optional[str] = None
    ) -> List[Provider]:
        """Search for providers by ZIP code and optional taxonomy code.
        
        Args:
            zip_code: 5-digit ZIP code
            taxonomy_code: Optional taxonomy code to filter by
            limit: Maximum number of results per search
            entity_type: Optional entity type filter ("1" for Individual, "2" for Organization)
            
        Returns:
            List of Provider objects
        """
        params = {
            "version": "2.1",
            "postal_code": zip_code,
            "limit": limit
        }
        
        if taxonomy_code:
            # NPPES API accepts taxonomy code directly
            params["taxonomy_description"] = taxonomy_code
            # Also try searching by code if description doesn't work
            # The API may match on taxonomy code in the description field
        
        if entity_type:
            params["enumeration_type"] = entity_type
        
        try:
            response = self.client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            providers = []
            if "results" in data:
                for entry in data["results"]:
                    provider = self._normalise_entry(entry)
                    if provider:
                        providers.append(provider)
            
            return providers
        except httpx.HTTPError as e:
            raise Exception(f"Failed to search NPPES API: {e}")
    
    def _normalise_entry(self, entry: dict) -> Optional[Provider]:
        """Normalize an NPPES API response entry into a Provider object.
        
        Args:
            entry: Raw NPPES API response entry
            
        Returns:
            Provider object or None if entry is invalid
        """
        try:
            npi = entry.get("number", "")
            if not npi:
                return None
            
            # Extract basic info
            basic = entry.get("basic", {})
            entity_type_code = basic.get("enumeration_type", "")
            entity_type = "Individual" if entity_type_code == "1" else "Organization"
            
            # Extract name
            name = ""
            if entity_type == "Individual":
                first_name = basic.get("first_name", "")
                last_name = basic.get("last_name", "")
                middle_name = basic.get("middle_name", "")
                name_parts = [first_name, middle_name, last_name]
                name = " ".join([p for p in name_parts if p]).strip()
            else:
                name = basic.get("organization_name", "").strip()
            
            if not name:
                return None
            
            # Extract taxonomy and specialty
            taxonomy_code = None
            specialty = None
            taxonomies = entry.get("taxonomies", [])
            if taxonomies:
                primary = taxonomies[0]
                taxonomy_code = primary.get("code", "")
                specialty = primary.get("desc", "")
            
            # Extract address and phone
            addresses = entry.get("addresses", [])
            address = None
            zip_code = None
            phone = None
            
            # Prefer primary location, fall back to first address
            primary_address = None
            for addr in addresses:
                if addr.get("address_purpose") == "LOCATION":
                    primary_address = addr
                    break
            
            if not primary_address and addresses:
                primary_address = addresses[0]
            
            if primary_address:
                address_parts = [
                    primary_address.get("address_1", ""),
                    primary_address.get("address_2", ""),
                    primary_address.get("city", ""),
                    primary_address.get("state", ""),
                ]
                address = ", ".join([p for p in address_parts if p]).strip()
                zip_code = primary_address.get("postal_code", "").split("-")[0]  # Get 5-digit ZIP
                phone = primary_address.get("telephone_number", "")
            
            return Provider(
                npi=npi,
                name=name,
                specialty=specialty,
                taxonomy_code=taxonomy_code,
                phone=phone,
                address=address,
                zip_code=zip_code,
                entity_type=entity_type,
                raw_data=entry
            )
        except Exception:
            return None
    
    def close(self):
        """Close the HTTP client."""
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

