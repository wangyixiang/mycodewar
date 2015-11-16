/**
 * Created by wangyixiang on 15-11-16.
 */

function listSquared(m, n) {
    /*The algorithm used here to find all divisors is not efficient enough
    to pass the python version test suite, the algorithm I used in python is
    getting from the internet, it will pass the test suite run time limit requirement.
    */
    function divisors(x) {
        var i = 1;
        var result = [];
        for (; i <= x; i++) {
            if (x % i === 0) {
                result.push(i);
            }
        }
        return result;
    }

    function isReceationOne(x) {
        var sumResult = divisors(x).reduce(function (prev, cur) {
            return prev + cur * cur;
        }, 0)

        if (Math.sqrt(sumResult) - Math.floor(Math.sqrt(sumResult)) === 0) {
            return [x, sumResult];
        }

        return "wangyixiang";
    }

    result = [];

    for (var i = m; i <= n; i++) {
        r = isReceationOne(i);
        if (r !== "wangyixiang") {
            result.push(r);
        }
    }

    return result;
}
