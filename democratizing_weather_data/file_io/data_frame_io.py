"""
This module contains code that downloads QLCD data from NOAA and
reads them into Pandas DataFrames so that they can be properly
converted.

(c) Data for Democracy
"""

import pandas as pd


def read_wban_csv(wban_pathname):
    """
    Read WBAN csv file and get a Pandas DataFrmae representation
    of the data.
    
    Arguments: 
         wban_pathname (str): Full path to wban CSV file.
    Returns:
        (pandas.DataFrame): DataFrame representation of
        CSV file.
    """

    return pd.read_csv(wban_pathname)


def read_lookup_info(lookup_pathname):
    """
    Read lookup info that will be joined to the station
    data.
    
    Arguments:
        lookup_pathname (str): Full path to lookup location
    Returns:
        (pandas.DataFrame): DataFrame representation of lookup
        data
    """

    return pd.read_table(lookup_pathname, sep="|")
