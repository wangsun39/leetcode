# 给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该
# 子字符串
# 的 最大 长度。
#
#
#
# 示例 1：
#
# 输入： s = "bcbbbcba"
#
# 输出： 4
#
# 解释：
#
# 以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
#
# 示例 2：
#
# 输入： s = "aaaa"
#
# 输出： 2
#
# 解释：
#
# 以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
#
#
#
# 提示：
#
# 2 <= s.length <= 100
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counter = Counter()
            for j in range(i, n + 1):
                ans = max(ans, j - i)
                if j > n - 1: break
                counter[s[j]] += 1
                if counter[s[j]] > 2:
                    break

        return ans


so = Solution()
print(so.maximumLengthSubstring("bcbbbcba"))
print(so.maximumLengthSubstring("aaaa"))




