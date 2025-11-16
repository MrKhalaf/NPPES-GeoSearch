"""ZIP code neighbor loading and iteration utilities."""

import json
import os
from typing import List, Set, Iterator, Optional
from pathlib import Path
from .zip_neighbor_finder import ZIPNeighborFinder


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


# Global neighbor finder instance (lazy-loaded)
_neighbor_finder: Optional[ZIPNeighborFinder] = None


def _get_neighbor_finder() -> Optional[ZIPNeighborFinder]:
    """Get or create the ZIP neighbor finder instance."""
    global _neighbor_finder
    if _neighbor_finder is None:
        try:
            _neighbor_finder = ZIPNeighborFinder()
        except Exception as e:
            print(f"Warning: Could not initialize ZIP neighbor finder: {e}")
            return None
    return _neighbor_finder


def get_neighbors(zip_code: str, neighbors_data: dict, use_dynamic: bool = True) -> List[str]:
    """Get neighbor ZIP codes, checking both file data and dynamic lookup.
    
    Args:
        zip_code: 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists (from file)
        use_dynamic: If True, use dynamic lookup when file data not available
        
    Returns:
        List of neighbor ZIP codes
    """
    zip_str = str(zip_code).strip()
    
    # First check file data
    neighbors = neighbors_data.get(zip_str, [])
    
    # If no neighbors found in file and dynamic lookup enabled, try dynamic lookup
    if not neighbors and use_dynamic:
        finder = _get_neighbor_finder()
        if finder:
            try:
                dynamic_neighbors = finder.find_neighbors(zip_str, radius_miles=20.0)
                if dynamic_neighbors:
                    print(f"Found {len(dynamic_neighbors)} neighbors for ZIP {zip_str} using dynamic lookup")
                    neighbors = dynamic_neighbors
            except Exception as e:
                print(f"Error in dynamic neighbor lookup for ZIP {zip_str}: {e}")
    
    return neighbors


def iter_zip_search_set(zip_code: str, neighbors_data: dict, include_neighbors: bool = True, use_dynamic: bool = True) -> Iterator[str]:
    """Iterate through ZIP codes to search, starting with origin then neighbors.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists
        include_neighbors: If True, include neighbors; if False, only origin
        use_dynamic: If True, use dynamic lookup when file data not available
        
    Yields:
        ZIP codes in search order (origin first, then neighbors)
    """
    zip_str = str(zip_code).strip()
    
    # Always yield origin first
    yield zip_str
    
    # Then yield neighbors if requested
    if include_neighbors:
        neighbors = get_neighbors(zip_str, neighbors_data, use_dynamic=use_dynamic)
        for neighbor in neighbors:
            yield neighbor


def get_search_set(zip_code: str, neighbors_data: dict, include_neighbors: bool = True, use_dynamic: bool = True) -> List[str]:
    """Get the full list of ZIP codes to search.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        neighbors_data: Dictionary mapping ZIP codes to neighbor lists
        include_neighbors: If True, include neighbors; if False, only origin
        use_dynamic: If True, use dynamic lookup when file data not available
        
    Returns:
        List of ZIP codes in search order
    """
    return list(iter_zip_search_set(zip_code, neighbors_data, include_neighbors, use_dynamic))

