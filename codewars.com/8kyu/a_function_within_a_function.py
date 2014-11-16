"""
a_function_within_a_function.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Tag: Fundamental
Problem:
    Given an input n, write a function always that returns a function which returns n.
    Ruby should return a lambda or a proc.
Example:
    three = always(3)
    three() /* returns 3 */
"""


def always(n=0):
    def do():
        return n
    return do