from comps.tasks import challenge

def test_challenges():
    for n in range(10000):
        chal = challenge(1, 100)
        assert chal >= 1 and chal <= 100
