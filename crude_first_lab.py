from comps.tasks import challenge, answer

num = challenge(5, 55)
answering = True
while answering:
    try:
        cand_expr = answer(num)
        cand = eval(cand_expr)
        print('{} = {}'.format(cand_expr, cand))
        if cand == num:
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
