# ce"
# 输出：5
# 提示：用合适的字符替换 t 中的 'p', 'r', 'a', 'i' 和 'c'，使 t 变成 s 的字母异位词。
# 示例 3：
#
# 输出：s = "anagram", t = "mangaar"
# 输出：0
# 提示："anagram" 和 "mangaar" 本身就是一组字母异位词。
# 示例 4：
#
# 输出：s = "xxyyzz", t = "xxyyzz"
# 输出：0
# 示例 5：
#
# 输出：s = "friend", t = "family"
# 输出：4
#
#
# 提示：
#
# 1 <= s.length <= 50000
# s.length == t.length
# s 和 t 只包含小写英文字母

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        c1, c2 = Counter(s), Counter(t)
        c3 = c1 & c2
        return n - sum(c3.values())


so = Solution()


