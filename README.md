# 🔢 Number Wise Flask Backend

> A powerful Flask-based backend application designed to handle advanced number-related operations and mathematical computations through a clean RESTful API.

[![Technologies](https://img.shields.io/badge/Technologies-Flask%20%7C%20Python%20%7C%20Pytest%20%7C%20REST-blue)](https://github.com/zakaria-zoulati/Number_Wise_Flask_BackEnd)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://python.org)

---

## ✨ Features

🎯 **RESTful API Architecture** - Clean, intuitive endpoints for all number operations  
🧮 **20+ Mathematical Algorithms** - Comprehensive collection of number theory implementations  
🚀 **Production Ready** - Built with Flask for scalability and easy deployment  
🧪 **Thoroughly Tested** - Complete test coverage using pytest  
⚡ **Lightweight & Fast** - Minimal dependencies for quick deployment and high performance

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose | Version |
|:----------:|---------|:-------:|
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | Lightweight WSGI web framework | Latest |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language | 3.7+ |
| ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) | Testing framework for unit tests | Latest |
| ![REST](https://img.shields.io/badge/REST-FF6B35?style=flat&logo=rest&logoColor=white) | API architectural pattern | - |

</div>

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:
- 🐍 Python 3.7 or higher
- 📦 pip package manager

### Installation

<details>
<summary><b>📋 Step-by-step setup</b></summary>

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/zakaria-zoulati/Number_Wise_Flask_BackEnd.git
cd Number_Wise_Flask_BackEnd
```

#### 2️⃣ Create virtual environment
```bash
python -m venv venv

# Activate virtual environment
# 🐧 Linux/macOS:
source venv/bin/activate

# 🪟 Windows:
venv\Scripts\activate
```

#### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Launch the application
```bash
python app.py
```

</details>

🌐 **Access the API at:** `http://localhost:8000`

---

## 🧮 Mathematical Algorithms

Our comprehensive collection of number theory algorithms, organized by category:

###  Prime & Composite Numbers
<details>
<summary>View algorithms</summary>

-  Prime Number Check - Efficient primality testing using square root optimization
-  Sphenic Number Check - Numbers that are products of exactly three distinct primes  
-  Deficient Number Check - Numbers where sum of proper divisors is less than the number

</details>

###  Perfect & Special Numbers
<details>
<summary>View algorithms</summary>

-  Perfect Number Check - Numbers equal to sum of their proper divisors
-  Automorphic Number Check - Numbers whose square ends with the number itself
-  Harshad Number Check - Numbers divisible by the sum of their digits

</details>

###  Sequence-Based Number
<details>
<summary>View algorithms</summary>

-  Fibonacci Check - Validates membership in the Fibonacci sequence
-  Lucas Number Check - Checks Lucas sequence membership (starts with 2, 1)
-  Catalan Number Check - Combinatorial sequence validation
-  Fermat Number Check - Numbers of the form 2^(2^n) + 1
-  Cullen Number Check - Numbers of the form n × 2^n + 1

</details>

###  Geometric Numbers
<details>
<summary>View algorithms</summary>

-  Triangular Number Check - Numbers representing triangular dot patterns
-  Pentagonal Number Check - Five-sided geometric number patterns
-  Octagonal Number Check - Eight-sided geometric sequences
-  Pentatope Number Check - Four-dimensional triangular pyramids
-  Icosahedral Number Check - Three-dimensional icosahedron structures

</details>

###  Arithmetic Properties
<details>
<summary>View algorithms</summary>

-  Palindrome Check - Numbers that read the same forwards and backwards
-  Pronic Number Check - Products of two consecutive integers
-  Polite Number Check - Expressible as sum of consecutive positive integers
-  Even Number Check  - Basic divisibility by 2

</details>

---

## 📁 Project Architecture

```
 Number_Wise_Flask_BackEnd/
├──  app.py                 # Main Flask application
├──  PythonAlgos.py         # Number theory implementations
├──  unitTests.py           # Comprehensive test suite
├──  requirements.txt       # Project dependencies
├──  utilities.py           # Helper functions & common operations  
└──  README.md              # Project documentation
```