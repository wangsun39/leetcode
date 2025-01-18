# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
#
#
#
# 示例 1：
#
# 输入：left = 5, right = 7
# 输出：4
# 示例 2：
#
# 输入：left = 0, right = 0
# 输出：0
# 示例 3：
#
# 输入：left = 1, right = 2147483647
# 输出：0
#
#
# 提示：
#
# 0 <= left <= right <= 231 - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(32):
            bit = 1 << i
            if left & bit == 0: continue
            bit_1 = bit << 1
            mask = bit_1 - 1
            if bit_1 - left & mask <= right - left:
                # 判断left 的 bit 位，是否会变成0，若能变成0，至少要加上 bit_1 - left & mask
                continue
            ans |= bit
        return ans

so = Solution()
print(so.rangeBitwiseAnd(left = 5, right = 7))

