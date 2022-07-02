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


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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

so = Solution()
print(so.longestPalindromeSubseq("bbbab"))
print(so.longestPalindromeSubseq("cbbd"))

