# 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：
#
# 从 word1 中选出某个 非空 子序列 subsequence1 。
# 从 word2 中选出某个 非空 子序列 subsequence2 。
# 连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
# 返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。
#
# 字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。
#
# 回文串 是正着读和反着读结果一致的字符串。
#
#
#
# 示例 1：
#
# 输入：word1 = "cacb", word2 = "cbba"
# 输出：5
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。
# 示例 2：
#
# 输入：word1 = "ab", word2 = "ab"
# 输出：3
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。
# 示例 3：
#
# 输入：word1 = "aa", word2 = "bb"
# 输出：0
# 解释：无法按题面所述方法构造回文串，所以返回 0 。
#
#
# 提示：
#
# 1 <= word1.length, word2.length <= 1000
# word1 和 word2 由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        ans = 0
        word = word1 + word2
        rword = word[::-1]
        # 以下是在找word和rword的最长公共子序列，但有个加强的条件，公共子序列在word1和word2中都必须非空
        dp = [[0] * (n1 + n2) for _ in range(n1 + n2)]
        # dp[i][j] 表示 word[i] 和 rword[j] 的最长公共子序列长度，并且这个公共子序列都是要保证在word1和word2中非空
        # 因为word1和word2的子序列中都必须非空，因此 i 和 j 都不能等于 n1 + n2 - 1
        for i in range(n1 + n2 - 1):
            idx = -1
            # 如果 i 超出word1 的范围，就必须保证，前面的递推，是找到word1和word2中非空子序列的，否则没有必要在计算下去
            if i == n1 and dp[n1 - 1][n2 - 1] == 0: break
            for j in range(n2):
                if i + j > n1 + n2 - 2: break
                if (i < n1 and word[i] == rword[j]) or (i and dp[i - 1][j]):
                    # word[i] == rword[j]的前提是 i < n1， 当i>=n1时，这个等式条件即使成立没有意义了
                    dp[i][j] = 1  # 找到dp[i][*]中第一个非0的，那就是1
                    idx = j
                    break
            if idx == -1: continue
            if i + j < n1 + n2 - 2:
                ans = max(ans, dp[i][j] * 2 + 1)
            else:
                ans = max(ans, dp[i][j] * 2)
            for j in range(idx + 1, n1 + n2 - 1 - i):
                dp[i][j] = dp[i][j - 1]
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if word[i] == rword[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                if i + j < n1 + n2 - 2:
                    ans = max(ans, dp[i][j] * 2 + 1)
                else:
                    ans = max(ans, dp[i][j] * 2)
        return ans

so = Solution()
print(so.longestPalindrome(word1 = "c", word2 = "ffccff"))
print(so.longestPalindrome(word1 = "aa", word2 = "bb"))
print(so.longestPalindrome(word1 = "ab", word2 = "ab"))
print(so.longestPalindrome(word1 = "cacb", word2 = "cbba"))




