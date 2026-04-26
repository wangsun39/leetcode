# 给你一个整数数组 nums。
#
# 如果元素 nums[i] 满足以下 至少一个 条件，则认为它是 有效 元素：
#
# 它 严格大于 其左侧的所有元素。
# 它 严格大于 其右侧的所有元素。
# 第一个元素和最后一个元素始终有效。
#
# 返回所有有效元素组成的数组，顺序与它们在 nums 中出现的顺序相同。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,4,2,3,2]
#
# 输出： [1,2,4,3,2]
#
# 解释：
#
# nums[0] 和 nums[5] 始终有效。
# nums[1] 和 nums[2] 都严格大于其左侧的所有元素。
# nums[4] 严格大于其右侧的所有元素。
# 因此，答案为 [1, 2, 4, 3, 2]。
# 示例 2：
#
# 输入： nums = [5,5,5,5]
#
# 输出： [5,5]
#
# 解释：
#
# 第一个元素和最后一个元素始终有效。
# 其他元素既不严格大于其左侧的所有元素，也不严格大于其右侧的所有元素。
# 因此，答案为 [5, 5]。
# 示例 3：
#
# 输入： nums = [1]
#
# 输出： [1]
#
# 解释：
#
# 由于数组中只有一个元素，它始终有效。因此，答案为 [1]。
#
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        mx = 0
        for i, x in enumerate(nums):
            if x > mx:
                mx = x
                left[i] = 1
        mx = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x > mx:
                mx = x
                right[i] = 1
        ans = []
        for i in range(n):
            if left[i] or right[i]:
                ans.append(nums[i])
        return ans


so = Solution()




