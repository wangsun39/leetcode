# 给你一个下标从 0开始的整数数组nums。一次操作中，选择 任意非负整数x和一个下标i，更新nums[i]为nums[i] AND (nums[i] XOR x)。
#
# 注意，AND是逐位与运算，XOR是逐位异或运算。
#
# 请你执行 任意次更新操作，并返回nums中所有元素最大逐位异或和。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,4,6]
# 输出：7
# 解释：选择 x = 4 和 i = 3 进行操作，num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2 。
# 现在，nums = [3, 2, 4, 2] 且所有元素逐位异或得到 3 XOR 2 XOR 4 XOR 2 = 7 。
# 可知 7 是能得到的最大逐位异或和。
# 注意，其他操作可能也能得到逐位异或和 7 。
# 示例 2：
#
# 输入：nums = [1,2,3,9,2]
# 输出：11
# 解释：执行 0 次操作。
# 所有元素的逐位异或和为 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11 。
# 可知 11 是能得到的最大逐位异或和。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 108


from leetcode.allcode.competition.mypackage import *

# bit位 函数：
# n.bit_length()
# value = int(s, 2)
from functools import reduce
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for e in nums:
            ans |= e
        return ans

        # return reduce(or_, nums)



so = Solution()
print(so.maximumXOR([3,2,4,6]))
print(so.maximumXOR([1,2,3,9,2]))




