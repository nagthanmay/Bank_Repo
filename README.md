# Banking System Application

## Overview

This project implements a simplified version of a banking system application following the clean architecture principles. The system consists of three layers: Domain, Use Case, and Infrastructure.

- **Domain Layer:** Contains entities representing domain concepts such as Account, Transaction, and Customer.

- **Use Case Layer:** Contains the business logic of the application, including use cases like creating a new account, making a transaction, and generating account statements.

- **Infrastructure Layer:** Deals with the interaction between the application and the outside world, including repositories for data persistence.

## Project Structure

The project follows a clean architecture structure with the following directories:

- **Domain:** Contains entity classes such as Account and Customer.

- **Service (Use Case):** Contains use case classes like AccountService, TransactionService, and StatementService.

- **Infra:** Deals with infrastructure concerns, including the AccountRepository for data persistence.

- **Tests:** Contains test files for the implemented functionalities.

## How to Run

1. create a conda environment with python=3.9

2. Navigate to the project directory:

    ```bash
    cd banking_system
    ```

3. Run the application:

    ```bash
    python Service/account_service.py
    ```

4. Run tests:
 navigate to Bank root directory
    ```bash
    python -m unittest discover -s tests -p "test_*.py"
    ```

## Additional Notes

- **Generating Statement String:** The logic to generate a statement string is implemented in `StatementService`. It retrieves transaction details for a given account and formats them into a human-readable string.

- **Unique Identifiers:** The `generate_unique_id` function generates a unique identifier using the `uuid` module.

- **Account Number Generation:** The `generate_account_number` function generates a random account number using the `random` and `string` modules.

## Troubleshooting

- If you encounter import errors or issues running scripts, ensure that the virtual environment is activated, and the correct Python interpreter is used.

- Check the project structure and file naming conventions to match the provided README instructions.
