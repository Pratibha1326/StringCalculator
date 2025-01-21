import pytest

from string_calculator import StringCalculator

# empty string should return 0
def test_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

# Test case for single number
def test_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1
# Test case for two numbers, should return some of 2 numbers.
def test_sum_two_number():
    calculator = StringCalculator()
    assert calculator.add("1, 2") == 3

