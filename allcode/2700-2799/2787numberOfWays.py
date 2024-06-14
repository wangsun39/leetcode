# 给你两个 正 整数 n 和 x 。
#
# 请你返回将 n 表示成一些 互不相同 正整数的 x 次幂之和的方案数。换句话说，你需要返回互不相同整数 [n1, n2, ..., nk] 的集合数目，满足 n = n1x + n2x + ... + nkx 。
#
# 由于答案可能非常大，请你将它对 109 + 7 取余后返回。
#
# 比方说，n = 160 且 x = 3 ，一个表示 n 的方法是 n = 23 + 33 + 53 。
#
#
#
# 示例 1：
#
# 输入：n = 10, x = 2
# 输出：1
# 解释：我们可以将 n 表示为：n = 32 + 12 = 10 。
# 这是唯一将 10 表达成不同整数 2 次方之和的方案。
# 示例 2：
#
# 输入：n = 4, x = 1
# 输出：2
# 解释：我们可以将 n 按以下方案表示：
# - n = 41 = 4 。
# - n = 31 + 11 = 4 。
#
#
# 提示：
#
# 1 <= n <= 300
# 1 <= x <= 5

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        cand = []
        i = 1
        while True:
            y = i ** x
            if y <= n:
                cand.append(y)
                i += 1
            else:
                break
        dp = [[0] * (n + 1) for _ in range(len(cand))]  # dp[i][j] 表示 前i个数，
        dp[0][1] = 1
        for i in range(1, len(cand)):
            y = cand[i]
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if j > y:
                    dp[i][j] += dp[i - 1][j - y]
                elif j == y:
                    dp[i][j] += 1
                dp[i][j] %= MOD
        return dp[-1][n]



so = Solution()
print(so.numberOfWays(n = 2, x = 2))
print(so.numberOfWays(n = 10, x = 2))
print(so.numberOfWays(n = 4, x = 1))




