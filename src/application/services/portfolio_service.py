from domain.entities.portfolio import Portfolio
from domain.entities.stock_operation import StockOperation
from domain.entities.tax_result import TaxResult
from application.services.tax_calculation_service import TaxCalculationService
from typing import List

class PortfolioService:
    def __init__(self, tax_calculation_service: TaxCalculationService):
        self.portfolio = Portfolio()
        self.tax_calculation_service = tax_calculation_service

    def process_stock_operations(self, stock_operations: List[StockOperation]) -> List[TaxResult]:
        tax_results = []

        for operation in stock_operations:
            tax_result = self.process_stock_operation(operation)
            tax_results.append(tax_result)

        return tax_results

    def process_stock_operation(self, stock_operation: StockOperation) -> TaxResult:
        if stock_operation.operation == "buy":
            self.portfolio.update_weighted_average(stock_operation)
            self.portfolio.add_stock_operation(stock_operation)
            return TaxResult(tax=0)

        if stock_operation.operation == "sell":
            self.portfolio.add_stock_operation(stock_operation)
            tax_result = self.tax_calculation_service.calculate_tax(stock_operation, self.portfolio)
            return tax_result

        raise ValueError("Invalid operation type")