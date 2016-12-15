def fibonacci(n):
    """
    It is
    :param n:
    :return:
    """
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

# print(fibonacci(100))
# print(fibonacci(200))
#1 1 2 3 5 8 13 21 34 55 55