import pandas as pd
import unittest
import sys
import os
from pec4.ex1 import *
from pec4.ex2 import *
from pec4.ex3 import *


class TestDataEx3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading datasets for test_ex1")
        cls._df = pd.read_csv("data/nics-firearm-background-checks.csv")
        cls._df_cleaned = clean_csv(cls._df, False)
        cls._df_rename = rename_col(cls._df_cleaned, False)
        cls._df_break_date = breakdown_date(cls._df_rename, False)
        cls._df_groupby_state = groupby_state_and_year(cls._df_break_date, False)

    def test_is_max_ex3(self):
        print("Starting test_is_max_ex3")
        row_max = "handgun"
        idx_max = self._df_groupby_state[row_max].idxmax()
        max_row = self._df_groupby_state.loc[idx_max]
        max_number = max_row[row_max]
        self.assertEqual(max_number, 662308)