# 给你一个长度为 n 的整数数组 nums。
#
# 在一次操作中，可以选择任意子数组 nums[l...r] （0 <= l <= r < n），并将该子数组中的每个元素 替换 为所有元素的 按位与（bitwise AND）结果。
#
# 返回使数组 nums 中所有元素相等所需的最小操作次数。
#
# 子数组 是数组中连续的、非空的元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2]
#
# 输出： 1
#
# 解释：
#
# 选择 nums[0...1]：(1 AND 2) = 0，因此数组变为 [0, 0]，所有元素在一次操作后相等。
#
# 示例 2：
#
# 输入： nums = [5,5,5]
#
# 输出： 0
#
# 解释：
#
# nums 本身是 [5, 5, 5]，所有元素已经相等，因此不需要任何操作。
#
#
#
# 提示：
#
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if all(x = nums[0] for x in nums):
            return 0
        return 1



so = Solution()
print(so.minOperations())




