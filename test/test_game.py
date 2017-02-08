import time
import os

import pytest
from altered import state, E
from mock import MagicMock

from random import randint
from comps import game
from comps.game import challenge, correct, points, illegal

def test_challenges():
    "Challenge function should simply return an integer in a specified span"
    for n in range(10000):
        chal = challenge(1, 100)
        assert chal >= 1 and chal <= 100

def test_correct():
    "correct() should return a `bool` describing correctness of expression"
    for n in range(100):
        a, b = randint(1, 100), randint(1, 100)
        assert correct('{} + {}'.format(a,b), a+b)
        assert not correct('{} - {}'.format(a,b), a+b)

@pytest.mark.parametrize("expr,expected", (
    ("1+1", 1), ("1+1-2", 3), ("2*2", 4), ("10/2+1", 9),("10", 0)) )
def test_points(expr, expected):
    "Checks points given by certain known fixtures"
    assert points(expr) == expected

@pytest.mark.parametrize("expr,legal", (
    ("", True), (os.linesep, True), ("+", True), ("10", False)) )
def test_illegal(expr, legal):
    "illegal() guards against certain known problematic illegal expressions"
    assert illegal(expr) == legal

def test_answer_integration_correct():
    "answer() should calculate points when given a correct expression"
    with state(game, reply=lambda *a: '1+1'):
        assert game.answer(2) == 1

def test_answer_integration_incorrect_retry_correct():
    "answer() should allow re-try of incorrect expressions after 2 seconds"
    correct = lambda challenge: '1+1'
    def incorrect(challenge):
        game.reply = correct
        return '1+2'

    mock_sleep = MagicMock()
    with state(game, reply=incorrect), state(time, sleep=mock_sleep):
        game.answer(2)
        assert mock_sleep.call_args[0] == (2,) # slept 2s, then retry
        points = game.answer(2)
        assert points == 1 # now correct
