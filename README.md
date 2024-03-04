## Description

This command-line interface (CLI) program calculates taxes on stock market operations.

### Technical and Architectural Decisions
As requested, I used a command-line interface (CLI). The program is written in Python and follows a modular and object-oriented design. I followed the principles of Domain Driven Design (DDD) to structure the codebase.

Domain Entities:

- StockOperation: Represents a stock market operation, such as buying or selling stocks. It encapsulates the operation type, unit cost, and quantity.

- Portfolio: Represents a collection of stock market operations and handles the logic and data for managing and calculating taxes.

- TaxResult: Represents the tax result of a stock market operation. It contains the calculated tax amount.

UseCase:
- The primary use case of this application is to calculate taxes on stock market operations. The `CalculateTaxUseCase` class encapsulates the core functionality, bringing together various components of the system to achieve this goal.
  
Services:
- TaxCalculationService: This service is responsible for calculating the tax for a given stock operation. It takes a StockOperation and a Portfolio as input and returns a TaxResult. The `calculate_tax` method in this service does the tax calculation based on the profit and loss of the portfolio.

- PortfolioService: This service is responsible for processing a list of stock operations and returning a list of tax results. The `process_stock_operations` method iterates over the list of stock operations, calls the `process_stock_operation` method for each operation and returns the tax_results.


#### Frameworks and Libraries

In this solution, I used the following frameworks and libraries:

- Docker: I chose to use Docker to containerize the application. Docker provides a simple and portable environment, ensuring that the program can run consistently across different machines and operating systems.

- unittest: I'm using unittest framework to write unit and integration tests for my application. unittest is a built-in simple and effective testing framework in Python. I'm using pytest to run the tests.

## How to Use

### Prerequisites

Make sure you have Docker installed on your machine.

### Build and Run With Docker

1. Download or copy the project files to your local machine.

2. Open a terminal and navigate to the project directory.

3. Build the Docker image:

    ```bash
    docker build -t ganho-de-capital .
    ```

4. Run the program:

    ```bash
    docker run -it ganho-de-capital
    ```

    The program will wait for input. Provide the stock market operations in JSON format, one per line. Press Enter on an empty line to finish.

    Alternatively, use an `input.txt` file:

    ```bash
    docker run -it ganho-de-capital <input.txt
    ```

### Run Without Docker
1. Ensure Python is Installed.
2. Install Dependencies

```bash
pip install -r requirements.txt
```
1. From `src` directory, run the code with the input file:

```bash
python main.py <input.txt
```

### Example Input

```json
[{"operation":"buy", "unit-cost":10.00, "quantity": 10000}, {"operation":"sell", "unit-cost":20.00, "quantity": 5000}]
[{"operation":"buy", "unit-cost":20.00, "quantity": 10000}, {"operation":"sell","unit-cost":10.00, "quantity": 5000}]
```

### Example Output

```json
[{"tax": 0.0}, {"tax": 10000.0}]
[{"tax": 0.0}, {"tax": 0.0}]
```

## Run Tests
To run the tests, you can use the following command:
```bash
python -m pytest
```