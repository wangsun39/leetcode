# 给你一个字符串 word 和一个字符串数组 forbidden 。
#
# 如果一个字符串不包含 forbidden 中的任何字符串，我们称这个字符串是 合法 的。
#
# 请你返回字符串 word 的一个 最长合法子字符串 的长度。
#
# 子字符串 指的是一个字符串中一段连续的字符，它可以为空。
#
#
#
# 示例 1：
#
# 输入：word = "cbaaaabc", forbidden = ["aaa","cb"]
# 输出：4
# 解释：总共有 9 个合法子字符串："c" ，"b" ，"a" ，"ba" ，"aa" ，"bc" ，"baa" ，"aab" 和 "aabc" 。最长合法子字符串的长度为 4 。
# 其他子字符串都要么包含 "aaa" ，要么包含 "cb" 。
# 示例 2：
#
# 输入：word = "leetcode", forbidden = ["de","le","e"]
# 输出：4
# 解释：总共有 11 个合法子字符串："l" ，"t" ，"c" ，"o" ，"d" ，"tc" ，"co" ，"od" ，"tco" ，"cod" 和 "tcod" 。最长合法子字符串的长度为 4 。
# 所有其他子字符串都至少包含 "de" ，"le" 和 "e" 之一。
#
#
# 提示：
#
# 1 <= word.length <= 105
# word 只包含小写英文字母。
# 1 <= forbidden.length <= 105
# 1 <= forbidden[i].length <= 10
# forbidden[i] 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        s = set(forbidden)
        m = max(len(x) for x in forbidden)
        dp = [0] * n
        ans = 0
        for i, x in enumerate(word):
            if x in s: continue
            for j in range(m):
                if i - j < 0: break
                if j > 0 and j > dp[i - 1]: break
                if word[i - j: i + 1] in s:
                    break
                dp[i] += 1
            if i > 0 and (dp[i] == m and i > m - 1):
                dp[i] = max(dp[i], dp[i - 1] + 1)
            ans = max(ans, dp[i])
        return ans



so = Solution()
print(so.longestValidSubstring("bcbab", ["cba","aaab","bcbc","caba"]))  # 3
print(so.longestValidSubstring("acbc", ["cbc","acb","acb","acbc"]))  # 2
print(so.longestValidSubstring(word = "a", forbidden = ["n"]))  # 1
print(so.longestValidSubstring(word = "leetcode", forbidden = ["de","le","e"]))  # 4
print(so.longestValidSubstring(word = "cbaaaabc", forbidden = ["aaa","cb"]))  # 4




