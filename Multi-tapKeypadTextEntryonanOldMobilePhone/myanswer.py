import unittest

def presses(phrase):
    keyboard_layout = [" 0", "1", "abc2", "def3", "ghi4", "jkl5", "mno6", "pqrs7", "tuv8", "wxyz9", "*", "#"]
    keyboard_layout_string = "".join(keyboard_layout)
    keyboard_layout_count = []
    press_count = 0

    for i in range(len(keyboard_layout)):
        keyboard_layout_count.append(len(keyboard_layout[i]))

    for char in phrase.lower():
        char_pos = keyboard_layout_string.find(char) + 1
        for count in keyboard_layout_count:
            char_pos = char_pos - count
            if char_pos <= 0:
                press_count = press_count + char_pos + count
                break

    return press_count


class TestMyAnswer(unittest.TestCase):

    def test_my_answer(self):
        self.assertEqual(presses("LOL"), 9)
        self.assertEqual(presses("HOW R U"), 13)
        self.assertEqual(presses("WHERE DO U WANT 2 MEET L8R"), 47)
        self.assertEqual(presses("#codewars #rocks"), 36)

if __name__ == "__main__":
    unittest.main()
