# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
#
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
#
#
#
# 示例 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 示例 2：
#
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s 仅由大写英文字母组成
# 0 <= k <= s.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        r = 0
        counter = Counter()
        counter[s[0]] += 1
        for l in range(n):
            while r < n:
                tot = r - l + 1
                if all(tot - v > k for v in counter.values()):
                    break
                ans = max(ans, tot)
                r += 1
                if r < n:
                    counter[s[r]] += 1
            if r == n:
                break
            counter[s[l]] -= 1
        return ans

so = Solution()
print(so.characterReplacement(s = "AABABBA", k = 1))
print(so.characterReplacement(s = "ABAB", k = 2))


