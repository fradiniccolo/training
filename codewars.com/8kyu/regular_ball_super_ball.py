"""
regular_ball_super_ball.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Tag: Fundamental
Problem:
    Create a class Ball.
    Ball objects should accept one argument for "ball type" when instantiated.
    If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
Example:
    ball1 = Ball()
    ball2 = Ball("super")
    ball1.ball_type  #=> "regular"
    ball2.ball_type  #=> "super"
"""


class Ball(object):
    def __init__(self, ball_type=None):
        if ball_type:
            self.ball_type = 'super'
        else:
            self.ball_type = 'regular'