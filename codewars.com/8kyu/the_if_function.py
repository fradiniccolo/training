"""
multiply.py

Language: python
Version: 2.7.5
OS: OS X
Author: Marcello Traversi
E-mail: me@marcellotraversi.com
Kyu: 8
Tag: Fundamental
Problem:
    Who likes keywords? Nobody likes keywords, so why use them?
    You know what keyword I use too much? if! We should make
    a function called _if, with its arguments as a logical test
    and two functions/lambdas where the first function is executed
    if the boolean is true, and the second if it's false,
    like an if/else statement, so that we don't have to mess around
    with those nasty keywords! Even so, It should support
    truthy/falsy types just like the keyword.
Example:
    def truthy(): print("True")
    def falsey(): print("False")
    _if(True, truthy, falsey)
    # Prints 'True' to the console.
"""


def _if(bool, truthy, falsey):
    if bool:
        return truthy()
    else:
        return falsey()