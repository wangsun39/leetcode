# 给你一个二进制字符串 s ，现需要将其转化为一个 交替字符串 。请你计算并返回转化所需的 最小 字符交换次数，如果无法完成转化，返回 -1 。
#
# 交替字符串 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 "010" 和 "1010" 属于交替字符串，但 "0100" 不是。
#
# 任意两个字符都可以进行交换，不必相邻 。
#
#
#
# 示例 1：
#
# 输入：s = "111000"
# 输出：1
# 解释：交换位置 1 和 4："111000" -> "101010" ，字符串变为交替字符串。
# 示例 2：
#
# 输入：s = "010"
# 输出：0
# 解释：字符串已经是交替字符串了，不需要交换。
# 示例 3：
#
# 输入：s = "1110"
# 输出：-1
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s[i] 的值为 '0' 或 '1'

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSwaps(self, s: str) -> int:
        c0, c1 = s.count('0'), s.count('1')
        if abs(c0 - c1) > 1: return -1
        def count(s, v):  # 将 s[0] 变成 v
            ans = 0
            for i, x in enumerate(s):
                if i & 1 == 0 and v != x:
                    ans += 1
                elif i & 1 and v == x:
                    ans += 1
            return ans // 2
        if len(s) & 1 == 0:
            return min(count(s, '0'), count(s, '1'))
        if c0 > c1:
            return count(s, '0')
        return count(s, '1')


so = Solution()
print(so.minSwaps("010"))
print(so.minSwaps("100"))
print(so.minSwaps("111000"))
print(so.minSwaps("1110"))




