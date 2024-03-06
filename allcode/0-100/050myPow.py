# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
#
#
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#
#
# 提示：
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -104 <= xn <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        bits = [x]
        m = abs(n)
        for i in range(m.bit_length()):
            bits.append(bits[-1] ** 2)
        ans = 1
        for i in range(m.bit_length()):
            if (1 << i) & m:
                ans *= bits[i]
        if n < 0:
            ans = 1 / ans
        return ans

so = Solution()
print(so.myPow(x = 2.00000, n = 10))
print(so.myPow(x = 2.10000, n = 3))
print(so.myPow(x = 2.00000, n = -2))




