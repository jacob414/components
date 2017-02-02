from random import randint
from string import digits

legal = digits+'+-*/()'

def challenge(min, max):
    answer = randint(min, max)
    return answer

def answer(num):
    s = input('{} >'.format(num))
    expr = ''.join(ch for ch in s if ch in legal)
    return expr
