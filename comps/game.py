import os
from random import randint
import time
from string import digits
from py_expression_eval import Parser

legal = digits+'+-*/()q'
parse = Parser().parse
calc = lambda e: parse(e).evaluate({})
correct = lambda e, c: calc(e) == c

def challenge(min, max):
    answer = randint(min, max)
    return answer

expr_filter = lambda inp: ''.join(ch for ch in inp if ch in legal)

reply = lambda num: input('{} >'.format(num))

def points(expr):
    n = lambda op: expr.count(op)
    return n('+') + n('-')*2 + n('*')*4 + n('/')*8

def illegal(expr):
    if expr in ("", os.linesep):
        return True
    try:
        calc(expr)
        return False
    except:
        return True

def answer(challenge):
    while True:
        try:
            cand_expr = reply(challenge)
            if illegal(cand_expr):
                raise SyntaxError()
            cand = calc(cand_expr)
            print('{} = {}'.format(cand_expr, cand))
            if correct(cand_expr, challenge):
                print('Correct, {} points'.format(points(cand_expr)))
                return points(cand_expr)
            else:
                print('Incorrect, 0 pts')
                time.sleep(2)
                continue
        except SyntaxError:
            print("Can't understand '{}'".format(cand_expr))
