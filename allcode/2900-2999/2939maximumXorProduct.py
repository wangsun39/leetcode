# 给你三个整数 a ，b 和 n ，请你返回 (a XOR x) * (b XOR x) 的 最大值 且 x 需要满足 0 <= x < 2n。
#
# 由于答案可能会很大，返回它对 109 + 7 取余 后的结果。
#
# 注意，XOR 是按位异或操作。
#
#
#
# 示例 1：
#
# 输入：a = 12, b = 5, n = 4
# 输出：98
# 解释：当 x = 2 时，(a XOR x) = 14 且 (b XOR x) = 7 。所以，(a XOR x) * (b XOR x) = 98 。
# 98 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
# 示例 2：
#
# 输入：a = 6, b = 7 , n = 5
# 输出：930
# 解释：当 x = 25 时，(a XOR x) = 31 且 (b XOR x) = 30 。所以，(a XOR x) * (b XOR x) = 930 。
# 930 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
# 示例 3：
#
# 输入：a = 1, b = 6, n = 3
# 输出：12
# 解释： 当 x = 5 时，(a XOR x) = 4 且 (b XOR x) = 3 。所以，(a XOR x) * (b XOR x) = 12 。
# 12 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
#
#
# 提示：
#
# 0 <= a, b < 250
# 0 <= n <= 50

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        def F(n):
            return (1 << n) - 1
        if a < b:
            a, b = b, a
        na, nb = a.bit_length(), b.bit_length()
        nab = max(na, nb)
        if nab > n:
            ta = a & (F(nab) << n)  # 记录目标 a XOR x 和 b XOR x
            tb = b & (F(nab) << n)
        else:
            ta = (F(n) << nab) & F(n)
            tb = (F(n) << nab) & F(n)

        left = min(nab, n)  # 剩余要处理的数位
        left_a = a & F(left)
        left_b = b & F(left)
        aorb = left_a ^ left_b
        l_aorb = aorb.bit_length()
        rev_aorb = (~aorb) & ((1 << left) - 1)  # 在 left 范围内对 aorb 取反
        if ta != tb:
            ta |= rev_aorb
            tb |= F(left)
        else:
            if l_aorb > 0:
                ta = ta | (1 << (l_aorb - 1)) | rev_aorb
                tb = tb | (1 << (l_aorb - 1)) ^ aorb | rev_aorb
            else:
                ta |= F(left)
                tb |= F(left)
        return ta * tb % MOD





so = Solution()
print(so.maximumXorProduct(a = 6, b = 7, n = 5))  # 930
print(so.maximumXorProduct(a = 12, b = 5, n = 4))  # 98
print(so.maximumXorProduct(a = 0, b = 5, n = 6))
print(so.maximumXorProduct(a = 0, b = 7, n = 2))
print(so.maximumXorProduct(a = 0, b = 3, n = 1))
print(so.maximumXorProduct(a = 1, b = 6, n = 3))  # 12




