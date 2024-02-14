# 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：
#
# 子串中不同字母的数目必须小于等于 maxLetters 。
# 子串的长度必须大于等于 minSize 且小于等于 maxSize 。
#
#
# 示例 1：
#
# 输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# 输出：2
# 解释：子串 "aab" 在原字符串中出现了 2 次。
# 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
# 示例 2：
#
# 输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# 输出：2
# 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
# 示例 3：
#
# 输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# 输出：3
# 示例 4：
#
# 输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# 输出：0
#
#
# 提示：
#
# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        ans = 0
        for l in range(minSize, maxSize + 1):
            ss = Counter(s[:l])  # 统计字母个数
            c = Counter()  # 统计子串次数
            start = 0
            while True:
                if len(ss) <= maxLetters:
                    c[s[start: start + l]] += 1
                    ans = max(ans, c[s[start: start + l]])
                ss[s[start]] -= 1
                if ss[s[start]] == 0:
                    ss.pop(s[start])
                if start + l >= n: break
                ss[s[start + l]] += 1
                start += 1
        return ans



so = Solution()
print(so.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
print(so.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))
print(so.maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3))
print(so.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3))




