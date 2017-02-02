from random import randint
from string import digits
from py_expression_eval import Parser

legal = digits+'+-*/()'
parse = Parser().parse
answer = lambda e: parse(e).evaluate({})
correct = lambda e, c: answer(e) == c

def challenge(min, max):
    answer = randint(min, max)
    return answer

def reply(num):
    s = input('{} >'.format(num))
    expr = ''.join(ch for ch in s if ch in legal)
    return expr

def points(expr):
    n = lambda op: expr.count(op)
    return n('+') + n('-')*2 + n('*')*4 + n('/')*8
