import pandas as pd
import unittest
import sys
import os
from pec4.ex1 import *
from pec4.ex2 import *


class TestDataEx2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset for test_ex1")
        cls._df = pd.read_csv("data/nics-firearm-background-checks.csv")
        cls._df_cleaned = clean_csv(cls._df, False)
        cls._df_rename = rename_col(cls._df_cleaned, False)
        #cls._df_break_date = breakdown_date(cls._df_rename, False)

    def test_is_year_ex2(self):
        print("Starting test_is_year_ex2")
        column = "year"
        self.assertIn(column, breakdown_date(self._df_rename, False).columns)