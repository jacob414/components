import pytest
from altered import state, E

from random import randint
from comps import game
from comps.game import challenge, correct, points, illegal

def test_challenges():
    for n in range(10000):
        chal = challenge(1, 100)
        assert chal >= 1 and chal <= 100

def test_correct():
    for n in range(100):
        a, b = randint(1, 100), randint(1, 100)
        assert correct('{} + {}'.format(a,b), a+b)

@pytest.mark.parametrize("expr,expected", (
    ("1+1", 1), ("1+1-2", 3), ("2*2", 4), ("10/2+1", 9),("10", 0)) )
def test_points(expr, expected):
    assert points(expr) == expected

@pytest.mark.parametrize("expr,legal", (
    ("", False), ("+", True), ("10", False)) )
def test_illegal(expr, legal):
    assert illegal(expr) == legal

def test_answer_integration_correct():
    with state(game, reply=lambda *a: '1+1'):
        assert game.answer(2) == 1
