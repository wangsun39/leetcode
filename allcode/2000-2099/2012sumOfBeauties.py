# 给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：
#
# 2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
# 1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
# 0，如果上述条件全部不满足
# 返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：2
# 解释：对于每个符合范围 1 <= i <= 1 的下标 i :
# - nums[1] 的美丽值等于 2
# 示例 2：
#
# 输入：nums = [2,4,6,4]
# 输出：1
# 解释：对于每个符合范围 1 <= i <= 2 的下标 i :
# - nums[1] 的美丽值等于 1
# - nums[2] 的美丽值等于 0
# 示例 3：
#
# 输入：nums = [3,2,1]
# 输出：0
# 解释：对于每个符合范围 1 <= i <= 1 的下标 i :
# - nums[1] 的美丽值等于 0
#
#
# 提示：
#
# 3 <= nums.length <= 105
# 1 <= nums[i] <= 105


from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n   # 左边的最大值
        right = [inf] * n  # 右边的最小值
        for i in range(1, n - 1):
            left[i] = max(left[i - 1], nums[i - 1])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i + 1])
        ans = 0
        for i in range(1, n - 1):
            if left[i] < nums[i] < right[i]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
        return ans




so = Solution()
print(so.sumOfBeauties([1,2,3]))



