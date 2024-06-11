# 有 n 根长度互不相同的木棍，长度为从 1 到 n 的整数。请你将这些木棍排成一排，并满足从左侧 可以看到 恰好 k 根木棍。从左侧 可以看到 木棍的前提是这个木棍的 左侧 不存在比它 更长的 木棍。
#
# 例如，如果木棍排列为 [1,3,2,5,4] ，那么从左侧可以看到的就是长度分别为 1、3 、5 的木棍。
# 给你 n 和 k ，返回符合题目要求的排列 数目 。由于答案可能很大，请返回对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
# 输入：n = 3, k = 2
# 输出：3
# 解释：[1,3,2], [2,3,1] 和 [2,1,3] 是仅有的能满足恰好 2 根木棍可以看到的排列。
# 可以看到的木棍已经用粗体+斜体标识。
# 示例 2：
#
# 输入：n = 5, k = 5
# 输出：1
# 解释：[1,2,3,4,5] 是唯一一种能满足全部 5 根木棍可以看到的排列。
# 可以看到的木棍已经用粗体+斜体标识。
# 示例 3：
#
# 输入：n = 20, k = 11
# 输出：647427950
# 解释：总共有 647427950 (mod 109 + 7) 种能满足恰好有 11 根木棍可以看到的排列。
#
#
# 提示：
#
# 1 <= n <= 1000
# 1 <= k <= n
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res *= i
                res %= MOD
            return res

        @cache
        def dfs(nn, kk):  # 长度为m的
            if nn == 1 or nn == kk: return 1
            if kk == 1:
                return factorial(nn - 1) % MOD
            # 当从n-1扩充到n个棍子时，不失一般性，增加的是最短的一根，分成两种情况
            # 前n-1个组成k-1组，最短的一根自成一组，放在最前面
            # 前n - 1个组成k组，那么最短的一根可以放在任意一根的后面
            return (dfs(nn - 1, kk - 1) + dfs(nn - 1, kk) * (nn - 1)) % MOD
        return dfs(n, k)


so = Solution()
print(so.rearrangeSticks(n = 5, k = 5))
print(so.rearrangeSticks(n = 3, k = 2))
print(so.rearrangeSticks(n = 20, k = 11))




