# 给定一个整数数组 nums 和一个整数 k，如果元素 nums[i] 严格 大于下标 i - k 和 i + k 处的元素（如果这些元素存在），则该元素 nums[i] 被认为是 好 的。如果这两个下标都不存在，那么 nums[i] 仍然被认为是 好 的。
#
# 返回数组中所有 好 元素的 和。
#
#
#
# 示例 1：
#
# 输入： nums = [1,3,2,1,5,4], k = 2
#
# 输出： 12
#
# 解释：
#
# 好的数字包括 nums[1] = 3，nums[4] = 5 和 nums[5] = 4，因为它们严格大于下标 i - k 和 i + k 处的数字。
#
# 示例 2：
#
# 输入： nums = [2,1], k = 1
#
# 输出： 2
#
# 解释：
#
# 唯一的好数字是 nums[0] = 2，因为它严格大于 nums[1]。
#
#
#
# 提示：
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= floor(nums.length / 2)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            if i >= k and x <= nums[i - k]: continue
            if i + k < n and x <= nums[i + k]: continue
            ans += x
        return ans

so = Solution()
print(so.sumOfGoodNumbers(nums = [1,3,2,1,5,4], k = 2))




