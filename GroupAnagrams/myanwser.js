/**
 * Created by wangyixiang on 15-11-23.
 */

Array.prototype.compare = function (testArr) {
    if (this.length != testArr.length) {
        return false;
    }

    // first sort the arrays
    var deepSort = function (a, b) {
            // if the two elements are arrays
            if (a.length && a[0].compare) {
                return a.length - b.length;
            }

            if (a > b) {
                return 1;
            } else if (a < b) {
                return -1;
            }

            return 0;
        },
        thisCopy = this.slice(0).sort(deepSort),
        testArrayCopy = testArr.slice(0).sort(deepSort);

    for (var i = 0; i < thisCopy.length; i++) {
        if (thisCopy[i].compare) {
            if (!thisCopy[i].compare(testArrayCopy[i])) {
                return false;
            }
        } else {
            if (thisCopy[i].toLowerCase() !== testArrayCopy[i].toLowerCase()) {
                return false;
            }
        }
    }

    return true;
}

assertSimilarUnsorted = function (array, expected, message) {
    return expect(array.compare(expected), message);
};


function groupAnagrams(words) {
    var wordCategory = {}

    for (var i = 0; i < words.length; i++) {
        var word_chars = words[i].split("");
        var word_key = word_chars.sort().join("");
        var word_chars_codes = word_chars.map(function (c) {
            return c.charCodeAt(0);
        })

        wordCategory[words[i].length] || ( wordCategory[words[i].length] = {} );

        var chars_sum = word_chars_codes.reduce(function (pre, cur) {
            return pre + cur;
        })
        wordCategory[words[i].length][chars_sum] || (wordCategory[words[i].length][chars_sum] = {});

        wordCategory[words[i].length][chars_sum][word_key] = [] || (wordCategory[words[i].length][chars_sum][word_key] = []);

        wordCategory[words[i].length][chars_sum][word_key].push(words[i]);
    }
    var result = [];
    Object.keys(wordCategory).forEach(function (lenItem) {
            Object.keys(wordCategory[lenItem]).forEach(function (sumItem) {
                Object.keys(wordCategory[lenItem][sumItem]).forEach(function (wordKey) {
                    result.push(wordCategory[lenItem][sumItem][wordKey])
                })
            })
        }
    )

    return result
}


describe("Human cases", function () {

    it("Light lists", function () {

        assertSimilarUnsorted(groupAnagrams(["rat", "tar", "star"]), [["rat", "tar"], ["star"]]);
        assertSimilarUnsorted(groupAnagrams(["tsar", "star", "tars", "rat", "tar", "cheese"]), [["tsar", "star", "tars"], ["rat", "tar"], ["cheese"]]);

    });

    it("Edge cases", function () {

        assertSimilarUnsorted(groupAnagrams([]), []);
        assertSimilarUnsorted(groupAnagrams(["hello"]), [["hello"]]);
        assertSimilarUnsorted(groupAnagrams(["aaA", "Aaa", "aaa"]), [["aaA", "Aaa"], ["aaa"]]);

    });

});

describe("Superhero cases", function () {

    it("Heavy computation that is way too long to be output (so if it fails you need to optimize the algorithm!)", function () {

        //+ Jonas Raoni Soares Silva
        //@ http://jsfromhell.com/array/shuffle [v1.0]
        function shuffle(o) { //v1.0
            for (var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
            return o;
        };

        var alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!%$@:;.,(){}[]=+-_",
            anagrams = [],
            words;

        // generate many anagrams
        for (var i = 0; i < 1000; i++) {
            anagrams.push(shuffle(alphabet));
        }

        // add some words
        words = anagrams.slice();
        words.push("star");
        words.push("tsar");

        assertSimilarUnsorted(groupAnagrams(words), [
            ["star", "tsar"],
            anagrams
        ]);

    });

});