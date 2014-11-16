"""
grader.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 7
Tag: Fundamental
Problem:
    Write a function named sumDigits which takes a number as input
    and returns the sum of the absolute value of each of
    the number's decimal digits.
    Let's assume that all numbers in the input will be integer values.
Example:
    sumDigits(10)  # Returns 1
    sumDigits(99)  # Returns 18
    sumDigits(-32) # Returns 5
"""


def sumDigits(number):
    number = abs(int(number))
    digits = [int(x) for x in str(number)]
    total = sum(digits)

    return total