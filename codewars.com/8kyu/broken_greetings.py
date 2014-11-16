"""
broken_greetings.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Tag: Fundamentals
Problem:
    Correct this code, so that the greet function returns the expected value.
Example:
"""


class Person:
    def __init__(self, name):
        self.name = name
  
    def greet(self, other_name):
        return "Hi {0}, my name is {1}".format(other_name, self.name)