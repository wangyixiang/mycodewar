import unittest
import math

http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor


def list_squared(m, n):
    def divisors(y):
        return filter(lambda yx: y % yx == 0, [yi for yi in xrange(1, y + 1)])

    def is_receation_one(x):

        r_sum = sum(map(lambda xx: xx * xx, divisorGenerator(x)))
        r_sum_sqrt = math.sqrt(r_sum)
        if r_sum_sqrt - math.floor(r_sum_sqrt) == 0:
            return [x, r_sum]
        return None

    return filter(lambda x: x, map(is_receation_one, [i for i in xrange(m, n)]))


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])


if __name__ == "__main__":
    unittest.main()
