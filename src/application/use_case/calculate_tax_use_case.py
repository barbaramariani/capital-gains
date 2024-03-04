from domain.entities.stock_operation import StockOperation
from domain.entities.tax_result import TaxResult
from domain.entities.portfolio import Portfolio
from application.services.tax_calculation_service import TaxCalculationService
from application.services.portfolio_service import PortfolioService
from typing import Dict, List

class CalculateTaxUseCase:
    def __init__(self, tax_calculation_service: TaxCalculationService, portfolio_service: PortfolioService):
        self.tax_calculation_service = tax_calculation_service
        self.portfolio_service = portfolio_service

    def __call__(self, stock_operations_list: List[Dict]) -> List[TaxResult]:
        self.portfolio_service.portfolio = Portfolio()

        stock_operations = [StockOperation(**operation) for operation in stock_operations_list]

        tax_results = self.portfolio_service.process_stock_operations(stock_operations)

        return tax_results