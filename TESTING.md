# Testing Strategy

## What was tested

The core calculator logic was tested using unit tests. Each arithmetic operation (addition, subtraction, multiplication, division) was verified individually.

Edge cases were also tested, including:
- division by zero
- negative numbers
- decimal numbers
- large numbers

Integration tests were used to ensure that different components of the application interact correctly.

## What was not tested

The command-line interface formatting and user input validation were not deeply tested because the main focus of the project is the calculation logic and testing strategy.

## Testing Pyramid

The test suite follows the testing pyramid model:

- Unit tests form the base and represent the majority of the tests.
- Integration tests are fewer and validate interactions between components.
- No UI tests were implemented since the application interface is minimal.

## Black-box vs White-box Testing

Unit tests mainly use white-box testing because they test the internal logic of the calculator functions.

Integration tests follow a more black-box approach, focusing on the behavior of the system as a whole without considering the internal implementation.

## Functional vs Non-Functional Testing

This project focuses on functional testing. Each test verifies that the calculator performs the correct arithmetic operations.

Non-functional testing such as performance, security, or usability was not included because the project scope is limited.

## Regression Testing

The test suite can serve as a regression testing tool. If new features are added or the code is modified, running the test suite ensures that existing functionality continues to work correctly.

## Test Results Summary

| Test Name | Type | Result |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_full_operation_sequence | Integration | Pass |
| test_clear_function | Integration | Pass |