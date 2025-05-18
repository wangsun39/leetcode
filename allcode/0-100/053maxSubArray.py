# 给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
# 示例 4：
#
# 输入：nums = [-1]
# 输出：-1
# 示例 5：
#
# 输入：nums = [-100000]
# 输出：-100000
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


from typing import List
class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        maxSegment = nums[0]
        start = None
        sumFromStart = nums[0]
        N = len(nums)
        for i in range(N):
            if start is None or nums[start] <= 0:
                start = i
                sumFromStart = nums[i]
                maxSegment = max(maxSegment, sumFromStart)
                continue
            sumFromStart += nums[i]
            if nums[i] >= 0:
                maxSegment = max(maxSegment, sumFromStart)
                continue
            if sumFromStart <= 0:
                start = None
                sumFromStart = 0
        return maxSegment

    def maxSubArray2(self, nums: List[int]) -> int:
        # 2023/7/20:  DP
        ans = v = nums[0]
        for i, x in enumerate(nums[1:], 1):
            # v 表示以 x 结尾的最大子数组和
            if v <= 0:  # 当前面的和 <= 0，那么:如果最大和子数组包含x,就不会包含x前的任何值
                v = x
            else:
                v += x
            ans = max(ans, v)
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        # 2025/5/17 前缀和，记录之前最小值
        s = 0
        mn = 0
        ans = nums[0]
        for x in nums:
            s += x
            ans = max(ans, s - mn)
            mn = min(mn, s)

        return ans

so = Solution()
print(so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(so.maxSubArray([1]))
print(so.maxSubArray([0]))
print(so.maxSubArray([-1]))
