# 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。
#
# 注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。
#
# 给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。
#
# 请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。
#
#
#
# 示例 1：
#
# 输入：s = "aaabcccd", k = 2
# 输出：4
# 解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
# 示例 2：
#
# 输入：s = "aabbaa", k = 2
# 输出：2
# 解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
# 示例 3：
#
# 输入：s = "aaaaaaaaaaa", k = 0
# 输出：3
# 解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
#
#
# 提示：
#
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s 仅包含小写英文字母

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def getLen(l):
            if l == 1:
                return 1
            if l < 10:
                return 2
            if l < 100:
                return 3
            return 4
        n = len(s)
        m = n - k
        dp = [[inf] * (m + 1) for _ in range(n + 1)]  # 表示之前已经保留j个字母，从第i个字母向后，缩写的最小长度
        dp[n][m] = 0
        for i in range(n - 1, -1, -1):
            for j in range(min(m + 1, i + 1)):
                if j == m:
                    dp[i][j] = 0
                    break
                dp[i][j] = dp[i + 1][j]
                cj = 0
                for t in range(i, n):
                    if s[i] == s[t]:
                        cj += 1
                    if j + cj > m: break
                    dp[i][j] = min(dp[i][j], dp[t + 1][j + cj] + getLen(cj))
        return dp[0][0]


so = Solution()
print(so.getLengthOfOptimalCompression(s = "aaaa", k = 0))
print(so.getLengthOfOptimalCompression(s = "aabbaa", k = 2))
print(so.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
print(so.getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))




