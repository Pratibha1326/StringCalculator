# StringCalculator KATA

This repository contains the solution for the String Calculator Kata using Test-Driven Development (TDD). The goal of the kata is to build a calculator that can handle a string of comma-separated numbers with the following features:

**Requirements**:
Empty String: The calculator should return 0 for an empty string.
Single Number: The calculator should return the number when given a string containing just a single number.
Multiple Numbers: The calculator must add multiple numbers (comma-separated).
Newline as a Delimiter: The calculator must accept newlines between numbers as delimiters.
Custom Delimiters: The calculator must support custom delimiters declared at the beginning of the input string.
Negative Numbers: The calculator throws an exception if a negative number occurs in the string, including all negative numbers.
Numbers Greater Than 1000: The calculator treats numbers larger than 1000 as ignored.
Multiple and Any-Length Delimiters: The calculator must work with multiple delimiters and delimiters of any length.

**Features Implemented:**
Handling of an Empty String: Returns 0 for an empty string.
Handling of a Number: Returns the same number provided the input is just a number.
Sum of Multiple Numbers: Performs addition on any number of numbers, whether it be a comma-separated number or a newline-separated list.
By default new lines are treated as delimiters.
Negative Number Handling: Displays an error message along with a list of negative numbers if one encounters any.
Ignore Numbers Greater Than 1000: Disregards numbers greater than 1000.
Accept Multiple and Long Delimiters: Accepts delimiters of any length: for example, //[***] as well as multiple delimiters: for example, //[*][%].


**Example usage:**
calculator = StringCalculator()

# Test Cases
print(calculator.add(""))  # Output: 0
print(calculator.add("1"))  # Output: 1
print(calculator.add("1,5"))  # Output: 6
print(calculator.add("1, 2, 3, 5, 8, 9"))  # Output: 28
print(calculator.add("1\n2,3"))  # Output: 6
print(calculator.add("//;\n1;2;3"))  # Output: 6
print(calculator.add("//[*][%]\n1*2%3"))  # Output: 6
print(calculator.add("//[***]\n1***2***3"))  # Output: 6
