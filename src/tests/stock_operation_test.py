import unittest
from unittest import TestCase

from domain.entities.portfolio import Portfolio
from domain.entities.stock_operation import StockOperation


class TestStockOperation(unittest.TestCase):
    def test_total_cost_calculation_given_stock_operation_then_correct_total_cost_calculated(self):
        operation = StockOperation(operation="buy", unit_cost=10.0, quantity=5)
        
        total_cost = operation.total_cost
        
        self.assertEqual(total_cost, 50.0)


if __name__ == '__main__':
    unittest.main()
