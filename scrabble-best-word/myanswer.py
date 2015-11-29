import unittest


def get_best_word(points, words):
    def word_point(word):
        return reduce(lambda acc, c: acc + points[ord(c) - ord('A')], word, 0)

    word_points = map(word_point, words)
    max_points = 0
    largest_position = -1
    for i in range(len(words)):
        if word_points[i] > max_points:
            max_points = word_points[i]
            largest_position = i
            continue
        if word_points[i] == max_points:
            if len(words[i]) < len(words[largest_position]):
                largest_position = i
    return largest_position


from string import ascii_uppercase


def get_best_word_v2(points, words):
    points = dict(zip(ascii_uppercase, points))
    score = lambda w: sum([points[c] for c in w])
    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])


class TestMyAnswer(unittest.TestCase):
    def test_my_answer(self):
        points = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2, 1, 1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)

        self.assertEqual(get_best_word(points, ["WHO", "IS", "THE", "BEST", "OF", "US"]), 0)
        self.assertEqual(get_best_word(points, ["AABCDEF", "WHO", "IS", "THE", "BEST", "OF", "US"]), 1)
        self.assertEqual(get_best_word(points, ["NOQ", "TXAY", "S", "OM", "ESFT", "CJUKQ", "QL", "QO", "ASTK", "Y"]), 5)
        self.assertEqual(get_best_word(points, ["N", "AO", "TQGZW", "P", "OBTP", "CLWXB", "Y", "JQGFJ", "Q", "RP", "OC",
                                                "MRQCZ", "ZWN", "ZRT", "OIRYH", "GWPMSZP", "LQRYUKQ", "LBM", "LFEI",
                                                "VHUX", "RTALLIC", "JEMUPS", "XUW", "X", "ZLXFMWS", "LFAGR", "HJ",
                                                "RTUAI", "JRBNG", "ZUYSC", "CIEYV", "FUY", "B", "EJS", "CINBTQS",
                                                "JEAC", "JX", "LLILSEK", "W", "KLUV"]), 16)
        self.assertEqual(get_best_word(points,
                                       ["SVWLIDP", "FCPKTHW", "EREMN", "NFEF", "PQ", "FSC", "ZYPOSXJ", "BOR", "YCGG",
                                        "RC", "DVPE", "VAOE", "OIGK", "OTQE", "REJFUFD", "FVBCSSB", "VHJ", "BEC",
                                        "MWZQ", "WX", "L", "ZPCB", "JKLHE", "RYFTY", "NKP", "ID", "O", "KA", "VRXX",
                                        "NTDB", "OERKPC", "YFLUI", "SKQCJ", "PXDSW", "ITYWD", "TC", "LOIDQEJ", "NE",
                                        "YND", "VJHOCEC", "RPRANZ", "BQ", "STM", "RGVBFW", "SMWUYLW", "KT", "SXHY",
                                        "XCE", "T", "SC", "UDJU", "CHDR", "UGXNQ", "CQOOBA", "O", "NWW", "V", "L",
                                        "BAQ", "AZN", "LBTR", "N", "QSURR", "KADPH", "M", "LCBEAKM", "ZHEVXS", "F",
                                        "TVAIQCY", "MF", "KCI", "YQ", "RCG", "AKYPCP", "WJXG", "RQXOI", "SJI", "TWXZ",
                                        "J", "HIKCGHV", "EAAXGG", "AETSH", "EO", "BUET", "TDIQCO", "TKL", "FJCRY",
                                        "ZHAJLK", "OLMCVA", "F"]), 6)
        self.assertEqual(get_best_word(points,
                                       ["RBBL", "ZJ", "ZOFXE", "LMBFCFX", "O", "JG", "SYRYE", "VXG", "EU", "DAIFZR",
                                        "BQUNZHH", "WKO", "TFPHPLX", "SWLG", "CY", "JYQNDSM", "ITPS", "B", "UVSDMWR",
                                        "LCPS"]), 15)
        self.assertEqual(get_best_word(points,
                                       ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC',
                                        'ZRENSWMG']), 5)

        self.assertEqual(get_best_word_v2(points, ["WHO", "IS", "THE", "BEST", "OF", "US"]), 0)
        self.assertEqual(get_best_word_v2(points, ["AABCDEF", "WHO", "IS", "THE", "BEST", "OF", "US"]), 1)
        self.assertEqual(get_best_word_v2(points, ["NOQ", "TXAY", "S", "OM", "ESFT", "CJUKQ", "QL", "QO", "ASTK", "Y"]), 5)
        self.assertEqual(get_best_word_v2(points, ["N", "AO", "TQGZW", "P", "OBTP", "CLWXB", "Y", "JQGFJ", "Q", "RP", "OC",
                                                "MRQCZ", "ZWN", "ZRT", "OIRYH", "GWPMSZP", "LQRYUKQ", "LBM", "LFEI",
                                                "VHUX", "RTALLIC", "JEMUPS", "XUW", "X", "ZLXFMWS", "LFAGR", "HJ",
                                                "RTUAI", "JRBNG", "ZUYSC", "CIEYV", "FUY", "B", "EJS", "CINBTQS",
                                                "JEAC", "JX", "LLILSEK", "W", "KLUV"]), 16)
        self.assertEqual(get_best_word_v2(points,
                                       ["SVWLIDP", "FCPKTHW", "EREMN", "NFEF", "PQ", "FSC", "ZYPOSXJ", "BOR", "YCGG",
                                        "RC", "DVPE", "VAOE", "OIGK", "OTQE", "REJFUFD", "FVBCSSB", "VHJ", "BEC",
                                        "MWZQ", "WX", "L", "ZPCB", "JKLHE", "RYFTY", "NKP", "ID", "O", "KA", "VRXX",
                                        "NTDB", "OERKPC", "YFLUI", "SKQCJ", "PXDSW", "ITYWD", "TC", "LOIDQEJ", "NE",
                                        "YND", "VJHOCEC", "RPRANZ", "BQ", "STM", "RGVBFW", "SMWUYLW", "KT", "SXHY",
                                        "XCE", "T", "SC", "UDJU", "CHDR", "UGXNQ", "CQOOBA", "O", "NWW", "V", "L",
                                        "BAQ", "AZN", "LBTR", "N", "QSURR", "KADPH", "M", "LCBEAKM", "ZHEVXS", "F",
                                        "TVAIQCY", "MF", "KCI", "YQ", "RCG", "AKYPCP", "WJXG", "RQXOI", "SJI", "TWXZ",
                                        "J", "HIKCGHV", "EAAXGG", "AETSH", "EO", "BUET", "TDIQCO", "TKL", "FJCRY",
                                        "ZHAJLK", "OLMCVA", "F"]), 6)
        self.assertEqual(get_best_word_v2(points,
                                       ["RBBL", "ZJ", "ZOFXE", "LMBFCFX", "O", "JG", "SYRYE", "VXG", "EU", "DAIFZR",
                                        "BQUNZHH", "WKO", "TFPHPLX", "SWLG", "CY", "JYQNDSM", "ITPS", "B", "UVSDMWR",
                                        "LCPS"]), 15)
        self.assertEqual(get_best_word_v2(points,
                                       ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC',
                                        'ZRENSWMG']), 5)


if __name__ == "__main__":
    unittest.main()
