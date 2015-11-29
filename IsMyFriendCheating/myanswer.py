import unittest
import math


def removNb(n):
    the_pairs = []
    n_arr = range(n + 1)
    n_sum = sum(n_arr) * 1.0
    n_half_arr = range(n / 2, n)
    if n < 3:
        return the_pairs

    for x in n_half_arr:
        y = (n_sum - x) / (x + 1)
        if y > 1 and y <= n and (y - math.floor(y) == 0):
            the_pairs.append((x, int(y)))
            the_pairs.append((int(y), x))
            n_half_arr.remove(y)
    the_pairs.sort()
    return the_pairs

    # 利用计算，使得速度远远快于循环遍历比对。
    ############################################
    # stop_point = n / 2
    # i = n - 1
    # while i > stop_point:
    #     j = i - 1
    #     while j > stop_point:
    #         if n_arr[i] * n_arr[j] == (n_sum - n_arr[i] - n_arr[j]):
    #             the_pairs.append((n_arr[j], n_arr[i]))
    #             the_pairs.append((n_arr[i], n_arr[j]))
    #             return the_pairs
    #         j -= 1
    #     i -= 1
    # return the_pairs
    #############################################
    # for i in range((n + 1) / 2, n + 1, 1):
    #     for j in range(i - 1, n + 1, 1):
    #         if i * j == (n_sum - i - j):
    #             the_pairs.append((i, j))
    #             the_pairs.append((j, i))
    #             return the_pairs
    # return the_pairs
    #############################################
    # for i in xrange(n + 1, (n + 1) / 2, -1):
    #     for j in xrange(n + 1, i - 1, -1):
    #         if i * j == (n_sum - i - j):
    #             the_pairs.append((i, j))
    #             the_pairs.append((j, i))
    #             return the_pairs


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        self.assertEqual(removNb(100), [])
        self.assertEqual(removNb(26), [(15, 21), (21, 15)])
        self.assertEqual(removNb(101), [(55, 91), (91, 55)])
        self.assertEqual(removNb(102), [(70, 73), (73, 70)])
        self.assertEqual(removNb(110), [(70, 85), (85, 70)])
        self.assertEqual(removNb(1006), [(546, 925), (925, 546)])
        self.assertEqual(removNb(446), [(252, 393), (393, 252)])


if __name__ == "__main__":
    unittest.main()
