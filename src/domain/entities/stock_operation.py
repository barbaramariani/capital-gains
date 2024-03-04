from dataclasses import dataclass

@dataclass
class StockOperation:
    operation: str
    unit_cost: float
    quantity: int
    
    @property
    def total_cost(self):
        return self.unit_cost * self.quantity