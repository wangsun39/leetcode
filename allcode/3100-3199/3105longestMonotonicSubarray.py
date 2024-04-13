# 给你一个整数数组 nums 。
#
# 返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,3,3,2]
#
# 输出：2
#
# 解释：
#
# nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及 [1,4] 。
#
# nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3,2] 以及 [4,3] 。
#
# 因此，返回 2 。
#
# 示例 2：
#
# 输入：nums = [3,3,3,3]
#
# 输出：1
#
# 解释：
#
# nums 中严格递增的子数组有 [3]、[3]、[3] 以及 [3] 。
#
# nums 中严格递减的子数组有 [3]、[3]、[3] 以及 [3] 。
#
# 因此，返回 1 。
#
# 示例 3：
#
# 输入：nums = [3,2,1]
#
# 输出：3
#
# 解释：
#
# nums 中严格递增的子数组有 [3]、[2] 以及 [1] 。
#
# nums 中严格递减的子数组有 [3]、[2]、[1]、[3,2]、[2,1] 以及 [3,2,1] 。
#
# 因此，返回 3 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dp1 = dp2 = 1
        ans = 1
        for i, x in enumerate(nums[1:], 1):
            if nums[i - 1] < x:
                dp1 += 1
            else:
                dp1 = 1
            if nums[i - 1] > x:
                dp2 += 1
            else:
                dp2 = 1
            ans = max(ans, dp1, dp2)
        return ans


so = Solution()
print(so.longestMonotonicSubarray([1]))
print(so.longestMonotonicSubarray([1,4,3,3,2]))
print(so.longestMonotonicSubarray([3,3,3,3]))
print(so.longestMonotonicSubarray([3,2,1]))




