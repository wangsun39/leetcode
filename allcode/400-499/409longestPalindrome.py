# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
#
# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。
#
#
#
# 示例 1:
#
# 输入:s = "abccccdd"
# 输出:7
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 示例 2:
#
# 输入:s = "a"
# 输出:1
# 示例 3：
#
# 输入:s = "aaaaaccc"
# 输出:7
#
#
# 提示:
#
# 1 <= s.length <= 2000
# s 只由小写 和/或 大写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        v = []
        odds = 0
        for x in counter.values():
            if x & 1 == 0:
                v.append(x)
            elif odds:
                v.append(x - 1)
            else:
                v.append(x)
                odds = 1
        return sum(v)

so = Solution()
print(so.longestPalindrome("abccccdd"))
print(so.longestPalindrome("a"))
print(so.longestPalindrome("aaaaaccc"))




