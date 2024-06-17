import pandas as pd
import unittest
import sys
import os
from pec4.ex1 import *

class TestDataEx1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset for test_ex1")
        cls._df = pd.read_csv("data/nics-firearm-background-checks.csv")
        cls._df_cleaned = clean_csv(cls._df, False)

    def test_is_dataframe_ex1(self):
        print("Starting test_is_dataframe")
        self.assertIsInstance(read_csv("data/nics-firearm-background-checks.csv", False), pd.DataFrame)

    def test_clean_csv_ex1(self):
        print("Starting test_clean_csv_ex1")
        self.assertEqual(clean_csv(self._df, False).shape[1], 5)

    def test_rename_col_ex1(self):
        print("Starting test_rename_col_ex1")
        column = "longgun"
        self.assertIn(column, rename_col(self._df_cleaned, False).columns)