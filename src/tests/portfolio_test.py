import unittest
from unittest import TestCase

from domain.entities.portfolio import Portfolio
from domain.entities.stock_operation import StockOperation


class PortfolioTest(TestCase):
    def setUp(self):
        self.empty_portfolio = Portfolio(stock_operations=[])
        self.filled_portfolio = Portfolio(
            stock_operations=[
                StockOperation(operation="buy", quantity=10, unit_cost=20),
                StockOperation(operation="buy", quantity=10, unit_cost=10),
            ],
            total_stocks_quantity=20,
            current_weighted_average=15
        )

    def test_add_stock_operation_given_empty_portfolio_when_adding_stock_operation_then_portfolio_contains_operation(self):
        new_portfolio = self.empty_portfolio
        stock_operation = StockOperation(operation="buy", quantity=5, unit_cost=70)
        new_portfolio.add_stock_operation(stock_operation)

        self.assertEqual(len(new_portfolio.stock_operations), 1)
        self.assertEqual(new_portfolio.stock_operations[0].operation, "buy")

    def test_update_stocks_quantity_given_empty_portfolio_when_updating_stocks_quantity_then_total_quantity_updated(self):
        new_portfolio = self.empty_portfolio
        stock_operation_buy = StockOperation(operation="buy", quantity=8, unit_cost=60)
        stock_operation_sell = StockOperation(operation="sell", quantity=3, unit_cost=40)

        new_portfolio.add_stock_operation(stock_operation_sell)
        new_portfolio.add_stock_operation(stock_operation_buy)

        self.assertEqual(new_portfolio.total_stocks_quantity, 5)

    def test_operation_profit_given_filled_portfolio_when_calculating_operation_profit_then_correct_profit_calculated(self):
        new_portfolio = self.filled_portfolio
        stock_operation = StockOperation(operation="sell", quantity=8, unit_cost=60)

        profit = new_portfolio.operation_profit(stock_operation)

        self.assertEqual(profit, 45*8)

    def test_update_weighted_average_given_filled_portfolio_when_updating_weighted_average_then_correct_average_updated(self):
        new_portfolio = self.filled_portfolio
        stock_operation = StockOperation(operation="buy", quantity=20, unit_cost=25)

        new_portfolio.update_weighted_average(stock_operation)

        self.assertEqual(new_portfolio.current_weighted_average, 20)


if __name__ == '__main__':
    unittest.main()
