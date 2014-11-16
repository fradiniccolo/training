"""
color_ghost.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Tag: Fundamentals
Problem:
    Create a class Ghost
    Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of
    "white" or "yellow" or "purple" or "red" when instantiated
Example:
    ghost = Ghost()
    ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""
import random


class Ghost(object):
    def __init__(self):
        seq = ('white', 'yellow', 'purple', 'red')
        self.color = random.choice(seq)