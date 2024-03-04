import unittest
from unittest.mock import Mock
from src.application.services.portfolio_service import PortfolioService
from src.domain.entities.stock_operation import StockOperation
from src.domain.entities.tax_result import TaxResult

class PortfolioServiceTest(unittest.TestCase):
    def test_process_stock_operations_given_stock_operations_then_tax_results_calculated(self):
        tax_calculation_service = Mock()
        sell_tax_calculation_result = TaxResult(tax=1.00)
        tax_calculation_service.calculate_tax.side_effect = [sell_tax_calculation_result]
        portfolio_service = PortfolioService(tax_calculation_service)
        stock_operations = [
            StockOperation(operation="buy", quantity=5, unit_cost=100),
            StockOperation(operation="sell", quantity=3, unit_cost=120)
        ]

        tax_results = portfolio_service.process_stock_operations(stock_operations)

        self.assertIsInstance(tax_results, list)
        self.assertEqual(len(tax_results), 2)
        self.assertEqual(tax_results[0].tax, 0)
        self.assertEqual(tax_results[1].tax, 1)

    def test_process_stock_operation_given_stock_operation_sell_then_calls_calculate_tax(self):
            tax_calculation_service = Mock()
            tax_result = TaxResult(tax=0.15)
            tax_calculation_service.calculate_tax.return_value = tax_result
            portfolio_service = PortfolioService(tax_calculation_service)
            stock_operation = StockOperation(operation="sell", quantity=3, unit_cost=120)

            tax_result = portfolio_service.process_stock_operation(stock_operation)

            tax_calculation_service.calculate_tax.assert_called_once()

    def test_process_stock_operation_given_stock_operation_buy_then_tax_is_0_and_no_calls_to_calculate_tax(self):
        tax_calculation_service = Mock()
        portfolio_service = PortfolioService(tax_calculation_service)
        stock_operation = StockOperation(operation="buy", quantity=5, unit_cost=100)

        tax_result = portfolio_service.process_stock_operation(stock_operation)

        self.assertEqual(tax_result.tax, 0) 
        tax_calculation_service.calculate_tax.assert_not_called()


if __name__ == '__main__':
    unittest.main()