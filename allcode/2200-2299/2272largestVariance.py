# 字符串的 波动定义为子字符串中出现次数 最多的字符次数与出现次数 最少的字符次数之差。
#
# 给你一个字符串s，它只包含小写英文字母。请你返回 s里所有 子字符串的最大波动值。
#
# 子字符串 是一个字符串的一段连续字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "aababbb"
# 输出：3
# 解释：
# 所有可能的波动值和它们对应的子字符串如以下所示：
# - 波动值为 0 的子字符串："a" ，"aa" ，"ab" ，"abab" ，"aababb" ，"ba" ，"b" ，"bb" 和 "bbb" 。
# - 波动值为 1 的子字符串："aab" ，"aba" ，"abb" ，"aabab" ，"ababb" ，"aababbb" 和 "bab" 。
# - 波动值为 2 的子字符串："aaba" ，"ababbb" ，"abbb" 和 "babb" 。
# - 波动值为 3 的子字符串 "babbb" 。
# 所以，最大可能波动值为 3 。
# 示例 2：
#
# 输入：s = "abcde"
# 输出：0
# 解释：
# s 中没有字母出现超过 1 次，所以 s 中每个子字符串的波动值都是 0 。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 只包含小写英文字母。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestVariance(self, s: str) -> int:
        s = list(s)
        counter = Counter(s)
        n = len(counter)
        if n == 1:
            return 0
        type = [k for k in counter]
        def maxSubSum(l):

        def helper(a, b):
            new = [0] * len(s)
            for i in range(len(s)):
                if s[i] == a:
                    new[i] = 1
                elif s[i] == b:
                    new[i] = -1
            return maxSubSum(new)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans = max(ans, helper(type[i], type[j]))
                ans = max(ans, helper(type[j], type[i]))
        return ans




so = Solution()
print(so.largestVariance("aababbb"))




