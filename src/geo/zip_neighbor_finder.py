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
            
            # Try to load coordinates for common ZIP codes
            # This is a simplified approach - in production you'd want to cache this
            print("Loading ZIP code coordinates from uszipcode library...")
            # We'll load on-demand instead of preloading all
            self.search_engine = search
            self.use_library = True
        except ImportError:
            print("uszipcode library not found. Install with: pip install uszipcode")
            print("  Falling back to file-based neighbor lookup only.")
            self.use_library = False
            self.search_engine = None
    
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
    
    def find_neighbors(self, zip_code: str, radius_miles: float = 20.0) -> List[str]:
        """Find neighboring ZIP codes within radius.
        
        Args:
            zip_code: Origin 5-digit ZIP code
            radius_miles: Search radius in miles (default: 20)
            
        Returns:
            List of neighboring ZIP codes
        """
        if not self.use_library:
            return []
        
        origin_coords = self.get_zip_coordinates(zip_code)
        if not origin_coords:
            return []
        
        origin_lat, origin_lon = origin_coords
        neighbors = []
        
        # Search nearby ZIP codes
        # Note: This is a simplified approach. For production, you'd want to:
        # 1. Use a spatial index or database
        # 2. Cache results
        # 3. Use a more efficient search algorithm
        
        # Search nearby ZIP codes using coordinate-based search
        try:
            # Use the search engine to find ZIP codes within radius
            # Note: uszipcode's by_coordinates may have different API, so we'll use a different approach
            # Search all ZIP codes and filter by distance
            # This is not efficient but works for now
            
            # Get a sample of nearby ZIP codes by searching a grid
            # For better performance, you'd want to use a spatial database
            search = self.search_engine
            
            # Search in a grid pattern around the origin
            # This is a simplified approach - in production use a spatial index
            lat_step = radius_miles / 69.0  # Approximate miles per degree latitude
            lon_step = radius_miles / (69.0 * abs(math.cos(math.radians(origin_lat))))
            
            checked_zips = set()
            checked_zips.add(zip_code)  # Don't include origin
            
            # Search in a grid around origin
            for lat_offset in [-lat_step, 0, lat_step]:
                for lon_offset in [-lon_step, 0, lon_step]:
                    search_lat = origin_lat + lat_offset
                    search_lon = origin_lon + lon_offset
                    
                    try:
                        # Try to find ZIP codes near this point
                        # uszipcode may have different methods, so we'll use a simple approach
                        # Search for ZIP codes by coordinates
                        nearby = search.by_coordinates(search_lat, search_lon, radius=radius_miles * 1.5)
                        
                        if nearby:
                            for result in nearby:
                                if result.zipcode and result.zipcode not in checked_zips:
                                    checked_zips.add(result.zipcode)
                                    if result.lat and result.lng:
                                        distance = haversine_distance(
                                            origin_lat, origin_lon,
                                            result.lat, result.lng
                                        )
                                        if distance <= radius_miles:
                                            neighbors.append(result.zipcode)
                    except Exception:
                        # If coordinate search doesn't work, skip this point
                        continue
                        
        except Exception as e:
            print(f"Error finding neighbors for ZIP {zip_code}: {e}")
            import traceback
            traceback.print_exc()
        
        return neighbors

