# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
#
#
# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
# 提示:
#
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        cp = Counter(p)
        cs = Counter()
        start = 0
        ans = []
        for i in range(n):
            cs[s[i]] += 1
            if s[i] not in cp or cs[s[i]] > cp[s[i]]:
                while cs[s[i]] > cp[s[i]]:
                    cs[s[start]] -= 1
                    start += 1
            else:
                if i - start + 1 == m:
                    ans.append(start)
                    cs[s[start]] -= 1
                    start += 1
        return ans



so = Solution()
print(so.findAnagrams(s = "cbaebabacd", p = "abc"))
