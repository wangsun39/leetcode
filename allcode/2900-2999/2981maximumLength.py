# 给你一个仅由小写英文字母组成的字符串 s 。
#
# 如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。
#
# 返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。
#
# 子字符串 是字符串中的一个连续 非空 字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "aaaa"
# 输出：2
# 解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。
# 可以证明最大长度是 2 。
# 示例 2：
#
# 输入：s = "abcdef"
# 输出：-1
# 解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。
# 示例 3：
#
# 输入：s = "abcaba"
# 输出：1
# 解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。
# 可以证明最大长度是 1 。
#
#
# 提示：
#
# 3 <= s.length <= 50
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        start = 0
        d = defaultdict(list)  # 记录每个字符出现的连续子串长度
        for i, x in enumerate(s[1:], 1):
            ch = s[start]
            if x == ch:
                continue
            d[ch].append(i - start)
            start = i
        d[s[start]].append(n - start)
        ans = -1
        for ll in d.values():
            ll.sort(reverse=True)
            if ll[0] > 2:
                ans = max(ans, ll[0] - 2)
            if len(ll) >= 3:
                ans = max(ans, ll[2])
            if len(ll) >= 2 and ll[1] >= ll[0] - 1 > 0:
                ans = max(ans, ll[0] - 1)
        return ans




so = Solution()
print(so.maximumLength("jicja"))
print(so.maximumLength("aada"))
print(so.maximumLength("aaaa"))
print(so.maximumLength("abcdef"))
print(so.maximumLength("abcaba"))




