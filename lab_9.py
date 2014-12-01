# -*- coding: cp1251 -*-

def fib_rec(n): #рекурсивный алгоритм; O(Ф^n) - экспоненциальное время

            """
                >>> fib_rec(1)
                    1
                        >>> fib_rec(5)
                            5
                                >>> fib_rec(29)
                                    514229
                                        """

                                            if n == 0:
                                                        return 0

                                                        elif n == 1 or n == 2:
                                                                    return 1

                                                                    else:
                                                                                return fib_rec(n-1) + fib_rec(n-2)


                                                                            def fib_iter(n): #нерекурсивный алгоритм; O(n)

                                                                                        """
                                                                                            >>> fib_iter(1)
                                                                                                1
                                                                                                    >>> fib_iter(5)
                                                                                                        5
                                                                                                            >>> fib_iter(29)
                                                                                                                514229
                                                                                                                    """

                                                                                                                        if n == 1 or n == 2:
                                                                                                                                    return 1

                                                                                                                                    fib1 = fib2 = 1
                                                                                                                                        i = 2

                                                                                                                                            while i < n:
                                                                                                                                                            fibs = fib1 + fib2
                                                                                                                                                                        fib1 = fib2
                                                                                                                                                                                    fib2 = fibs
                                                                                                                                                                                                i = i + 1

                                                                                                                                                                                                    return fibs

                                                                                                                                                                                                def fib_magic(n): #волшенбный алгоритм; O(logn)

                                                                                                                                                                                                        """
                                                                                                                                                                                                            >>> fib_magic(1)
                                                                                                                                                                                                                1
                                                                                                                                                                                                                    >>> fib_magic(5)
                                                                                                                                                                                                                        5
                                                                                                                                                                                                                            >>> fib_magic(29)
                                                                                                                                                                                                                                514229
                                                                                                                                                                                                                                    """

                                                                                                                                                                                                                                        a = b = c = rd = 1
                                                                                                                                                                                                                                            rc = d = 0

                                                                                                                                                                                                                                                while n:
                                                                                                                                                                                                                                                            if n & 1:
                                                                                                                                                                                                                                                                            tc = rc
                                                                                                                                                                                                                                                                                        rc = rc*a + rd*c
                                                                                                                                                                                                                                                                                                    rd = tc*b + rd*d

                                                                                                                                                                                                                                                                                                            ta = a
                                                                                                                                                                                                                                                                                                                    tb = b
                                                                                                                                                                                                                                                                                                                            tc = c
                                                                                                                                                                                                                                                                                                                                    a = a*a + b*c
                                                                                                                                                                                                                                                                                                                                            b = ta*b + b*d
                                                                                                                                                                                                                                                                                                                                                    c = c*ta + d*c
                                                                                                                                                                                                                                                                                                                                                            d = tc*tb + d*d

                                                                                                                                                                                                                                                                                                                                                                    n >>= 1

                                                                                                                                                                                                                                                                                                                                                                        return rc

                                                                                                                                                                                                                                                                                                                                                                    def test(fn):
                                                                                                                                                                                                                                                                                                                                                                            samples = [(0, 1), (1, 2), (2, 4), (7, 9), (3, 8), (10, 66), (1488, 33333)]
                                                                                                                                                                                                                                                                                                                                                                                for c in samples:
                                                                                                                                                                                                                                                                                                                                                                                            print fn.__name__, "OK"

                                                                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                    test(fib_rec)
                                                                                                                                                                                                                                                                                                                                                                                                        test(fib_iter)
                                                                                                                                                                                                                                                                                                                                                                                                            test(fib_magic)
                                                                                                                                                                                                                                                                                                                                                                                                                import doctest
                                                                                                                                                                                                                                                                                                                                                                                                                    doctest.testmod()
