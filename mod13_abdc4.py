import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
import main

class TestInputs(unittest.TestCase):
    def test_symbol_valid(self, mock_input):
        self.assertEqual(main.get_stock_symbol(), "AAPL")
    
    def test_symbol_empty_then_valid(self, mock_input):
        result = main.get_stock_symbol()
        self.assertEqual(result, "MSFT")
        self.assertIn("Enter a valid stock symbol.", output.getvalue())
    
    def text_symbol_allows_invalid_format(self, mock_input):
        self.assertEqual(main.get_stock_symbol(), "1234")

    def test_chart_type_bar(self, mock_input):
        self.assertEqual(main.get_chart_type(), "bar")
    
    def test_chart_type_line(self, mock_input):
        self.assertEqual(main.get_chart_type(), "line")
    
    def test_chart_type_invalid_then_valid(self, mock_input):
        result = main.get_chart_type()
        self.assertEqual(result, "line")
        self.assertIn("Error", output.getvalue())
    
    def test_series_valid(self):
        valid = ["1", "2", "3", "4"]
        for choice in valid:
            self.assertIN(choice, ["1", "2", "3", "4"])
    
    def test_time_series_invalid(self):
        invalid = ["0", "5", "a", "12"]
        for choice in invalid:
            self.assertNotIN(choice, ["1", "2", "3", "4"])
    
    def test_valid_date(self, mock_input):
        result = main.get_valid_date("Enter date: ")
        self.assertEqual(result, datetime(2022, 1, 1))

    def test_invalid_then_valid_date(self, mock_input):
        result = main.get_valid_date("Enter date: ")
        self.assertEqual(result, datetime(2022, 1, 1))
        self.assertIN("YYYY-MM-DD", output.getvalue())
    
    def test_date_range_validation(self, mock_input):
        start, end = main.get_date_range()
        self.assertEqual(start, datetime(2022, 1, 1))
        self.assertEqual(end, datetime(2022, 12, 31))
        self.assertIn("End date cannot be before start date", output.getvalue())
    
if __name__ == "__main__":
    unittest.main()