# 给你一个整数数组 nums，和一个整数 k 。
#
# 对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。
#
# nums 的 分数 是 nums 中最大元素和最小元素的差值。
#
# 在更改每个下标对应的值之后，返回 nums 的最小 分数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1], k = 0
# 输出：0
# 解释：分数 = max(nums) - min(nums) = 1 - 1 = 0 。
# 示例 2：
#
# 输入：nums = [0,10], k = 2
# 输出：6
# 解释：将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。
# 示例 3：
#
# 输入：nums = [1,3,6], k = 3
# 输出：3
# 解释：将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 104
# 0 <= k <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            ans = min(ans, max(nums[-1] - nums[i + 1], abs((nums[-1] - k) - (nums[0] + k)),
                               abs((nums[i] + k) - (nums[i + 1] - k)), nums[i] - nums[0]))
        return ans


so = Solution()
print(so.smallestRangeII(nums = [3,1,10], k = 4))
print(so.smallestRangeII(nums = [0,10], k = 2))
print(so.smallestRangeII(nums = [1], k = 0))
print(so.smallestRangeII(nums = [1,3,6], k = 3))




