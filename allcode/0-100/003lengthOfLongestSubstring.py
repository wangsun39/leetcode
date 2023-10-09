# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 提示：
#
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        st = set()
        ans = 0
        for right, x in enumerate(s):
            if x not in st:
                st.add(x)
                ans = max(ans, len(st))
                continue
            while s[left] != x:
                st.remove(s[left])
                left += 1
            left += 1
        return ans




so = Solution()
print(so.lengthOfLongestSubstring("pwwkew"))
print(so.lengthOfLongestSubstring("abcabcbb"))
