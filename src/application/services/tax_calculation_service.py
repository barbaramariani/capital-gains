from domain.entities.portfolio import Portfolio
from domain.entities.stock_operation import StockOperation
from domain.entities.tax_result import TaxResult
from typing import List

class TaxCalculationService:
    def calculate_tax(self, stock_operation: StockOperation, portfolio: Portfolio) -> TaxResult:
        profit = portfolio.operation_profit(stock_operation)
        if profit > 0:
            deducted_profit = max(profit-portfolio.loss, 0)
            tax = round(0.2* deducted_profit, 2)
            portfolio.loss = max(portfolio.loss-profit, 0)
        else:
            tax = 0
            portfolio.loss -= profit
        
        if stock_operation.total_cost <= 20_000:
            return TaxResult(tax=0)
        return TaxResult(tax=tax)