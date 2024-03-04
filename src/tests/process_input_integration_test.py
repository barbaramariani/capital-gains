import unittest
from io import StringIO
from unittest.mock import patch

from infrastructure.helpers.input_helper import process_input_line


class TestProcessInputIntegration(unittest.TestCase):
    case_1_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":15.0, "quantity": 50}, {"operation":"sell", "unit-cost":15.0, "quantity": 50}]'
    case_2_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":20.0, "quantity": 5000}, {"operation":"sell", "unit-cost":5.0, "quantity": 5000}]'
    case_3_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":5.0, "quantity": 5000}, {"operation":"sell", "unit-cost":20.0, "quantity": 3000}]'
    case_4_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"buy", "unit-cost":25.0, "quantity": 5000}, {"operation":"sell", "unit-cost":15.0, "quantity": 10000}]'
    case_5_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"buy", "unit-cost":25.0, "quantity": 5000}, {"operation":"sell", "unit-cost":15.0, "quantity": 10000}, {"operation":"sell", "unit-cost":25.0, "quantity": 5000}]'
    case_6_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":2.0, "quantity": 5000}, {"operation":"sell", "unit-cost":20.0, "quantity": 2000}, {"operation":"sell", "unit-cost":20.0, "quantity": 2000}, {"operation":"sell", "unit-cost":25.0, "quantity": 1000}]'
    case_7_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":2.0, "quantity": 5000}, {"operation":"sell", "unit-cost":20.0, "quantity": 2000}, {"operation":"sell", "unit-cost":20.0, "quantity": 2000}, {"operation":"sell", "unit-cost":25.0, "quantity": 1000}, {"operation":"buy", "unit-cost":20.0, "quantity": 10000}, {"operation":"sell", "unit-cost":15.0, "quantity": 5000}, {"operation":"sell", "unit-cost":30.0, "quantity": 4350}, {"operation":"sell", "unit-cost":30.0, "quantity": 650}]'
    case_8_input = '[{"operation":"buy", "unit-cost":10.0, "quantity": 10000}, {"operation":"sell", "unit-cost":50.0, "quantity": 10000}, {"operation":"buy", "unit-cost":20.0, "quantity": 10000}, {"operation":"sell", "unit-cost":50.0, "quantity": 10000}]'

    def test_process_input_given_case_1_input_then_return_expected_output(self):
        result = process_input_line(self.case_1_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_2_input_then_return_expected_output(self):
        result = process_input_line(self.case_2_input)
        expected_output = '[{"tax": 0.0}, {"tax": 10000.0}, {"tax": 0.0}]'
        self.assertEqual(expected_output, result)
        
    def test_process_input_given_case_3_input_then_return_expected_output(self):
        result = process_input_line(self.case_3_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 1000.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_4_input_then_return_expected_output(self):
        result = process_input_line(self.case_4_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_5_input_then_return_expected_output(self):
        result = process_input_line(self.case_5_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 10000.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_6_input_then_return_expected_output(self):
        result = process_input_line(self.case_6_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 3000.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_7_input_then_return_expected_output(self):
        result = process_input_line(self.case_7_input)
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 3000.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 3700.0}, {"tax": 0.0}]'
        self.assertEqual(expected_output, result)

    def test_process_input_given_case_8_input_then_return_expected_output(self):
        result = process_input_line(self.case_8_input)
        expected_output = '[{"tax": 0.0}, {"tax": 80000.0}, {"tax": 0.0}, {"tax": 60000.0}]'
        self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()