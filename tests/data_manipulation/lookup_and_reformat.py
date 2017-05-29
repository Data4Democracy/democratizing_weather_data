"""
This module contains the tests for joining and transforming data.

(c) Data for Democracy
"""

import unittest
import os


class TestJoinsAndTransforms(unittest.TestCase):
    """
    Test suite for all data joins and transforms for 
    """
    def setUp(self):
        self.fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')


if __name__ == '__main__':
    unittest.main()
