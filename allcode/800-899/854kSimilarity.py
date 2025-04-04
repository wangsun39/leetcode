# 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
#
# 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
#
#
#
# 示例 1：
#
# 输入：s1 = "ab", s2 = "ba"
# 输出：1
# 示例 2：
#
# 输入：s1 = "abc", s2 = "bca"
# 输出：2
#
#
# 提示：
#
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1和s2只包含集合{'a', 'b', 'c', 'd', 'e', 'f'}中的小写字母
# s2 是 s1 的一个字母异位词

from functools import lru_cache

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def func(s1, s2):
            if len(s1) == 0:
                return 0
            if s1[0] == s2[0]:
                return func(s1[1:], s2[1:])
            ans = float('inf')
            for i in range(1, len(s1)):
                if s2[i] == s1[0] != s1[i]:
                    ans = min(ans, 1 + func(s1[1:], s2[1:i] + s2[0] + s2[i + 1:]))
            return ans
        return func(s1, s2)




so = Solution()

print(so.kSimilarity( s1 = "abccaacceecdeea", s2 = "bcaacceeccdeaae"))
print(so.kSimilarity( s1 = "ab", s2 = "ba"))
print(so.kSimilarity( s1 = "abc", s2 = "bca"))


