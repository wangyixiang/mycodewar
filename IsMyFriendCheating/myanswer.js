/**
 * Created by wangyixiang on 15-11-18.
 */
function removeNb (n) {
    function getArray(n){
        var result = []
        for( var i = 1; i <= n ; i++){
            result.push(i)
        }
        return result
    }

    var the_pairs = []
    var n_arr = getArray(n)
    var n_sum = n_arr.reduce(function(x, y) { return x + y}, 0)

    if (n < 3) {
        return the_pairs
    }

    var stop_point = Math.floor(n / 2)
    var i = n - 1
    while (i > stop_point) {
        var j = i - 1
        while ( j > stop_point){
            if ((n_arr[i] * n_arr[j]) === (n_sum - n_arr[i] - n_arr[j])){
                return [[n_arr[j],n_arr[i]], [n_arr[i], n_arr[j]]]
            }
            j -= 1
        }
        i -= 1
    }
    return the_pairs
}