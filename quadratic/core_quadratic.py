from math import sqrt


def solve_quadratic(a, b, c):
    res = {
        'status': 0
    }
    d = b*b - 4*a*c
    if d == 0:
        x = -b / 2 * a
        res['x'] = check_int(x)
        res['status'] = 1
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        res['x1'] = check_int(x1)
        res['x2'] = check_int(x2)
        res['status'] = 2
    return res


def check_int(x):
    if x == int(x):
        return int(x)
    else:
        return x

print(solve_quadratic(1.0, -4.0, 4.0))

# a  b   c   x1   x2
# 5  6   1 -0.2   -1
# 5  2   1    0
# 1 -7   0    0  0.7
# 1  2  -8   -4    2
# 1 -4   4    2


