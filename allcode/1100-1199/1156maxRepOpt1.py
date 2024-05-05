# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
#
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
#
#
#
# 示例 1：
#
# 输入：text = "ababa"
# 输出：3
# 示例 2：
#
# 输入：text = "aaabaaa"
# 输出：6
# 示例 3：
#
# 输入：text = "aaabbaaa"
# 输出：4
# 示例 4：
#
# 输入：text = "aaaaa"
# 输出：5
# 示例 5：
#
# 输入：text = "abcdef"
# 输出：1
#
#
# 提示：
#
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。

from typing import List, Optional
from collections import deque, defaultdict
from functools import cache



class Solution:
    def maxRepOpt1(self, text: str) -> int:
        text += '.'
        l = []  # 按顺序记录每个分段的字母和分段的长度
        d = defaultdict(int)  # 统计每种字符有多少段
        ans = 0
        start = 0
        for i, x in enumerate(text[1:], 1):
            if text[start] == x:
                continue
            l.append([text[start], i - start])
            d[text[start]] += 1
            start = i
        # 统计两段相同字母段，中间仅隔一个其他字母的段总长
        for i, [ch, time] in enumerate(l):
            if d[ch] > 1:
                ans = max(ans, time + 1)
            else:
                ans = max(ans, time)
            if time != 1 or i == 0 or i == len(l) - 1: continue
            if l[i - 1][0] == l[i + 1][0]:
                if d[l[i - 1][0]] > 2:
                    ans = max(ans, l[i - 1][1] + l[i + 1][1] + 1)
                else:
                    ans = max(ans, l[i - 1][1] + l[i + 1][1])

        return ans



obj = Solution()
print(obj.maxRepOpt1("abcd"))
print(obj.maxRepOpt1("ababa"))
print(obj.maxRepOpt1("aaabaaa"))
print(obj.maxRepOpt1("aaabbaaa"))

