# 小写字符 的 数值 是它在字母表中的位置（从 1 开始），因此 a 的数值为 1 ，b 的数值为 2 ，c 的数值为 3 ，以此类推。
#
# 字符串由若干小写字符组成，字符串的数值 为各字符的数值之和。例如，字符串 "abe" 的数值等于 1 + 2 + 5 = 8 。
#
# 给你两个整数 n 和 k 。返回 长度 等于 n 且 数值 等于 k 的 字典序最小 的字符串。
#
# 注意，如果字符串 x 在字典排序中位于 y 之前，就认为 x 字典序比 y 小，有以下两种情况：
#
# x 是 y 的一个前缀；
# 如果 i 是 x[i] != y[i] 的第一个位置，且 x[i] 在字母表中的位置比 y[i] 靠前。
#
#
# 示例 1：
#
# 输入：n = 3, k = 27
# 输出："aay"
# 解释：字符串的数值为 1 + 1 + 25 = 27，它是数值满足要求且长度等于 3 字典序最小的字符串。
# 示例 2：
#
# 输入：n = 5, k = 73
# 输出："aaszz"
#
#
# 提示：
#
# 1 <= n <= 105
# n <= k <= 26 * n





from leetcode.allcode.competition.mypackage import *


# Definition for a binary tree node.
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 最终答案形如： aaayzzzz, y 表示某个字母
        # 设前面 a 的个数为 x ， 那么有等式： x + y + (n - 1 - x) * 26 = k
        # 得： x = (y + 26 * n - 26 - k) / 25 其中 1 <= y <= 26，要求出最大的 x
        x1 = 26 * n - 26 - k
        for i in range(26, 0, -1):
            if (i + x1) % 25 == 0:
                x = (i + x1) // 25
                if x >= n:
                    continue
                return 'a' * x + chr(ord('a') + i - 1) + 'z' * (n - x - 1)






