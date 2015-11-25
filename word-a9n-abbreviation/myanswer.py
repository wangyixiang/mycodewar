import unittest
import re


def abbreviate(s):
    def abbr_word(w):
        if len(w) < 4:
            return w
        return w[0] + str(len(w[1:-1])) + w[-1]

    splitters = ".:'; -,"
    last_word = ""
    result = []
    for i in xrange(len(s)):
        if splitters.find(s[i]) != -1:
            result.append(abbr_word(last_word))
            result.append(abbr_word(s[i]))
            last_word = ""
        else:
            last_word += s[i]
    result.append(abbr_word(last_word))
    return "".join(result)


def abbreviate2(s):
    def abbr_word(w):
        return w[0] + str(len(w[1:-1])) + w[-1]

    return re.sub(r"\w{4,}", lambda m: abbr_word(m.group(0)), s)


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        self.assertEqual(abbreviate("internationalization"), "i18n")
        self.assertEqual(abbreviate("accessibility"), "a11y")
        self.assertEqual(abbreviate("Accessibility"), "A11y")
        self.assertEqual(abbreviate("cat. monolithic-monolithic: double-barreled'doggy-a: mat-balloon; "),
                         "cat. m8c-m8c: d4e-b6d'd3y-a: mat-b5n; ")
        self.assertEqual(abbreviate2("internationalization"), "i18n")
        self.assertEqual(abbreviate2("accessibility"), "a11y")
        self.assertEqual(abbreviate2("Accessibility"), "A11y")
        self.assertEqual(abbreviate2("cat. monolithic-monolithic: double-barreled'doggy-a: mat-balloon; "),
                         "cat. m8c-m8c: d4e-b6d'd3y-a: mat-b5n; ")


if __name__ == "__main__":
    unittest.main()
