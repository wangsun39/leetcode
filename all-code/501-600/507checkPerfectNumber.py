# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
#
#  
#
# 示例 1：
#
# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。
# 示例 2：
#
# 输入：num = 6
# 输出：true
# 示例 3：
#
# 输入：num = 496
# 输出：true
# 示例 4：
#
# 输入：num = 8128
# 输出：true
# 示例 5：
#
# 输入：num = 2
# 输出：false
#  
#
# 提示：
#
# 1 <= num <= 108



import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 1 if num > 1 else 0
        N = int(math.sqrt(num))
        for i in range(2, N + 1):
            if num % i == 0:
                res += i
                res += (num // i)
        return res == num

so = Solution()
print(so.checkPerfectNumber(1))
print(so.checkPerfectNumber(28))
print(so.checkPerfectNumber(6))
print(so.checkPerfectNumber(496))
print(so.checkPerfectNumber(2))
print(so.checkPerfectNumber(99999994))

