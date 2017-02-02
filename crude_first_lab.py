from comps.game import challenge, reply, calc, correct, points

num = challenge(5, 55)
answering = True
while answering:
    try:
        cand_expr = reply(num)
        cand = calc(cand_expr)
        print('{} = {}'.format(cand_expr, cand))
        if correct(cand_expr, num):
            print('Correct, {} points'.format(points(cand_expr)))
        else:
            print('Incorrect, 0 pts')
        answering = False
    except SyntaxError:
        print("Can't understand '{}'".format(cand_expr))
        answering = True
