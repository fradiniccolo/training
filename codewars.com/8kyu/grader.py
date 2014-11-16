"""
grader.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Problem:
    Create a function that takes a number as an argument and returns a grade based on that number.
    Anything greater than 1 or less than 0.6 should return "F"
    0.9 or greater should return the grade "A"
    0.8 or greater should return the grade "B"
    0.7 or greater should return the grade "C"
    0.6 or greater should return the grade "D"
Example:
    grader(0.9) == "A"
    grader(0.3) == "F"
    grader(234) == "F"
    grader(0.75) == "C"
"""


def grader(score):
    if score >= 0.9 and score <= 1:
        return "A"
    elif score >= 0.8 and score < 0.9:
        return "B"
    elif score >= 0.7 and score < 0.8:
        return "C"
    elif score >= 0.6 and score < 0.7:
        return "D"
    else:
        return "F"