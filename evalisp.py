#!/usr/bin/env python3

'''
Eva Lisp is an evaluator for simple and limited Lisp expressions.
'''

from cin import cinput

class ExpressionSyntaxError(Exception):
    '''Exception raised when the user types wrong expressions.'''

    def __init__(self, err=''):
        Exception.__init__(self, err)

def expression():
    '''Evalute a Lisp expression.'''

    cinput.skip_whitespace()
    char = cinput.getc()
    if char.isdigit() or char in {'-', '+'}:
        cinput.ungetc(char)
        num = cinput.getfloat()
        return num
    elif char == '(':
        cinput.skip_whitespace()
        operator = cinput.getc()
        exp1 = expression()
        exp2 = expression()
        cinput.skip_whitespace()
        close = cinput.getc()
        if close != ')':
            raise ExpressionSyntaxError('Missing ).')
        return calc(operator, exp1, exp2)
    else:
        raise ExpressionSyntaxError('Unknown start of token, ' + char)

def calc(operator, exp1, exp2):
    '''Apply operator on exp1 and exp2.'''

    if operator == '+':
        return exp1 + exp2
    elif operator == '-':
        return exp2 - exp2
    elif operator == '*':
        return exp1 * exp2
    elif operator == '/':
        # let Python handle division by zero
        return exp1 / exp2
    else:
        raise ExpressionSyntaxError('Unknow operator, ' + operator)

if __name__ == '__main__':
    print("Hello! My name is Eva Lisp. Call me Eva.")
    print("I can help you evaluate simple Lisp expressions.")

    while True:
        try:
            print("> ", end='')
            print(expression())
        except (EOFError, KeyboardInterrupt):
            print("Bye!")
            break
