import unittest


def spin_words(sentence):
    def spin(word):
        if len(word) >= 5:
            return reduce(lambda x,y: x + y, reversed(word), "")
        else:
            return word
    return ' '.join(map(spin, sentence.split()))


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This is a test"), "This is a test")
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")


if __name__ == "__main__":
    unittest.main()
