"""File to hold a class definition to test code"""

import unittest


class TestListElements(unittest.TestCase):
    """Holding class to organize our test cases."""

    def test_sorting():
        """Test to make sure the sorting function works with a simple list"""

        known_input = [5,4,1,2,3]
        expected_output = [1,2,3,4,5]
        assertListEqual(known_input, known_output)
