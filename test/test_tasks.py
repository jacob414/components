import pytest

from random import randint
from comps.tasks import challenge, correct, points

def test_challenges():
    for n in range(10000):
        chal = challenge(1, 100)
        assert chal >= 1 and chal <= 100

def test_correct():
    for n in range(100):
        a, b = randint(1, 100), randint(1, 100)
        assert correct('{} + {}'.format(a,b), a+b)


@pytest.mark.parametrize("expr,expected", (
    ("1+1", 1), ("1+1-2", 3), ("2*2", 3), ("10/2+1", 9)) )
def test_points(expr, expected):
    assert points(expr) == expected
