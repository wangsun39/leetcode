# 给你一个字符串 s ，它包含一个或者多个单词。单词之间用单个空格 ' ' 隔开。
#
# 如果字符串 t 中第 i 个单词是 s 中第 i 个单词的一个 排列 ，那么我们称字符串 t 是字符串 s 的同位异构字符串。
#
# 比方说，"acb dfe" 是 "abc def" 的同位异构字符串，但是 "def cab" 和 "adc bef" 不是。
# 请你返回 s 的同位异构字符串的数目，由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：s = "too hot"
# 输出：18
# 解释：输入字符串的一些同位异构字符串为 "too hot" ，"oot hot" ，"oto toh" ，"too toh" 以及 "too oht" 。
# 示例 2：
#
# 输入：s = "aa"
# 输出：1
# 解释：输入字符串只有一个同位异构字符串。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 只包含小写英文字母和空格 ' ' 。
# 相邻单词之间由单个空格隔开。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countAnagrams(self, s: str) -> int:
        l = s.split()
        MOD = 10 ** 9 + 7

        def calc(word):  # 计算一个单词的不同排列个数
            counter = Counter(word)
            n = len(word)
            res = 1
            for v in counter.values():
                res *= math.comb(n, v)
                res %= MOD
                n -= v
            return res

        ans = 1
        for x in l:
            ans *= calc(x)
            ans %= MOD
        return ans



so = Solution()
print(so.countAnagrams(s = "too hot"))
print(so.countAnagrams(s = "too hot"))




