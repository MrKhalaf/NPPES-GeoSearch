"""Tests for ZIP code neighbor finding functionality."""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.geo.zip_neighbor_finder import ZIPNeighborFinder, haversine_distance
from src.geo.zip_neighbors import get_neighbors, get_search_set, iter_zip_search_set


class TestHaversineDistance(unittest.TestCase):
    """Test haversine distance calculation."""
    
    def test_same_point(self):
        """Distance from a point to itself should be 0."""
        distance = haversine_distance(38.86, -77.15, 38.86, -77.15)
        self.assertAlmostEqual(distance, 0.0, places=2)
    
    def test_known_distance(self):
        """Test distance between two known points."""
        # Falls Church, VA (22044) to Arlington, VA (22205)
        # Should be approximately 1.5 miles
        distance = haversine_distance(38.86, -77.15, 38.88, -77.11)
        self.assertGreater(distance, 1.0)
        self.assertLess(distance, 3.0)  # Adjusted for actual calculated distance
    
    def test_different_coordinates(self):
        """Distance should be positive for different points."""
        distance = haversine_distance(38.86, -77.15, 34.05, -118.24)  # VA to CA
        self.assertGreater(distance, 2000)  # Should be thousands of miles


class TestZIPNeighborFinder(unittest.TestCase):
    """Test ZIPNeighborFinder class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Mock the SearchEngine to avoid actual database calls
        self.mock_search = Mock()
        self.mock_search.by_zipcode.return_value = Mock(lat=38.86, lng=-77.15)
        
        # Patch uszipcode.SearchEngine at the module level where it's imported
        self.patcher = patch('uszipcode.SearchEngine', return_value=self.mock_search)
        self.patcher.start()
        # Re-initialize finder after patching
        self.finder = ZIPNeighborFinder()
    
    def tearDown(self):
        """Clean up after tests."""
        self.patcher.stop()
    
    def test_get_zip_coordinates_success(self):
        """Test getting coordinates for a valid ZIP code."""
        coords = self.finder.get_zip_coordinates('22044')
        self.assertIsNotNone(coords)
        self.assertEqual(coords, (38.86, -77.15))
    
    def test_get_zip_coordinates_not_found(self):
        """Test getting coordinates for invalid ZIP code."""
        self.mock_search.by_zipcode.return_value = None
        coords = self.finder.get_zip_coordinates('99999')
        self.assertIsNone(coords)
    
    def test_find_neighbors_few_results_at_20_miles(self):
        """Test when there are few neighbors at 20 miles - should return all."""
        # Mock results: only 5 neighbors at 20 miles (use different ZIP codes)
        mock_results = []
        neighbor_zips = ['22041', '22046', '22205', '22203', '22311']
        for i, zip_code in enumerate(neighbor_zips):
            mock_result = Mock()
            mock_result.zipcode = zip_code
            mock_result.lat = 38.86 + (i * 0.01)
            mock_result.lng = -77.15 + (i * 0.01)
            mock_results.append(mock_result)
        
        self.mock_search.by_coordinates.return_value = mock_results
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should return all 5 neighbors (within 20 miles)
        self.assertEqual(len(neighbors), 5)
        self.assertEqual(radius, 20.0)
        self.mock_search.by_coordinates.assert_called_once()
        call_args = self.mock_search.by_coordinates.call_args
        self.assertEqual(call_args[1]['radius'], 20.0)
    
    def test_find_neighbors_too_many_at_20_reduces_to_10(self):
        """Test when too many neighbors at 20 miles, reduces to 10 miles."""
        # Mock results: 50 neighbors at 20 miles, 25 at 10 miles
        many_results_20 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)]
        few_results_10 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(25)]
        
        # First call returns many, second call returns few
        self.mock_search.by_coordinates.side_effect = [many_results_20, few_results_10]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should have called twice (20 miles, then 10 miles)
        self.assertEqual(self.mock_search.by_coordinates.call_count, 2)
        # Should return 25 neighbors (within 10 miles)
        self.assertEqual(len(neighbors), 25)
        self.assertEqual(radius, 10.0)
        # Verify second call was with 10 mile radius
        second_call = self.mock_search.by_coordinates.call_args_list[1]
        self.assertEqual(second_call[1]['radius'], 10.0)
    
    def test_find_neighbors_reduces_to_5_miles(self):
        """Test radius reduction to 5 miles."""
        # Mock: too many at 20, too many at 10, but <=30 at 5
        many_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)]
        few_results_5 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(20)]
        
        self.mock_search.by_coordinates.side_effect = [many_results, many_results, few_results_5]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should have called 3 times (20, 10, 5)
        self.assertEqual(self.mock_search.by_coordinates.call_count, 3)
        self.assertEqual(len(neighbors), 20)
        self.assertEqual(radius, 5.0)
        # Verify third call was with 5 mile radius
        third_call = self.mock_search.by_coordinates.call_args_list[2]
        self.assertEqual(third_call[1]['radius'], 5.0)
    
    def test_find_neighbors_reduces_to_2_miles(self):
        """Test radius reduction to 2 miles."""
        # Mock: too many at all larger radii, but <=30 at 2
        many_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)]
        few_results_2 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(15)]
        
        self.mock_search.by_coordinates.side_effect = [many_results, many_results, many_results, few_results_2]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should have called 4 times (20, 10, 5, 2)
        self.assertEqual(self.mock_search.by_coordinates.call_count, 4)
        self.assertEqual(len(neighbors), 15)
        self.assertEqual(radius, 2.0)
        # Verify fourth call was with 2 mile radius
        fourth_call = self.mock_search.by_coordinates.call_args_list[3]
        self.assertEqual(fourth_call[1]['radius'], 2.0)
    
    def test_find_neighbors_exactly_30_at_20_miles(self):
        """Test when exactly 30 neighbors at 20 miles."""
        exact_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(30)]
        self.mock_search.by_coordinates.return_value = exact_results
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should return all 30, only call once
        self.assertEqual(len(neighbors), 30)
        self.assertEqual(radius, 20.0)
        self.mock_search.by_coordinates.assert_called_once()
    
    def test_find_neighbors_no_results(self):
        """Test when no neighbors found."""
        # Return empty list or list with only origin
        self.mock_search.by_coordinates.return_value = []
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        self.assertEqual(len(neighbors), 0)
        self.assertEqual(radius, 20.0)
    
    def test_find_neighbors_excludes_origin(self):
        """Test that origin ZIP code is excluded from results."""
        mock_results = [
            Mock(zipcode='22044', lat=38.86, lng=-77.15),  # Origin
            Mock(zipcode='22041', lat=38.87, lng=-77.14),  # Neighbor
            Mock(zipcode='22046', lat=38.85, lng=-77.16),  # Neighbor
        ]
        self.mock_search.by_coordinates.return_value = mock_results
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should exclude origin
        self.assertNotIn('22044', neighbors)
        self.assertEqual(len(neighbors), 2)
        self.assertEqual(radius, 20.0)
    
    def test_find_neighbors_all_within_radius(self):
        """Test that all returned neighbors are within the final radius."""
        # Create results at different distances
        mock_results_5 = [
            Mock(zipcode='22041', lat=38.87, lng=-77.14),  # ~1.5 miles
            Mock(zipcode='22046', lat=38.85, lng=-77.16),  # ~1.5 miles
        ]
        # At 5 miles, we get these 2 neighbors
        self.mock_search.by_coordinates.side_effect = [
            [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)],  # Too many at 20
            [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)],  # Too many at 10
            mock_results_5,  # 2 at 5 miles
        ]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should return 2 neighbors, all within 5 miles
        self.assertEqual(len(neighbors), 2)
        self.assertEqual(radius, 5.0)
        self.assertIn('22041', neighbors)
        self.assertIn('22046', neighbors)


class TestZIPNeighborsModule(unittest.TestCase):
    """Test the zip_neighbors module functions."""
    
    @patch('src.geo.zip_neighbors._get_neighbor_finder')
    def test_get_neighbors(self, mock_get_finder):
        """Test get_neighbors function."""
        mock_finder = Mock()
        mock_finder.find_neighbors.return_value = (['22041', '22046', '22205'], 20.0)
        mock_get_finder.return_value = mock_finder
        
        neighbors, radius = get_neighbors('22044', radius_miles=20.0, max_results=30)
        
        self.assertEqual(neighbors, ['22041', '22046', '22205'])
        self.assertEqual(radius, 20.0)
        mock_finder.find_neighbors.assert_called_once_with('22044', radius_miles=20.0, max_results=30)
    
    @patch('src.geo.zip_neighbors._get_neighbor_finder')
    def test_get_neighbors_no_finder(self, mock_get_finder):
        """Test get_neighbors when finder is not available."""
        mock_get_finder.return_value = None
        
        neighbors, radius = get_neighbors('22044', radius_miles=20.0, max_results=30)
        
        self.assertEqual(neighbors, [])
        self.assertEqual(radius, 20.0)
    
    def test_iter_zip_search_set_with_neighbors(self):
        """Test iterating ZIP search set with neighbors."""
        with patch('src.geo.zip_neighbors.get_neighbors', return_value=(['22041', '22046'], 20.0)):
            search_set = list(iter_zip_search_set('22044', include_neighbors=True, max_neighbors=30))
            
            self.assertEqual(search_set[0], '22044')  # Origin first
            self.assertIn('22041', search_set)
            self.assertIn('22046', search_set)
            self.assertEqual(len(search_set), 3)
    
    def test_iter_zip_search_set_without_neighbors(self):
        """Test iterating ZIP search set without neighbors."""
        search_set = list(iter_zip_search_set('22044', include_neighbors=False, max_neighbors=30))
        
        self.assertEqual(search_set, ['22044'])  # Only origin
    
    def test_get_search_set(self):
        """Test get_search_set function."""
        with patch('src.geo.zip_neighbors.get_neighbors', return_value=(['22041', '22046'], 20.0)):
            search_set, radius = get_search_set('22044', include_neighbors=True, max_neighbors=30)
            
            self.assertEqual(search_set[0], '22044')  # Origin first
            self.assertEqual(len(search_set), 3)
            self.assertEqual(radius, 20.0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_search = Mock()
        self.mock_search.by_zipcode.return_value = Mock(lat=38.86, lng=-77.15)
        
        # Patch uszipcode.SearchEngine at the module level where it's imported
        self.patcher = patch('uszipcode.SearchEngine', return_value=self.mock_search)
        self.patcher.start()
        # Re-initialize finder after patching
        self.finder = ZIPNeighborFinder()
    
    def tearDown(self):
        """Clean up after tests."""
        self.patcher.stop()
    
    def test_max_results_boundary_29(self):
        """Test with 29 neighbors (just under limit)."""
        results_29 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(29)]
        self.mock_search.by_coordinates.return_value = results_29
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        self.assertEqual(len(neighbors), 29)
        self.assertEqual(radius, 20.0)
        self.mock_search.by_coordinates.assert_called_once()
    
    def test_max_results_boundary_30(self):
        """Test with exactly 30 neighbors."""
        results_30 = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(30)]
        self.mock_search.by_coordinates.return_value = results_30
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        self.assertEqual(len(neighbors), 30)
        self.assertEqual(radius, 20.0)
    
    def test_max_results_boundary_31(self):
        """Test with 31 neighbors (just over limit, should reduce radius)."""
        many_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(31)]
        few_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(25)]
        
        self.mock_search.by_coordinates.side_effect = [many_results, few_results]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=30)
        
        # Should reduce radius and return 25
        self.assertEqual(len(neighbors), 25)
        self.assertEqual(self.mock_search.by_coordinates.call_count, 2)
        self.assertEqual(radius, 10.0)
    
    def test_custom_max_results(self):
        """Test with custom max_results value."""
        many_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)]
        few_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(10)]
        
        self.mock_search.by_coordinates.side_effect = [many_results, few_results]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=20.0, max_results=10)
        
        self.assertEqual(len(neighbors), 10)
        self.assertEqual(self.mock_search.by_coordinates.call_count, 2)
        self.assertEqual(radius, 10.0)
    
    def test_custom_starting_radius(self):
        """Test with custom starting radius."""
        many_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(50)]
        few_results = [Mock(zipcode=f'2204{i:02d}', lat=38.86, lng=-77.15) for i in range(20)]
        
        self.mock_search.by_coordinates.side_effect = [many_results, few_results]
        
        neighbors, radius = self.finder.find_neighbors('22044', radius_miles=15.0, max_results=30)
        
        # Should start at 15, then try 10
        first_call = self.mock_search.by_coordinates.call_args_list[0]
        self.assertEqual(first_call[1]['radius'], 15.0)
        self.assertEqual(radius, 10.0)


if __name__ == '__main__':
    unittest.main()

