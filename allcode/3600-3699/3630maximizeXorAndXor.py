# 给你一个整数数组 nums。
#
# 将数组划分为 三 个（可以为空）子序列 A、B 和 C，使得 nums 中的每个元素 恰好 属于一个子序列。
#
# 你的目标是 最大化 以下值：XOR(A) + AND(B) + XOR(C)
#
# 其中：
#
# XOR(arr) 表示 arr 中所有元素的按位异或结果。如果 arr 为空，结果定义为 0。
# AND(arr) 表示 arr 中所有元素的按位与结果。如果 arr 为空，结果定义为 0。
# 返回可实现的最 大 值。
#
# 注意: 如果有多种划分方式得到相同的 最大 和，你可以按其中任何一种划分。
#
# 子序列 是指一个数组通过删除一些或不删除任何元素，不改变剩余元素的顺序得到的元素序列。
#
#
# 示例 1:
#
# 输入: nums = [2,3]
#
# 输出: 5
#
# 解释:
#
# 一个最优划分是：
#
# A = [3], XOR(A) = 3
# B = [2], AND(B) = 2
# C = [], XOR(C) = 0
# 最大值为: XOR(A) + AND(B) + XOR(C) = 3 + 2 + 0 = 5。因此，答案是 5。
#
# 示例 2:
#
# 输入: nums = [1,3,2]
#
# 输出: 6
#
# 解释:
#
# 一个最优划分是：
#
# A = [1], XOR(A) = 1
# B = [2], AND(B) = 2
# C = [3], XOR(C) = 3
# 最大值为: XOR(A) + AND(B) + XOR(C) = 1 + 2 + 3 = 6。因此，答案是 6。
#
# 示例 3:
#
# 输入: nums = [2,3,6,7]
#
# 输出: 15
#
# 解释:
#
# 一个最优划分是：
#
# A = [7], XOR(A) = 7
# B = [2,3], AND(B) = 2
# C = [6], XOR(C) = 6
# 最大值为: XOR(A) + AND(B) + XOR(C) = 7 + 2 + 6 = 15。因此，答案是 15。
#
#
#
# 提示:
#
# 1 <= nums.length <= 19
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class XorBasis:
    # n 为值域最大值 U 的二进制长度，例如 U=1e9 时 n=30
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        # 从高到低遍历，保证计算 max_xor 的时候，参与 XOR 的基的最高位（或者说二进制长度）是互不相同的
        for i in range(len(b) - 1, -1, -1):
            if x >> i:  # 由于大于 i 的位都被我们异或成了 0，所以 x >> i 的结果只能是 0 或 1
                if b[i] == 0:  # x 和之前的基是线性无关的
                    b[i] = x  # 新增一个基，最高位为 i
                    return
                x ^= b[i]  # 保证每个基的二进制长度互不相同
        # 正常循环结束，此时 x=0，说明一开始的 x 可以被已有基表出，不是一个线性无关基

    def max_xor(self) -> int:
        b = self.b
        res = 0
        # 从高到低贪心：越高的位，越必须是 1
        # 由于每个位的基至多一个，所以每个位只需考虑异或一个基，若能变大，则异或之
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:  # 手写 max 更快
                res ^= b[i]
        return res

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(x.bit_length() for x in nums)
        # a = [0] * (1 << m)
        # b = [0] * (1 << m)
        ans = 0
        for i in range(1 << n):
            # 枚举nums的所有子集B
            andB = xorAC = 0
            i_ = ((1 << n) - 1) ^ i  # i 的补集
            if i:
                andB = reduce(lambda x, y: x & y, [z for j, z in enumerate(nums) if (1 << j) & i])
            if i_:
                xorAC = reduce(lambda x, y: x ^ y, [z for j, z in enumerate(nums) if (1 << j) & i_])  # A 和 C 的异或和
            # xorAC 中 1 的bit位表示 A+C中有奇数个此位的1，最终A的异或和xorA 和 C的异或和xorC 在这个bit上一定是互不相同，可以不需要考虑这个bit位
            # 再最终的结果中加上 xorAC 即可
            # 剩下只需考虑 A 和 C 中的每个元素的其他bit位
            xB = XorBasis(m)
            for j, z in enumerate(nums):
                if (1 << j) & i_:
                    xB.insert(z & ~xorAC)  # 放入线性基中的值不需要考虑 xorAC 为 1 的bit位
                    # 在线性基中找个最大的异或子集 A'，则 max(xorA+xorC) = 2 * xorA'
                    # 最终的结果要加上 xorAC
            maxXorAC = xB.max_xor() * 2 + xorAC
            ans = max(ans, maxXorAC + andB)

        return ans





so = Solution()
print(so.maximizeXorAndXor(nums = [2,3]))




