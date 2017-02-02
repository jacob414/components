from comps.game import challenge, reply, calc, correct, points, answer

total = 0
remaining = 10
while remaining:
    total += answer(challenge(5, 55))
    remaining -= 1
print('Total {}'.format(total))
