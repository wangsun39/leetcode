# 给你一个字符串 s 和一个整数 k。
#
# 判断是否存在一个长度 恰好 为 k 的子字符串，该子字符串需要满足以下条件：
#
# 该子字符串 只包含一个唯一字符（例如，"aaa" 或 "bbb"）。
# 如果该子字符串的 前面 有字符，则该字符必须与子字符串中的字符不同。
# 如果该子字符串的 后面 有字符，则该字符也必须与子字符串中的字符不同。
# 如果存在这样的子串，返回 true；否则，返回 false。
#
# 子字符串 是字符串中的连续、非空字符序列。
#
#
#
# 示例 1：
#
# 输入： s = "aaabaaa", k = 3
#
# 输出： true
#
# 解释：
#
# 子字符串 s[4..6] == "aaa" 满足条件：
#
# 长度为 3。
# 所有字符相同。
# 子串 "aaa" 前的字符是 'b'，与 'a' 不同。
# 子串 "aaa" 后没有字符。
# 示例 2：
#
# 输入： s = "abc", k = 2
#
# 输出： false
#
# 解释：
#
# 不存在长度为 2 、仅由一个唯一字符组成且满足所有条件的子字符串。
#
#
#
# 提示：
#
# 1 <= k <= s.length <= 100
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            counter = Counter(s[i: i + k])
            if len(counter.keys()) != 1: continue
            if i > 0 and s[i] == s[i - 1]: continue
            if i + k <= n - 1 and s[i + k - 1] == s[i + k]: continue
            return True
        return False

so = Solution()
print(so.hasSpecialSubstring(s = "aaabaaa", k = 3))
print(so.hasSpecialSubstring(s = "abc", k = 2))




