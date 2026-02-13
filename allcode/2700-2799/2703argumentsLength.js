//请你编写一个函数 argumentsLength，返回传递给该函数的参数数量。
//
//
//示例 1：
//
//输入：args = [5]
//输出：1
//解释：
//argumentsLength(5); // 1
//
//只传递了一个值给函数，因此它应返回 1。
//示例 2：
//
//输入：args = [{}, null, "3"]
//输出：3
//解释：
//argumentsLength({}, null, "3"); // 3
//
//传递了三个值给函数，因此它应返回 3。
//
//
//提示：
//
//args 是一个有效的 JSON 数组
//0 <= args.length <= 100

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */


