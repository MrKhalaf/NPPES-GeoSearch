"""ZIP code neighbor utilities using uszipcode library."""

from typing import List, Iterator, Optional
from .zip_neighbor_finder import ZIPNeighborFinder


# Global neighbor finder instance (lazy-loaded)
_neighbor_finder: Optional[ZIPNeighborFinder] = None


def _get_neighbor_finder() -> Optional[ZIPNeighborFinder]:
    """Get or create the ZIP neighbor finder instance.
    
    Returns:
        ZIPNeighborFinder instance or None if uszipcode not available
    """
    global _neighbor_finder
    if _neighbor_finder is None:
        try:
            _neighbor_finder = ZIPNeighborFinder()
        except Exception as e:
            print(f"Warning: Could not initialize ZIP neighbor finder: {e}")
            print("  Install uszipcode library: pip install uszipcode")
            return None
    return _neighbor_finder


def get_neighbors(zip_code: str, radius_miles: float = 20.0, max_results: int = 30) -> List[str]:
    """Get neighbor ZIP codes within radius using uszipcode.
    
    Args:
        zip_code: 5-digit ZIP code
        radius_miles: Search radius in miles (default: 20)
        max_results: Maximum number of neighbors to return (default: 30)
        
    Returns:
        List of neighbor ZIP codes (limited to max_results)
    """
    zip_str = str(zip_code).strip()
    
    finder = _get_neighbor_finder()
    if not finder:
        return []
    
    try:
        neighbors = finder.find_neighbors(zip_str, radius_miles=radius_miles, max_results=max_results)
        return neighbors
    except Exception as e:
        print(f"Error finding neighbors for ZIP {zip_str}: {e}")
        return []


def iter_zip_search_set(zip_code: str, include_neighbors: bool = True, radius_miles: float = 20.0, max_neighbors: int = 30) -> Iterator[str]:
    """Iterate through ZIP codes to search, starting with origin then neighbors.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        include_neighbors: If True, include neighbors; if False, only origin
        radius_miles: Search radius in miles for neighbors (default: 20)
        max_neighbors: Maximum number of neighbors to include (default: 30)
        
    Yields:
        ZIP codes in search order (origin first, then neighbors)
    """
    zip_str = str(zip_code).strip()
    
    # Always yield origin first
    yield zip_str
    
    # Then yield neighbors if requested
    if include_neighbors:
        neighbors = get_neighbors(zip_str, radius_miles=radius_miles, max_results=max_neighbors)
        for neighbor in neighbors:
            yield neighbor


def get_search_set(zip_code: str, include_neighbors: bool = True, radius_miles: float = 20.0, max_neighbors: int = 30) -> List[str]:
    """Get the full list of ZIP codes to search.
    
    Args:
        zip_code: Origin 5-digit ZIP code
        include_neighbors: If True, include neighbors; if False, only origin
        radius_miles: Search radius in miles for neighbors (default: 20)
        max_neighbors: Maximum number of neighbors to include (default: 30)
        
    Returns:
        List of ZIP codes in search order
    """
    return list(iter_zip_search_set(zip_code, include_neighbors, radius_miles, max_neighbors))
