/**
 * Created by wangyixiang on 15-11-20.
 */

function sumStrings(a, b) {
    var a_arr = a.split("");
    var b_arr = b.split("");

    if (a_arr.length > b_arr.length) {
        for (; a_arr.length != b_arr.length;) {
            b_arr.unshift("0");
        }
    }
    else if (a_arr.length < b_arr.length) {
        for (; b_arr.length != a_arr.length;) {
            a_arr.unshift("0");
        }
    }
    var result = [];
    var adv = 0;
    for (var i = a_arr.length - 1; i >= 0; i--) {

        var c = Number(a_arr[i]) + Number(b_arr[i]) + adv;
        if (c >= 10) {
            adv = 1;
            c -= 10;
        } else {
            adv = 0;
        }
        result.unshift(c);
    }
    if (adv != 0) {
        result.unshift(adv)
    }
    return result.join("").replace(/^0+/, '');
}

function t(a, b, answer) {
    expect(sumStrings(a, b)).toBe(answer);
}

describe("The test", function () {
    it("should pass", function () {
        t('123', '456', '579');
        t('8797', '45', '8842');
        t('800', '9567', '10367');
        t('99', '1', '100');
        t('00103', '08567', '8670');
        t('', '5', '5');
        t('712569312664357328695151392',
            '8100824045303269669937',
            '712577413488402631964821329');
        t('50095301248058391139327916261',
            '81055900096023504197206408605',
            '131151201344081895336534324866');
    })
});
