from comps.game import challenge, reply, calc, correct, points, answer
from time import time

start = time()
total = 0
remaining = 10
while remaining:
    total += answer(challenge(5, 55))
    remaining -= 1
end = time()
print('Total {}, took {} seconds'.format(total, round(end-start)))
