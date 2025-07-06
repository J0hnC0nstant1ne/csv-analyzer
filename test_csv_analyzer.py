import unittest
from csv_analyzer import filter_data

sample_data = [
    {"Name": "Alice", "Salary": "60000"},
    {"Name": "Bob", "Salary": "45000"},
    {"Name": "Charlie", "Salary": "70000"},
    {"Name": "Diana", "Salary": "30000"}
]

class TestCSVAnalyzer(unittest.TestCase):

    def test_filter_data_greater_than(self):
        result = filter_data(sample_data, "Salary", "greater_than", "50000")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Name"], "Alice")
        self.assertEqual(result[1]["Name"], "Charlie")

    def test_filter_data_less_than(self):
        result = filter_data(sample_data, "Salary", "less_than", "50000")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["Name"], "Bob")
        self.assertEqual(result[1]["Name"], "Diana")

    def test_filter_data_equal(self):
        result = filter_data(sample_data, "Salary", "equals", "60000")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Name"], "Alice")

if __name__ == "__main__":
    unittest.main()
