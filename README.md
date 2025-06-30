# Number Wise Flask Backend

A Flask-based backend application designed to handle advanced number-related operations and mathematical computations through a clean RESTful API.

![Technologies Used](https://img.shields.io/badge/Technologies-Flask%20%7C%20Python%20%7C%20Pytest%20%7C%20REST-blue)

## 🚀 Features

- **RESTful API Architecture** - Clean, intuitive endpoints for all number operations
- **20+ Mathematical Algorithms** - Comprehensive collection of number theory implementations
- **Production Ready** - Built with Flask for scalability and easy deployment
- **Thoroughly Tested** - Complete test coverage using pytest
- **Lightweight & Fast** - Minimal dependencies for quick deployment and high performance

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Flask** | Lightweight WSGI web framework |
| **Python** | Core programming language |
| **Pytest** | Testing framework for unit tests |
| **REST** | API architectural pattern |

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/zakaria-zoulati/Number_Wise_Flask_BackEnd.git
   cd Number_Wise_Flask_BackEnd
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:8000`

## 🧮 Supported Algorithms

### Prime & Composite Numbers
- **Prime Number Check** - Efficient primality testing using square root optimization
- **Sphenic Number Check** - Numbers that are products of exactly three distinct primes
- **Deficient Number Check** - Numbers where sum of proper divisors is less than the number

### Perfect & Special Numbers
- **Perfect Number Check** - Numbers equal to sum of their proper divisors
- **Automorphic Number Check** - Numbers whose square ends with the number itself
- **Harshad Number Check** - Numbers divisible by the sum of their digits

### Sequence-Based Numbers
- **Fibonacci Check** - Validates membership in the Fibonacci sequence
- **Lucas Number Check** - Checks Lucas sequence membership (starts with 2, 1)
- **Catalan Number Check** - Combinatorial sequence validation
- **Fermat Number Check** - Numbers of the form 2^(2^n) + 1
- **Cullen Number Check** - Numbers of the form n × 2^n + 1

### Geometric Numbers
- **Triangular Number Check** - Numbers representing triangular dot patterns
- **Pentagonal Number Check** - Five-sided geometric number patterns
- **Octagonal Number Check** - Eight-sided geometric sequences
- **Pentatope Number Check** - Four-dimensional triangular pyramids
- **Icosahedral Number Check** - Three-dimensional icosahedron structures

### Arithmetic Properties
- **Palindrome Check** - Numbers that read the same forwards and backwards
- **Pronic Number Check** - Products of two consecutive integers
- **Polite Number Check** - Expressible as sum of consecutive positive integers
- **Even Number Check** - Basic divisibility by 2



## 📁 Project Structure

```
Number_Wise_Flask_BackEnd/
├── app.py                 # Main Flask application
├── PythonAlgos.py            # Number theory implementations
├── unitTests.py                # Test files
├── requirements.txt      # Dependencies
├── utilities.py      # Helper functions, common operations
└── README.md            # This documentation


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Commit your changes (`git commit -am 'Add new algorithm'`)
4. Push to the branch (`git push origin feature/new-algorithm`)
5. Create a Pull Request

