# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
#
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。
#
#
#
# 示例 1：
#
# 输入：n = 1, a = 2, b = 3
# 输出：2
# 示例 2：
#
# 输入：n = 4, a = 2, b = 3
# 输出：6
#
#
# 提示：
#
# 1 <= n <= 109
# 2 <= a, b <= 4 * 104


from typing import List
import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        lcm = math.lcm(a, b)
        def count(n):
            c1, c2 = math.floor(n / a), math.floor(n / b)
            c3 = math.floor(n / lcm)
            if n % a == 0 or n % b == 0:
                return c1 + c2 - c3
            return c1 + c2 - c3 + 0.5  # 不能整除，说明n并不是神奇数字
        low, high = min(a, b) - 1, max(a, b) * n + 1
        while True:
            mid = (low + high) // 2
            v = count(mid)
            if v == n:
                return mid % MOD
            elif v > n:
                high = mid
            else:
                low = mid




so = Solution()
print(so.nthMagicalNumber(n = 1000000000, a = 40000, b = 40000))  # 999720007
print(so.nthMagicalNumber(n = 1, a = 2, b = 3))  # 2
print(so.nthMagicalNumber(n = 4, a = 2, b = 3))  # 6


