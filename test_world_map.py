import unittest
from unittest.mock import patch
import world_map_dots

class TestWorldMap(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    def test_plot_world_map(self, mock_show):
        try:
            world_map_dots.plot_world_map()
        except Exception as e:
            self.fail(f"plot_world_map() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
