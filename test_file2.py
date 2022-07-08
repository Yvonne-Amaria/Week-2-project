import unittest
from file2 import get_report, get_forecast
import requests
import json
import sqlalchemy as db
import pandas as pd



class Testfile2(unittest.TestCase):
    def test_get_report(self):
        self.assertIn(get_report, (name, country, weather_condition, temp_f, temp_c, humidity,wind))

if __name__ == '__main__':
    unittest.main()