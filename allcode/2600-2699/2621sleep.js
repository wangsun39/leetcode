//请你编写一个异步函数，它接收一个正整数参数 millis ，并休眠 millis 毫秒。要求此函数可以解析任何值。
//
//请注意，实际睡眠持续时间与 millis 之间的微小偏差是可以接受的。
//
//
//
//示例 1：
//
//输入：millis = 100
//输出：100
//解释：
//在 100ms 后此异步函数执行完时返回一个 Promise 对象
//let t = Date.now();
//sleep(100).then(() => {
//  console.log(Date.now() - t); // 100
//});
//示例 2：
//
//输入：millis = 200
//输出：200
//解释：在 200ms 后函数执行完时返回一个 Promise 对象
//
//
//提示：
//
//1 <= millis <= 1000

// 在 JavaScript 里，函数本质上没有“声明级别”的构造函数与普通函数区别，只有“调用方式”区别。
// 也就是说，它是不是构造函数取决于是否用 new 调用，以及它的代码和周边用法是否“意图”让它当构造函数用。
var TimeLimitedCache = function() {
    this.cache = new Map();  // 构造函数
};


/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // 这里是给构造函数的原型对象 prototype 添加一个 set 方法。所有通过 new TimeLimitedCache() 创建的实例都能在其原型链上访问到这个方法。
    if (this.cache.has(key)) {
        var vs = this.cache.get(key);
        clearTimeout(vs.timeout);
        const timeout = setTimeout(() => this.cache.delete(key), duration);
        this.cache.delete(key);
        this.cache.set(key, {value, timeout});
        return true;
    }
    const timeout = setTimeout(() => this.cache.delete(key), duration);
    this.cache.set(key, {value, timeout});
    // 上句的等价的长写法  this.cache.set(key, { value: value, timeout: timeout });
    return false;

};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache.has(key)) {
        return this.cache.get(key).value;
    }
    return -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */


