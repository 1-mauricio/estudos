# S = 2/500 - 5/490 + 2/480 - 5/470
def serie_2(n, num_1 = 2, num_2 = 5, den = 500, sin = 1):
    if n <= 1:
        if sin > 0:
            res = sin * num_1 / den
        else:
            res = sin * num_2 / den
    else:
        if sin > 0:
            res = sin * num_1 / den + serie_2(n - 1, num_1, num_2, den - 10, sin * -1)
        else:
            res = sin * num_1 / den + serie_2(n - 1, num_1, num_2, den - 10, sin * 1)
    return res

def serie_1(n, num = 2, den = 500, sin = 1):
    if n <= 1:
        res = sin * num / den
    else:
        res = num / den + serie_2(n - 1, num - 7 * sin, den - 10, sin * -1)
    return res