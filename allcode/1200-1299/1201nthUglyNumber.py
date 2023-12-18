# 给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
#
# 丑数是可以被 a 或 b 或 c 整除的 正整数 。
#
#
#
# 示例 1：
#
# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
# 示例 2：
#
# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
# 示例 3：
#
# 输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
# 示例 4：
#
# 输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984
#
#
# 提示：
#
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# 本题结果在 [1, 2 * 10^9] 的范围内
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(val):
            gab = math.lcm(a, b)
            gbc = math.lcm(b, c)
            gac = math.lcm(a, c)
            gabc = math.lcm(a, b, c)
            return val // a + val // b + val // c - val // gab - val // gbc - val // gac + val // gabc >= n

        lo, hi = 0, 2 * 10 ** 9
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.nthUglyNumber(n = 3, a = 2, b = 3, c = 5))
print(so.nthUglyNumber(n = 4, a = 2, b = 3, c = 4))
print(so.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))
print(so.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))




