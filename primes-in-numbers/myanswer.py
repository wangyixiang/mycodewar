#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. 开始的解法思路是得出小于Ｎ的完整素数列表，然后用得到的素数列表，从小到大去
# 反复除的方法得到所有的素数乘积集合，下面是得到素数集的算法。（注意后面有但是）

# http://www.cnblogs.com/luluping/archive/2010/03/03/1677552.html
# 可以参考一下是思想，但是里面的实现代码很多都是错的，坑爹得很。
# the prime generator
# https://inventwithpython.com/hacking/chapter23.html
# http://thelivingpearl.com/2013/01/06/how-to-find-prime-numbers-in-python/

# in codewar the timeout for an answer finishing running is 6000ms, the below way will not fullfil the request.
# 算法一：是利用小于sqrt(N)的所有数来进行整除测试
def old_isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# 算法二：是利用所有小于sqrt(N)的所有质数来进行整除测试
primes = [2]


def isPrime(n):
    global primes
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    i = 0
    while primes[i] * primes[i] <= n:
        if n % primes[i] == 0:
            return False
        if i < len(primes) - 1:
            i += 1
        else:
            break
    primes.append(n)
    return True


# 算法三：是利用筛选法，与一和二不一样的地方，上面是一个一个数判断，这个算法是直接对一组数进行。
# 素数筛选方法来得到完整的小于Ｎ的素数集合，比每个数的判断要快很多倍，而且思想是非常有趣的。
# 这个算法还可以把筛子再优化，不知道可以快多少？
import math


def primeSieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * (sieveSize + 1)
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer <= sieveSize:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieveSize + 1):
        if sieve[i] == True:
            primes.append(i)

    return primes


def prime():
    i = 2
    yield i
    i = 3
    while True:
        if isPrime(i):
            yield i
        i += 2


import time

pms = []
pg = prime()

start = time.time()

for i in range(361407):
    pms.append(pg.next())
end = time.time()

print len(pms), "it took ", end - start, " seconds"

start = time.time()

pms = primeSieve(5200000)

end = time.time()

print len(pms), "it took ", end - start, " seconds"


# 6000000中412849个素数时第一个为55秒， 第二个为9秒，

def primesgen():
    for x in pms:
        yield x


def primeFactors_p(n):
    if isPrime(n):
        return "(" + str(n) + ")"
    pg = primesgen()
    p = pg.next()
    pexrs = []
    while not ((n % p == 0) and (n / p == 1)):
        pcount = 0
        while n % p == 0:
            n = n / p
            pcount += 1

        if pcount == 1:
            pexrs.append("(" + str(p) + ")")
        elif pcount > 1:
            pexrs.append("(" + str(p) + "**" + str(pcount) + ")")
        p = pg.next()
    pexrs.append("(" + str(p) + ")")
    return "".join(pexrs)


# 但是，但是在这里，我的这个解法并不是这道为题的最优解法，这个问题完全
# 可以不用去求小Ｎ的完整素数列表，只要用反复除就可以了，想想也很简单，
# 假设Ｐ1..P(i)P(i+1)..Ｐm个素数，当Ｎ被Ｐi除到除不尽时，所有Ｐi到Ｐ(i+1)
# 间的数一定是无法是剩余Ｎ的因数，因为所有的因数都被Ｐ1..Ｐi的整除给过滤掉了
def primeFactors_n(n):
    pexrs = []
    pcount = 0
    for x in xrange(2, n + 1):
        while n % x == 0:
            pcount += 1
            n /= x
        if pcount != 0:
            pexrs.append("({}{})".format(x, "**%d" % pcount if pcount > 1 else ""))
            pcount = 0
        if n == 1:
            break
    return "".join(pexrs)


def time_func(f):
    def time_f(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print "it took ", end - start, " seconds"
        return result

    return time_f


print time_func(primeFactors_n)(7775460)
print time_func(primeFactors_p)(7775460)
print time_func(primeFactors_n)(86240)
print time_func(primeFactors_p)(86240)
print time_func(primeFactors_n)(933555431)
print time_func(primeFactors_p)(933555431)


def primeFactors(n):
    return primeFactors_n(n)


import unittest


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        self.assertEqual(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        self.assertEqual(primeFactors(7919), "(7919)")
        self.assertEqual(primeFactors(17*17*93*677), "(3)(17**2)(31)(677)")
        self.assertEqual(primeFactors(933555431), "(7537)(123863)")
        self.assertEqual(primeFactors(342217392), "(2**4)(3)(11)(43)(15073)")
        self.assertEqual(primeFactors(35791357), "(7)(5113051)", )
        self.assertEqual(primeFactors(782611830), "(2)(3**2)(5)(7**2)(11)(13)(17)(73)")
        self.assertEqual(primeFactors(775878912), "(2**8)(3**4)(17)(31)(71)")

if __name__ == "__main__":
    unittest.main()
