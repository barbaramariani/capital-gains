import sys
import traceback
from infrastructure.helpers.input_helper import process_input_line


for line in sys.stdin:
    try:
        output = process_input_line(line)
        if output:
            print(output)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        sys.exit(1)