from random import randint
from string import digits
from py_expression_eval import Parser

legal = digits+'+-*/()'
parse = Parser().parse
calc = lambda e: parse(e).evaluate({})
correct = lambda e, c: calc(e) == c

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

def illegal(expr):
    if expr == "":
        return False
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
        except SyntaxError:
            print("Can't understand '{}'".format(cand_expr))
