def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def cons(a, b):
    return lambda f: f(a, b)


def car(x):
    return x(lambda a, b: a)


def cdr(x):
    return x(lambda a, b: b)
