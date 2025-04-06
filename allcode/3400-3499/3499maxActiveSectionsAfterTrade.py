# 给你一个长度为 n 的二进制字符串 s，其中：
#
# '1' 表示一个 活跃 区段。
# '0' 表示一个 非活跃 区段。
# 你可以执行 最多一次操作 来最大化 s 中的活跃区段数量。在一次操作中，你可以：
#
# 将一个被 '0' 包围的连续 '1' 区块转换为全 '0'。
# 然后，将一个被 '1' 包围的连续 '0' 区块转换为全 '1'。
# 返回在执行最优操作后，s 中的 最大 活跃区段数。
#
# 注意：处理时需要在 s 的两侧加上 '1' ，即 t = '1' + s + '1'。这些加上的 '1' 不会影响最终的计数。
#
#
#
# 示例 1：
#
# 输入： s = "01"
#
# 输出： 1
#
# 解释：
#
# 因为没有被 '0' 包围的 '1' 区块，因此无法进行有效操作。最大活跃区段数为 1。
#
# 示例 2：
#
# 输入： s = "0100"
#
# 输出： 4
#
# 解释：
#
# 字符串 "0100" → 两端加上 '1' 后得到 "101001" 。
# 选择 "0100"，"101001" → "100001" → "111111" 。
# 最终的字符串去掉两端的 '1' 后为 "1111" 。最大活跃区段数为 4。
# 示例 3：
#
# 输入： s = "1000100"
#
# 输出： 7
#
# 解释：
#
# 字符串 "1000100" → 两端加上 '1' 后得到 "110001001" 。
# 选择 "000100"，"110001001" → "110000001" → "111111111"。
# 最终的字符串去掉两端的 '1' 后为 "1111111"。最大活跃区段数为 7。
# 示例 4：
#
# 输入： s = "01010"
#
# 输出： 4
#
# 解释：
#
# 字符串 "01010" → 两端加上 '1' 后得到 "1010101"。
# 选择 "010"，"1010101" → "1000101" → "1111101"。
# 最终的字符串去掉两端的 '1' 后为 "11110"。最大活跃区段数为 4。
#
#
# 提示：
#
# 1 <= n == s.length <= 105
# s[i] 仅包含 '0' 或 '1'

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        intv = []
        cnt1 = s.count('1')
        s = '01' + s + '10'
        for i, x in enumerate(s[1:], 1):
            if x != s[i - 1]:
                intv.append(i)
        if len(intv) == 4:   # 原始串为 0011 或 11100，不能有任何操作
            return cnt1
        if len(intv) <= 6:   # 可以使得操作之和全为 1
            return len(s) - 4
        ans = 0  # 能将最多的0变成1的个数
        for i in range(0, len(intv) - 5, 2):
            ans = max(ans, intv[i + 4] - intv[i + 3] + intv[i + 2] - intv[i + 1])  # 将两个挨着的全0区间都变成1
        return ans + cnt1


so = Solution()
print(so.maxActiveSectionsAfterTrade("10100101"))
print(so.maxActiveSectionsAfterTrade("0100"))
print(so.maxActiveSectionsAfterTrade("01101001"))
print(so.maxActiveSectionsAfterTrade("01"))




