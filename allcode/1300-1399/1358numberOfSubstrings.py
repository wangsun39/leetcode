# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
#
# 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
#
#
#
# 示例 1：
#
# 输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
# 示例 2：
#
# 输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
# 示例 3：
#
# 输入：s = "abc"
# 输出：1
#
#
# 提示：
#
# 3 <= s.length <= 5 x 10^4
# s 只包含字符 a，b 和 c 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counter = Counter()
        r = 0
        ans = 0
        counter[s[0]] = 1
        for l, x in enumerate(s):
            if l > 0:
                counter[s[l - 1]] -= 1
                if counter[s[l - 1]] == 0:
                    del(counter[s[l - 1]])
            while len(counter) < 3 and r + 1 < n:
                r += 1
                counter[s[r]] += 1
            if len(counter) == 3:
                ans += (n - r)
        return ans


so = Solution()
print(so.numberOfSubstrings("abcabc"))
print(so.numberOfSubstrings("aaacb"))
print(so.numberOfSubstrings("abc"))




