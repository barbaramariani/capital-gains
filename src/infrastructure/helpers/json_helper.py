from dataclasses import asdict
import json

def kebab_to_snake(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            new_key = key.replace("-", "_")
            new_dict[new_key] = kebab_to_snake(value)
        return new_dict
    elif isinstance(obj, list):
        return [kebab_to_snake(item) for item in obj]
    else:
        return obj

def transform_json_to_operations(json_data):
    return json.loads(json_data, object_hook=kebab_to_snake)

def format_tax_results(tax_results):
    return [{"tax": round(result.tax*100, 2)/100} for result in tax_results]

def transform_result_to_json(result):
    formatted_results = format_tax_results(result)
    return json.dumps(formatted_results)
