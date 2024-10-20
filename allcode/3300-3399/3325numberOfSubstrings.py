# 给你一个字符串 s 和一个整数 k，在 s 的所有子字符串中，请你统计并返回 至少有一个 字符 至少出现 k 次的子字符串总数。
#
# 子字符串 是字符串中的一个连续、 非空 的字符序列。
#
#
#
# 示例 1：
#
# 输入： s = "abacb", k = 2
#
# 输出： 4
#
# 解释：
#
# 符合条件的子字符串如下：
#
# "aba"（字符 'a' 出现 2 次）。
# "abac"（字符 'a' 出现 2 次）。
# "abacb"（字符 'a' 出现 2 次）。
# "bacb"（字符 'b' 出现 2 次）。
# 示例 2：
#
# 输入： s = "abcde", k = 1
#
# 输出： 15
#
# 解释：
#
# 所有子字符串都有效，因为每个字符至少出现一次。
#
#
#
# 提示：
#
# 1 <= s.length <= 3000
# 1 <= k <= s.length
# s 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        r = 0
        counter = Counter()
        ans = 0
        def check():
            return any(v >= k for v in counter.values())
        for l in range(n):
            while r < n and not check():
                counter[s[r]] += 1
                r += 1
            if check():
                ans += n - r + 1
            counter[s[l]] -= 1

        return ans


so = Solution()
print(so.numberOfSubstrings(s = "abacb", k = 2))
print(so.numberOfSubstrings(s = "abcde", k = 1))




