# 给你一个字符串 s，最多 可以从中删除一个字符。
#
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "aba"
# 输出：true
# 示例 2：
#
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。
# 示例 3：
#
# 输入：s = "abc"
# 输出：false
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        flg = False
        while l < r - 1:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            if flg: return False
            flg = True
            break
        if not flg: return True
        s1 = s[:l] + s[l + 1:]
        s2 = s[:r] + s[r + 1:]
        return s1 == s1[::-1] or s2 == s2[::-1]



obj = Solution()
print(obj.validPalindrome("aba"))
