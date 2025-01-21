import pytest

from string_calculator import StringCalculator

# empty string should return 0
def test_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0
