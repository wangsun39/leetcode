# 给你一个下标从 0 开始的整数数组 nums 。
#
# 如果存在一些整数满足 0 <= index1 < index2 < ... < indexk < nums.length ，得到 nums[index1] | nums[index2] | ... | nums[indexk] = x ，那么我们说 x 是 可表达的 。换言之，如果一个整数能由 nums 的某个子序列的或运算得到，那么它就是可表达的。
#
# 请你返回 nums 不可表达的 最小非零整数 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1]
# 输出：4
# 解释：1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3 是可表达的。由于 4 是不可表达的，所以我们返回 4 。
# 示例 2：
#
# 输入：nums = [5,3,2]
# 输出：1
# 解释：1 是最小不可表达的数字。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # 最小值只会出现在 2 ^ i 上，当i < n, 且 2 ^ i都出现在 nums 中，那么 比 2 ^ n 小的数都能通过他们的或运算构造出来
        s = set(nums)
        for i in range(36):
            if 2 ** i not in s:
                return 2 ** i





so = Solution()
print(so.minImpossibleOR([2, 1]))
print(so.minImpossibleOR([5,3,2]))




