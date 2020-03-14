from math import gcd


def recursive_find_threes(n, mod_by):
    if not n:
        return 3
    return pow(3, recursive_find_threes(n - 1, mod_by), mod_by)


def iscoprime(a, b):
    return gcd(a, b) == 1


def eulerstotient(q):
    output = 0
    for i in range(1, q):
        output += iscoprime(q, i)
    return output
