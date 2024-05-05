# 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
#
#
#
# 示例 1：
#
# 输入：s = "abab"
# 输出："bab"
# 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
# 示例 2：
#
# 输入：s = "leetcode"
# 输出："tcode"
#
#
# 提示：
#
# 1 <= s.length <= 4 * 105
# s 仅含有小写英文字符。

from leetcode.allcode.competition.mypackage import *

class Solution:

    def lastSubstring(self, s: str) -> str:
        # 使用库函数比较字符串
        mx = max(s)
        n = len(s)
        s1 = 0
        for i in range(1, n):
            if s[i] == mx and s[s1:] < s[i:]:
                s1 = i
        return s[s1:]





so = Solution()
print(so.lastSubstring(s = "aaaaa"))
print(so.lastSubstring(s = "abab"))
print(so.lastSubstring(s = "leetcode"))




