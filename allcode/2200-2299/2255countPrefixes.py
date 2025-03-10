# 给你一个字符串数组words和一个字符串s，其中words[i] 和s只包含 小写英文字母。
#
# 请你返回 words中是字符串 s前缀的 字符串数目。
#
# 一个字符串的 前缀是出现在字符串开头的子字符串。子字符串是一个字符串中的连续一段字符序列。
#
#
#
# 示例 1：
#
# 输入：words = ["a","b","c","ab","bc","abc"], s = "abc"
# 输出：3
# 解释：
# words 中是 s = "abc" 前缀的字符串为：
# "a" ，"ab" 和 "abc" 。
# 所以 words 中是字符串 s 前缀的字符串数目为 3 。
# 示例 2：
#
# 输入：words = ["a","a"], s = "aa"
# 输出：2
# 解释：
# 两个字符串都是 s 的前缀。
# 注意，相同的字符串可能在 words 中出现多次，它们应该被计数多次。
#
#
# 提示：
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, s.length <= 10
# words[i] 和s只包含小写英文字母。


from leetcode.allcode.competition.mypackage import *
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for e in words:
            if s.startswith(e):
                ans += 1
        return ans


so = Solution()
print(so.countPrefixes(["a","b","c","ab","bc","abc"], s = "abc"))

