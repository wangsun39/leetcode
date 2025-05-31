# 给你一个字符串 word。
#
# 返回以 首尾字母相同 且 长度至少为 4 的 不相交子字符串 的最大数量。
#
# 子字符串 是字符串中连续的 非空 字符序列。
#
#
#
# 示例 1：
#
# 输入： word = "abcdeafdef"
#
# 输出： 2
#
# 解释：
#
# 两个子字符串是 "abcdea" 和 "fdef"。
#
# 示例 2：
#
# 输入： word = "bcdaaaab"
#
# 输出： 1
#
# 解释：
#
# 唯一的子字符串是 "aaaa"。注意我们 不能 同时选择 "bcdaaaab"，因为它和另一个子字符串有重叠。
#
#
#
# 提示：
#
# 1 <= word.length <= 2 * 105
# word 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSubstrings(self, word: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        word = list(word)
        word = [c2i[x] for x in word]
        n = len(word)
        left = [-1] * 26  # 前一个相同字符的位置
        dp = [0] * n  # 前i项满足要求的最多子串数量
        for i, x in enumerate(word):
            if i >= 3:
                dp[i] = dp[i - 1]
                left[word[i - 3]] = i - 3
                if left[x] != -1:
                    if left[x] > 0:
                        dp[i] = max(dp[i - 1], 1 + dp[left[x] - 1])
                    else:
                        dp[i] = max(dp[i - 1], 1)
        return dp[-1]


so = Solution()
print(so.maxSubstrings(word = "abcdeafdef"))




