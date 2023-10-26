# 给你一个整数 n 。你需要掷一个 6 面的骰子 n 次。请你在满足以下要求的前提下，求出 不同 骰子序列的数目：
#
# 序列中任意 相邻 数字的 最大公约数 为 1 。
# 序列中 相等 的值之间，至少有 2 个其他值的数字。正式地，如果第 i 次掷骰子的值 等于 第 j 次的值，那么 abs(i - j) > 2 。
# 请你返回不同序列的 总数目 。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# 如果两个序列中至少有一个元素不同，那么它们被视为不同的序列。
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：184
# 解释：一些可行的序列为 (1, 2, 3, 4) ，(6, 1, 2, 3) ，(1, 2, 3, 1) 等等。
# 一些不可行的序列为 (1, 2, 1, 3) ，(1, 2, 3, 6) 。
# (1, 2, 1, 3) 是不可行的，因为第一个和第三个骰子值相等且 abs(1 - 3) = 2 （下标从 1 开始表示）。
# (1, 2, 3, 6) i是不可行的，因为 3 和 6 的最大公约数是 3 。
# 总共有 184 个不同的可行序列，所以我们返回 184 。
# 示例 2：
#
# 输入：n = 2
# 输出：22
# 解释：一些可行的序列为 (1, 2) ，(2, 1) ，(3, 2) 。
# 一些不可行的序列为 (3, 6) ，(2, 4) ，因为最大公约数不为 1 。
# 总共有 22 个不同的可行序列，所以我们返回 22 。
#
#
# 提示：
#
# 1 <= n <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6
        MOD = 10 ** 9 + 7
        dp1 = [[0] * 7 for _ in range(7)]  # dp[i][j]  # 表示前一次掷出j，再前一次掷出i的总数
        dp2 = [[0] * 7 for _ in range(7)]
        pre = [[], {2, 3, 4, 5, 6}, {1, 3, 5}, {1, 2, 4, 5}, {1, 3, 5}, {1, 2, 3, 4, 6}, {1, 5}]  # 一个数字前面允许的数字

        for j in range(1, 7):
            for i in pre[j]:
                dp1[i][j] = 1

        for _ in range(n - 2):
            for i in range(1, 7):
                for j in range(1, 7):
                    dp2[i][j] = sum(dp1[x][i] for x in pre[i] if x != j and i != j and i in pre[j]) % MOD
            dp1, dp2 = dp2, [[0] * 7 for _ in range(7)]
        return sum(sum(x) for x in dp1) % MOD

so = Solution()
print(so.distinctSequences(3))
print(so.distinctSequences(4))
print(so.distinctSequences(2))




