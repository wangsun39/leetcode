# 给你一个二进制字符串s和一个正整数k。
#
# 请你返回 s的 最长子序列，且该子序列对应的 二进制数字小于等于 k。
#
# 注意：
#
# 子序列可以有 前导 0。
# 空字符串视为0。
# 子序列是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
#
#
# 示例 1：
#
# 输入：s = "1001010", k = 5
# 输出：5
# 解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
# 注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
# 最长子序列的长度为 5 ，所以返回 5 。
# 示例 2：
#
# 输入：s = "00101001", k = 1
# 输出：6
# 解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
# 最长子序列的长度为 6 ，所以返回 6 。
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s[i] 要么是'0'，要么是'1' 。
# 1 <= k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0:
            return 0
        value = int(s, 2)
        # print(value)
        ans = n
        pos = []
        for i, e in enumerate(s):
            if e == '1':
                pos.append(i)
        i = 0
        bias = 0
        if value <= k:
            return ans
        while i < len(pos): # 从左至右，依次把s中的1删掉，第一个满足<=k的就是答案
            s = s[:pos[i] - bias] + s[pos[i] - bias + 1:]
            value = int(s, 2)
            ans -= 1
            if value <= k:
                return ans
            bias += 1
            i += 1
        return ans



so = Solution()
print(so.longestSubsequence(s = "1001010", k = 5))
print(so.longestSubsequence(s = "00101001", k = 1))
print(so.longestSubsequence(s = "", k = 5))
print(so.longestSubsequence(s = "00101001", k = 0))




