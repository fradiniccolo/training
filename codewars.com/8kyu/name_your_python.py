"""
name_your_python.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Problem:
    For those of us who are not very familiar with Python,
    let's handle the very basic challenge of creating a class named Python.
    We want to give our Pythons a name, so it should take a name argument that we can retrieve later.
Example:
    bubba = Python('Bubba')
    bubba.name # should return 'Bubba'
"""


class Python:
    def __init__(self, name):
        self.name = name