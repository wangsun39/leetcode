# 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：
#
# 操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
# 比方说， "00010" -> "10010"
# 操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
# 比方说， "00010" -> "00001"
# 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。
#
#
#
# 示例 1：
#
# 输入：binary = "000110"
# 输出："111011"
# 解释：一个可行的转换为：
# "000110" -> "000101"
# "000101" -> "100101"
# "100101" -> "110101"
# "110101" -> "110011"
# "110011" -> "111011"
# 示例 2：
#
# 输入：binary = "01"
# 输出："01"
# 解释："01" 没办法进行任何转换。
#
#
# 提示：
#
# 1 <= binary.length <= 105
# binary 仅包含 '0' 和 '1' 。

from leetcode.allcode.competition.mypackage import *


# Definition for a binary tree node.
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 零只能向左移动，不能向有移动
        # 用操作2，把所以0都移动到第一个0的后面，再用操作1，从左第一个0开始执行
        # 直至剩下一个0
        ans = list(binary)
        nz = ans.count('0')
        if nz <= 1:
            return ''.join(ans)
        pos = ans.index('0')
        ans = ['1'] * len(ans)
        ans[pos + nz - 1] = '0'
        return ''.join(ans)

so = Solution()
print(so.maximumBinaryString("01111001100000110010"))
print(so.maximumBinaryString("000110"))
print(so.maximumBinaryString("01"))



