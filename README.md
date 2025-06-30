# Number Wise Flask Backend

This project is a Flask-based backend application designed to handle number-related operations. It provides a set of APIs to perform various mathematical and logical operations.

![Technologies Used](https://img.shields.io/badge/Technologies-Flask%20%7C%20Python%20%7C%20Pytest%20%7C%20REST-blue)

## Technologies Used

The project leverages the following technologies:

- **Flask**: A lightweight WSGI web application framework for Python.
- **Python**: The core programming language used for development.
- **Pytest**: A testing framework for writing and running unit tests.
- **REST**: Architectural style for designing networked applications.

---

## Features

- **RESTful API**: Easy-to-use endpoints for number operations.
- **Scalable**: Built with Flask, allowing for easy scaling and integration.
- **Lightweight**: Minimal dependencies for quick deployment.
- **Tested**: Includes unit tests using `pytest` for robust functionality.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Number_Wise_Flask_BackEnd.git
    cd Number_Wise_Flask_BackEnd
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Algorithms Used

### 1. Prime Number Check
   - Determines if a number is prime using trial division.
   - Optimized to check divisors up to the square root of the number.

### 2. Factorial Calculation
   - Computes the factorial of a number using iterative or recursive methods.

### 3. Even/Odd Check
   - Simple modulus operation to determine if a number is even or odd.

### 4. Sum of Numbers
   - Aggregates a list of numbers using Python's built-in `sum()` function.

## API Endpoints

### 1. **GET /api/number-info**
    - **Description**: Fetches information about a given number.
    - **Query Parameters**:
      - `number` (required): The number to analyze.
    - **Response**:
      ```json
      {
         "number": 5,
         "is_prime": true,
         "is_even": false,
         "factorial": 120
      }
      ```

### 2. **POST /api/operations**
    - **Description**: Performs operations on a list of numbers.
    - **Request Body**:
      ```json
      {
         "numbers": [1, 2, 3, 4],
         "operation": "sum"
      }
      ```
    - **Response**:
      ```json
      {
         "result": 10
      }
      ```

## Project Structure

```
Number_Wise_Flask_BackEnd/
│
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── static/              # Static files (if any)
├── templates/           # HTML templates (if any)
└── tests/               # Unit tests using pytest
```

## Testing

Run the tests using `pytest`:
```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, feel free to reach out at [your-email@example.com].