from typing import Optional
from infrastructure.dependency_injector import calculate_tax_use_case

from infrastructure.helpers.json_helper import transform_json_to_operations, transform_result_to_json


def process_input_line(line: str) -> Optional[str]:
    if line.strip() == "":
        return None
    
    operations = transform_json_to_operations(line)
    result = calculate_tax_use_case(operations)
    return transform_result_to_json(result)