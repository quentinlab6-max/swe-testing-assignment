# Quick-Calc

Quick-Calc is a simple calculator application that performs basic arithmetic operations including addition, subtraction, multiplication, and division. It also includes a clear function to reset the calculator state.

## Setup Instructions

1. Clone the repository

git clone https://github.com/username/swe-testing-assignment

2. Install dependencies

pip install -r requirements.txt

## Run the application

python main.py

## Run tests

pytest

## Testing Framework Research

### Pytest vs Unittest

Pytest and Unittest are two widely used testing frameworks in Python.

Unittest is part of Python’s standard library and follows a class-based structure similar to Java’s JUnit. It is very stable and widely used in enterprise projects. However, it often requires more boilerplate code to write simple tests.

Pytest is a more modern testing framework that focuses on simplicity and readability. Tests can be written as simple functions, and powerful features such as fixtures, parameterization, and detailed failure reports make it easier to write and maintain test suites.

In this project, Pytest was chosen because it allows faster development of tests, requires less boilerplate code, and provides clearer output when tests fail.