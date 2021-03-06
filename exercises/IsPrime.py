#!/usr/bin/env python3

# ----------
# IsPrime.py
# ----------

from math     import sqrt
from unittest import main, TestCase

def is_prime (n) :
    assert n > 0                            # if n == 2, return True, 2 is prime
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :       # range(a, b) goes from a to b-1, should be range(3, int(sqrt(n) + 1), 2), fixed off-by-one error and added step size
        if (n % i) == 0 :
            return False
    return True

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime(1))

    def test_2 (self) :
        self.assertFalse(is_prime(2))       # broken, 2 is prime

    def test_3 (self) :
        self.assertTrue(is_prime(3))

    def test_4 (self) :
        self.assertFalse(is_prime(4))

    def test_5 (self) :
        self.assertTrue(is_prime(5))

    def test_6 (self) :
        self.assertTrue(is_prime(7))

    def test_7 (self) :
        self.assertTrue(is_prime(9))        # broken, 9 is not prime, sqrt(9) is 3, range(3, 3) never runs

    def test_8 (self) :
        self.assertFalse(is_prime(27))

    def test_9 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
coverage3 run --branch IsPrime.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK



coverage3 report -m
Name      Stmts   Miss Branch BrMiss  Cover   Missing
-----------------------------------------------------
IsPrime      31      0      6      0   100%
"""




"""
Process:
We have a bunch of tests that are broken, fix the tests, the tests begin to fail,
fix the code, and the tests work again.
"""