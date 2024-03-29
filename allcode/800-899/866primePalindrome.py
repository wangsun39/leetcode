# 给你一个整数 n ，返回大于或等于 n 的最小回文质数。
#
# 一个整数如果恰好有两个除数：1 和它本身，那么它是 质数 。注意，1 不是质数。
#
# 例如，2、3、5、7、11 和 13 都是质数。
# 一个整数如果从左向右读和从右向左读是相同的，那么它是 回文数 。
#
# 例如，101 和 12321 都是回文数。
# 测试用例保证答案总是存在，并且在 [2, 2 * 108] 范围内。
#
#
#
# 示例 1：
#
# 输入：n = 6
# 输出：7
# 示例 2：
#
# 输入：n = 8
# 输出：11
# 示例 3：
#
# 输入：n = 13
# 输出：101
#
#
# 提示：
#
# 1 <= n <= 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(n: int) -> bool:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return n >= 2  # 1 不是质数
        s = str(n)
        l = len(s)
        half = int(s[:(l + 1) // 2])
        if n < 10:
            for x in range(n, 12):
                if is_prime(x):
                    return x
        def double(x, odds):
            if odds:
                return int(str(x) + str(x)[:-1][::-1])
            return int(str(x) + str(x)[::-1])
        if l & 1:
            for x in range(half, 10 ** 5):
                y = double(x, 1)
                if y < n: continue
                if is_prime(y):
                    return y
            for x in range(half, 10 ** 5):
                y = double(x, 0)
                if y < n: continue
                if is_prime(y):
                    return y
        else:
            for x in range(half, 10 ** 5):
                y = double(x, 0)
                if y < n: continue
                if is_prime(y):
                    return y
            for x in range(10 ** (l // 2), 10 ** 5):
                y = double(x, 1)
                if y < n: continue
                if is_prime(y):
                    return y








so = Solution()
print(so.primePalindrome(10))
print(so.primePalindrome(13))
print(so.primePalindrome(8))
print(so.primePalindrome(6))




