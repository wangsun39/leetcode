# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
#
#
# 示例 1：
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由小写英文字母组成

from functools import cache

class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]  # dp[i][j] 表示 在区间s[i]...s[j]内最长回文子序列
        for i in range(N):
            dp[i][i] = 1
        for i in range(1, N):
            for j in range(N - i):  # dp[j][j + i]
                if s[j] != s[j + i]:
                    dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
                else:
                    if i == 1:
                        dp[j][j + i] = 2
                    else:
                        dp[j][j + i] = dp[j + 1][j + i - 1] + 2

        print(dp)
        return dp[0][N - 1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        # 2023/4/11 等价于：求原串和逆序串的LCS
        s1, s2 = s, s[::-1]
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0:
                        dp[i][j] = dp[i - 1][j]
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]

    def longestPalindromeSubseq(self, s: str) -> int:
        # 2023/4/11 区间DP的DFS版本，这个性能高
        n = len(s)

        @cache
        def dfs(i, j):  # s[i: j + 1] 的最长回文子序列
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return max(dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, n - 1)


so = Solution()
print(so.longestPalindromeSubseq("bbbab"))
print(so.longestPalindromeSubseq("cbbd"))

