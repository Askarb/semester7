import cmath
n, px, py = map(int, input().split(' '))

x, y = map(int, input().split(' '))
d = cmath.sqrt(x * x + y * y)
mi = d
ma = d
prev = cmath.sqrt(x*x+y*y)
prevX = x
prevY = y
for i in range(1, n):
    x, y = map(int, input().split(' '))
    d = cmath.sqrt(x*x + y*y)
    if d > ma:
        ma = d
    if d < mi:
        mi = d

    cur = cmath.sqrt(x * x + y * y)
    h = prev*cur/ (cmath.sqrt(pow(prevX-x, 2) + pow(prevY-y, 2)))

minR = cmath.sqrt(pow(px-x, 2) + pow(py-y, 2))
print(minR)

