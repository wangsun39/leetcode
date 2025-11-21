# 给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。
#
# 即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
#
# 回文 是正着读和反着读一样的字符串。
#
# 子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
#
# 例如，"ace" 是 "abcde" 的一个子序列。
#
#
# 示例 1：
#
# 输入：s = "aabca"
# 输出：3
# 解释：长度为 3 的 3 个回文子序列分别是：
# - "aba" ("aabca" 的子序列)
# - "aaa" ("aabca" 的子序列)
# - "aca" ("aabca" 的子序列)
# 示例 2：
#
# 输入：s = "adc"
# 输出：0
# 解释："adc" 不存在长度为 3 的回文子序列。
# 示例 3：
#
# 输入：s = "bbcbaba"
# 输出：4
# 解释：长度为 3 的 4 个回文子序列分别是：
# - "bbb" ("bbcbaba" 的子序列)
# - "bcb" ("bbcbaba" 的子序列)
# - "bab" ("bbcbaba" 的子序列)
# - "aba" ("bbcbaba" 的子序列)
#
#
# 提示：
#
# 3 <= s.length <= 105
# s 仅由小写英文字母组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = [c2i[x] for x in s]
        c2 = [0] * 26
        for x in s[2:]:
            c2[x] += 1
        c1 = [0] * 26
        c1[s[0]] += 1
        ans = [0] * 26 * 26
        for i, x in enumerate(s[1:], 1):
            for j in range(26):
                if c1[j] and c2[j]:
                    ans[x * 26 + j] = 1
            c1[x] += 1
            if i < len(s) - 1:
                c2[s[i + 1]] -= 1
        return sum(ans)


so = Solution()
print(so.countPalindromicSubsequence("aabca"))

