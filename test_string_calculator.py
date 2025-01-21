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

#  Test case for multiple numbers
def test_sum_unknown_number():
    calculator = StringCalculator()
    assert calculator.add("1, 2, 3, 5, 8, 9") == 28
    
# Test case  for new line in between numbers.
def test_new_line_between_numbers():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6

# Test case for different delimiters
def test_sum_with_custom_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2;3") == 6

# Test case for negetive numbers
def test_sum_with_negetive_numbers():
    calculator = StringCalculator()
    try:
    # with pytest.raises(ValueError) as excinfo:
        calculator.add("1,-2,-3")
    except ValueError as e:
        assert str(e) == "negative numbers not allowed -2,-3"

#Test case to ignore large numbers like above 1000
def test_ignore_large_numbers():
    calculator = StringCalculator()
    assert calculator.add("2, 1001") == 2

# Test case for anylength of delimiter
def test_anylength_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//[***]\n1***2***3") == 6