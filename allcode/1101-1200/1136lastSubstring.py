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

from typing import List
from collections import deque, defaultdict


class Solution:
    def lastSubstring1(self, s: str) -> str:
        mx = cur = 0  # mx 记录当前字典序最大的后缀子串的开头位置
        n = len(s)
        while cur + 1 < n:  # s[mx: cur]  s[cur: n]
            cur += 1
            l1 = cur - mx
            l2 = n - cur
            l = min(l1, l2)
            if s[mx: mx + l] < s[cur: cur + l]: # 这个地方的性能不高
                mx = cur

        return s[mx:]

    def lastSubstring(self, s: str) -> str:
        mx, cur = 0, 1  # mx 记录当前字典序最大的后缀子串的开头位置
        n = len(s)
        while cur < n:  # s[mx: cur]  s[cur: n]
            i = 0
            while cur + i < n:
                if s[mx + i] == s[cur + i]:
                    i += 1
                elif s[mx + i] > s[cur + i]:
                    cur += i + 1
                    break
                else:
                    mx += i + 1
                    cur = mx + 1
                    break
            else:
                break


        return s[mx:]


obj = Solution()
print(obj.lastSubstring("abab"))
print(obj.lastSubstring("leetcode"))

