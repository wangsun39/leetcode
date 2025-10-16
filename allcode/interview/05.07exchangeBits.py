# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
#
# 示例 1：
#
#  输入：num = 2（或者0b10）
#  输出：[4, 1] 或者（[0b100, 0b1]）
# 示例 2：
#
#  输入：num = 1
#  输出：[2, -1]
# 提示：
#
# num 的范围在[1, 2147483647]之间；
# 如果找不到前一个或者后一个满足条件的正数，那么输出 -1。


from typing import List

class Solution:
    def exchangeBits(self, num: int) -> int:
        b0 = num & 0x55555555
        b1 = num & 0xaaaaaaaa
        return (b1 >> 1) | (b0 << 1)


so = Solution()
print(so.exchangeBits(2))


