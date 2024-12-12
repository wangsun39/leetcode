# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
#
# 返回 nums 中 所有 子数组范围的 和 。
#
# 子数组是数组中一个连续 非空 的元素序列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0
# [2]，范围 = 2 - 2 = 0
# [3]，范围 = 3 - 3 = 0
# [1,2]，范围 = 2 - 1 = 1
# [2,3]，范围 = 3 - 2 = 1
# [1,2,3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
# 示例 2：
#
# 输入：nums = [1,3,3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0
# [3]，范围 = 3 - 3 = 0
# [3]，范围 = 3 - 3 = 0
# [1,3]，范围 = 3 - 1 = 2
# [3,3]，范围 = 3 - 3 = 0
# [1,3,3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
# 示例 3：
#
# 输入：nums = [4,-2,-3,4,1]
# 输出：59
# 解释：nums 中所有子数组范围的和是 59
#  
#
# 提示：
#
# 1 <= nums.length <= 1000
# -109 <= nums[i] <= 109
#  
#
# 进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？





from leetcode.allcode.competition.mypackage import *
class Solution:
    def subArrayRanges1(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            low, high = nums[i], nums[i]
            for j in range(i + 1, N):
                low = min(nums[j], low)
                high = max(nums[j], high)
                res += (high - low)
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        lessLeft, lessRight = [0] * N, [0] * N  # 第 i 数的左右两边第一个比它小的数的下标
        largerLeft, largerRight = [0] * N, [0] * N
        minStack = []  # 栈顶元素最小
        for i, e in enumerate(nums):
            while len(minStack) > 0:
                if minStack[-1] < e:
                    left = minStack.pop()
                    largerRight[left] = i
            if len(minStack) == 0:
                lessLeft[i] = -1
            else:
                lessLeft[i] = minStack[-1]
            minStack.append(i)




so = Solution()
print(so.subArrayRanges([1,2,3]))
print(so.subArrayRanges([4,-2,-3,4,1]))

