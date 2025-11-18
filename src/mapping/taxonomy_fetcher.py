"""Utility to fetch and update taxonomy code descriptions from reliable sources.

The NUCC (National Uniform Claim Committee) maintains the official taxonomy code set.
The dataset is available at:
- CMS: https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/health-care-taxonomy
- NUCC: https://www.nucc.org/

The taxonomy code set is updated biannually (January and July).
"""

import httpx
from typing import Dict, Set
import json


def fetch_taxonomy_descriptions_from_nppes(sample_size: int = 1000) -> Dict[str, str]:
    """Fetch taxonomy code descriptions by sampling NPPES API results.
    
    This builds a mapping by querying the NPPES API and extracting
    taxonomy codes and their descriptions from provider records.
    
    Args:
        sample_size: Number of providers to sample (across multiple ZIP codes)
        
    Returns:
        Dictionary mapping taxonomy codes to their descriptions
    """
    client = httpx.Client(timeout=30.0)
    base_url = 'https://npiregistry.cms.hhs.gov/api'
    
    # Sample ZIP codes from different regions
    sample_zips = [
        '10001', '90210', '60601', '77001', '33101',  # Major cities
        '02101', '30301', '98101', '19101', '75201',
    ]
    
    taxonomy_map: Dict[str, str] = {}
    providers_checked = 0
    
    for zip_code in sample_zips:
        if providers_checked >= sample_size:
            break
            
        params = {
            'version': '2.1',
            'postal_code': zip_code,
            'limit': min(200, sample_size - providers_checked),
            'enumeration_type': '1'
        }
        
        try:
            response = client.get(base_url, params=params)
            data = response.json()
            results = data.get('results', [])
            
            for provider in results:
                taxonomies = provider.get('taxonomies', [])
                for tax in taxonomies:
                    code = tax.get('code', '')
                    desc = tax.get('desc', '')
                    if code and desc:
                        taxonomy_map[code] = desc
                
                providers_checked += 1
                if providers_checked >= sample_size:
                    break
        except Exception as e:
            print(f"Error fetching from ZIP {zip_code}: {e}")
            continue
    
    return taxonomy_map


def get_nppes_accepted_description(taxonomy_code: str, taxonomy_map: Dict[str, str]) -> str:
    """Get the NPPES API-accepted description for a taxonomy code.
    
    The NPPES API accepts shorter, simpler descriptions. This function
    extracts the base description that works with the API.
    
    Args:
        taxonomy_code: Taxonomy code (e.g., "207X00000X")
        taxonomy_map: Dictionary mapping codes to full descriptions
        
    Returns:
        API-accepted description (e.g., "Orthopedic" instead of "Orthopedic Surgery")
    """
    full_desc = taxonomy_map.get(taxonomy_code, '')
    
    # Map known variations to API-accepted format
    # Based on testing, the API accepts shorter descriptions
    description_mappings = {
        'Orthopedic Surgery': 'Orthopedic',
        'Orthopedic Surgeon': 'Orthopedic',
        'Family Practice': 'Family Medicine',
        'General Practice': 'General Practice',
    }
    
    # Check if we have a known mapping
    if full_desc in description_mappings:
        return description_mappings[full_desc]
    
    # For most cases, the full description works
    # But remove common suffixes that might cause issues
    if full_desc.endswith(' Surgery'):
        return full_desc.replace(' Surgery', '')
    if full_desc.endswith(' Surgeon'):
        return full_desc.replace(' Surgeon', '')
    
    return full_desc


# Note: For a complete taxonomy code dataset, download from:
# - CMS: https://www.cms.gov/medicare/enrollment-renewal/providers-suppliers/health-care-taxonomy
# - NUCC: https://www.nucc.org/
# The dataset is updated biannually (January and July)

