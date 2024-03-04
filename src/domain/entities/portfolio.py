from dataclasses import dataclass, field
from typing import List
from domain.entities.stock_operation import StockOperation

@dataclass
class Portfolio:
    stock_operations: List[StockOperation] = field(default_factory=list)
    current_weighted_average: float = 0
    loss: float = 0
    total_stocks_quantity: int = 0
    
    def operation_profit(self, stock_operation: StockOperation) -> float:
        return stock_operation.total_cost - (self.current_weighted_average * stock_operation.quantity)

    def update_weighted_average(self, stock_operation: StockOperation) -> None:
        self.current_weighted_average = self.__calculate_weighted_average(stock_operation)
    
    def add_stock_operation(self, stock_operation) -> None:
        self.stock_operations.append(stock_operation)
        self.__update_stocks_quantity(stock_operation)

    def __update_stocks_quantity(self, stock_operation: StockOperation) -> None:
        if stock_operation.operation == "sell":
            self.total_stocks_quantity -= stock_operation.quantity
        elif stock_operation.operation == "buy":
            self.total_stocks_quantity += stock_operation.quantity
    
    def __calculate_weighted_average(self, stock_operation: StockOperation) -> float:
        if stock_operation.quantity == 0:
            return 0
        if self.total_stocks_quantity == 0:
            return stock_operation.unit_cost

        return round(((self.total_stocks_quantity * self.current_weighted_average) + (stock_operation.quantity * stock_operation.unit_cost)) / (self.total_stocks_quantity + stock_operation.quantity), 2)