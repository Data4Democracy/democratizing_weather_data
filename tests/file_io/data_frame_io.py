"""
This module contains the code that tests all of the IO
functionality for this package.

(c) Data for Democracy
"""

import unittest
import os
import pandas as pd
from democratizing_weather_data.file_io.data_frame_io import read_wban_csv
from democratizing_weather_data.file_io.data_frame_io import read_lookup_info


class TestCSVIO(unittest.TestCase):
    """
    Class that tests all of the CSV IO capabilities for this package.
    """

    def setUp(self):
        self.fixture_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'fixtures'
        )
        self.wban_csv = os.path.join(self.fixture_dir, '200902daily.txt')
        self.lookup_csv = os.path.join(self.fixture_dir, '200902station.txt')

    def TestReadWBANCSV(self):
        """
        Test whether a WBAN DataFrame can be read from it's text file.
        """

        wban_frame = read_wban_csv(self.wban_csv)

        self.assertTrue(isinstance(wban_frame, pd.DataFrame))


    def TestReadSTNLookup(self):
        """
        Test whether a station Lookup information DataFrame can be 
        gathered from it's text file.
        """

        lookup_frame = read_lookup_info(self.lookup_csv)

        self.assertTrue(isinstance(lookup_frame, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()