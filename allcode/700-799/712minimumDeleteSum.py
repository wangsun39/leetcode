# 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。
#
#
#
# 示例 1:
#
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
# 示例 2:
#
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
#
#
# 提示:
#
# 0 <= s1.length, s2.length <= 1000
# s1 和 s2 由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[0] * n2 for _ in range(n1)]  # 公共子序列的最大ASCII和
        for i in range(n1):
            for j in range(n2):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i])
                    if i and j and dp[i - 1][j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + ord(s1[i])
                if i and dp[i][j] < dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                if j and dp[i][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
        o1 = sum(ord(x) for x in s1)
        o2 = sum(ord(x) for x in s2)

        return o1 + o2 - dp[-1][-1] * 2




so = Solution()
print(so.minimumDeleteSum(s1 = "delete", s2 = "leet"))
print(so.minimumDeleteSum(s1 = "a", s2 = "at"))
print(so.minimumDeleteSum(s1 = "fzokfmazrbh", s2 = "nkvakivl"))
print(so.minimumDeleteSum(s1 = "sea", s2 = "eat"))


