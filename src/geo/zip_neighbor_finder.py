"""ZIP code neighbor finder using coordinates and distance calculation."""

from typing import List, Optional
import math


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points using Haversine formula.
    
    Args:
        lat1, lon1: Latitude and longitude of first point
        lat2, lon2: Latitude and longitude of second point
        
    Returns:
        Distance in miles
    """
    R = 3959  # Earth's radius in miles
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c


class ZIPNeighborFinder:
    """Find neighboring ZIP codes within a specified radius."""
    
    def __init__(self):
        """Initialize the ZIP neighbor finder."""
        self.zip_coordinates = {}
        self._load_zip_coordinates()
    
    def _load_zip_coordinates(self):
        """Load ZIP code coordinates. Uses uszipcode library if available, otherwise empty."""
        try:
            from uszipcode import SearchEngine
            search = SearchEngine()
            
            self.search_engine = search
            self.use_library = True
        except ImportError:
            raise ImportError(
                "uszipcode library not found. Install with: pip install uszipcode"
            )
    
    def get_zip_coordinates(self, zip_code: str) -> Optional[tuple]:
        """Get latitude and longitude for a ZIP code.
        
        Args:
            zip_code: 5-digit ZIP code
            
        Returns:
            Tuple of (latitude, longitude) or None if not found
        """
        if not self.use_library:
            return None
        
        try:
            result = self.search_engine.by_zipcode(zip_code)
            if result and result.lat and result.lng:
                return (result.lat, result.lng)
        except Exception as e:
            print(f"Error getting coordinates for ZIP {zip_code}: {e}")
        
        return None
    
    def find_neighbors(self, zip_code: str, radius_miles: float = 20.0, max_results: int = 30) -> List[str]:
        """Find neighboring ZIP codes within radius, reducing radius if too many found.
        
        Args:
            zip_code: Origin 5-digit ZIP code
            radius_miles: Starting search radius in miles (default: 20)
            max_results: Maximum number of neighbors to return (default: 30)
            
        Returns:
            List of neighboring ZIP codes (within adjusted radius to get <= max_results)
        """
        if not self.use_library:
            return []
        
        origin_coords = self.get_zip_coordinates(zip_code)
        if not origin_coords:
            return []
        
        origin_lat, origin_lon = origin_coords
        
        # Try progressively smaller radii until we get <= max_results neighbors
        radii_to_try = [radius_miles, 10.0, 5.0, 2.0]
        
        for current_radius in radii_to_try:
            try:
                search = self.search_engine
                
                # Search for ZIP codes within current radius
                # Fetch more than max_results to account for origin being in results
                nearby_results = search.by_coordinates(
                    origin_lat, origin_lon, 
                    radius=current_radius, 
                    returns=max_results + 10
                )
                
                if nearby_results:
                    neighbors = []
                    for result in nearby_results:
                        # Skip the origin ZIP code itself
                        if result.zipcode and result.zipcode != zip_code:
                            # Verify distance
                            if result.lat and result.lng:
                                distance = haversine_distance(
                                    origin_lat, origin_lon,
                                    result.lat, result.lng
                                )
                                if distance <= current_radius:
                                    neighbors.append(result.zipcode)
                    
                    # If we have <= max_results neighbors, return them
                    if len(neighbors) <= max_results:
                        if current_radius < radius_miles:
                            print(f"Reduced radius to {current_radius} miles to get {len(neighbors)} neighbors (target: {max_results})")
                        return neighbors
                    # Otherwise, continue to next smaller radius
                        
            except Exception as e:
                print(f"Error finding neighbors for ZIP {zip_code} at radius {current_radius}: {e}")
                import traceback
                traceback.print_exc()
                continue
        
        # If we still have too many even at 2 miles, just return the first max_results
        # This shouldn't happen often, but handle it gracefully
        if nearby_results:
            neighbors = []
            for result in nearby_results:
                if result.zipcode and result.zipcode != zip_code:
                    if result.lat and result.lng:
                        distance = haversine_distance(
                            origin_lat, origin_lon,
                            result.lat, result.lng
                        )
                        if distance <= 2.0:
                            neighbors.append(result.zipcode)
                            if len(neighbors) >= max_results:
                                break
            return neighbors
        
        return []

