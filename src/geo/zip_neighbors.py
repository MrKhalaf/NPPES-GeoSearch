"""ZIP code neighbor loading and iteration utilities."""

import json
import os
from typing import List, Set, Iterator, Optional
from pathlib import Path


def load_zip_neighbors(data_path: Optional[str] = None) -> dict:
    """Load ZIP code neighbors from JSON file.
    
    Args:
        data_path: Optional path to JSON file. If None, looks in data/ directory.
        
    Returns:
        Dictionary mapping ZIP codes to lists of neighbor ZIP codes
        
    Raises:
        FileNotFoundError: If the data file cannot be found
        json.JSONDecodeError: If the file is not valid JSON
    """
    if data_path is None:
        # Default to data directory in project root
        project_root = Path(__file__).parent.parent.parent
        data_path = project_root / "data" / "zip_neighbors_20mi.json"
    
    data_path = Path(data_path)
    
    if not data_path.exists():
        raise FileNotFoundError(f"ZIP neighbors data file not found: {data_path}")
    
    with open(data_path, 'r') as f:
        return json.load(f)


def get_neighbors(zip_code: str, neighbors_data: dict) -> List[str]:
    """Get neighbor ZIP codes for a given ZIP code.
    
    Args:
        zip_code: 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists
        
    Returns:
        List of neighbor ZIP codes, empty list if ZIP not found
    """
    zip_str = str(zip_code).strip()
    return neighbors_data.get(zip_str, [])


def iter_zip_search_set(zip_code: str, neighbors_data: dict, include_neighbors: bool = True) -> Iterator[str]:
    """Iterate through ZIP codes to search, starting with origin then neighbors.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists
        include_neighbors: If True, include neighbors; if False, only origin
        
    Yields:
        ZIP codes in search order (origin first, then neighbors)
    """
    zip_str = str(zip_code).strip()
    
    # Always yield origin first
    yield zip_str
    
    # Then yield neighbors if requested
    if include_neighbors:
        neighbors = get_neighbors(zip_str, neighbors_data)
        for neighbor in neighbors:
            yield neighbor


def get_search_set(zip_code: str, neighbors_data: dict, include_neighbors: bool = True) -> List[str]:
    """Get the full list of ZIP codes to search.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists
        include_neighbors: If True, include neighbors; if False, only origin
        
    Returns:
        List of ZIP codes in search order
    """
    return list(iter_zip_search_set(zip_code, neighbors_data, include_neighbors))

