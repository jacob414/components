from comps.tasks import challenge, reply, answer, correct

num = challenge(5, 55)
answering = True
while answering:
    try:
        cand_expr = reply(num)
        cand = answer(cand_expr)
        print('{} = {}'.format(cand_expr, cand))
        if correct(cand_expr, num):
            addp = cand_expr.count('+') * 1
            subp = cand_expr.count('-') * 2
            mulp = cand_expr.count('*') * 4
            divp = cand_expr.count('/') * 8
            print('Correct, {} points'.format(addp+subp+mulp+divp))
        else:
            print('Incorrect, 0 pts')
        answering = False
    except SyntaxError:
        print("Can't understand '{}'".format(cand_expr))
        answering = True
