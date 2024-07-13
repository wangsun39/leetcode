# 给你一个下标从 0 开始的 正 整数数组 nums 。
#
# 如果 nums 的一个子数组满足：移除这个子数组后剩余元素 严格递增 ，那么我们称这个子数组为 移除递增 子数组。比方说，[5, 3, 4, 6, 7] 中的 [3, 4] 是一个移除递增子数组，因为移除该子数组后，[5, 3, 4, 6, 7] 变为 [5, 6, 7] ，是严格递增的。
#
# 请你返回 nums 中 移除递增 子数组的总数目。
#
# 注意 ，剩余元素为空的数组也视为是递增的。
#
# 子数组 指的是一个数组中一段连续的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：10
# 解释：10 个移除递增子数组分别为：[1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4] 和 [1,2,3,4]。移除任意一个子数组后，剩余元素都是递增的。注意，空数组不是移除递增子数组。
# 示例 2：
#
# 输入：nums = [6,5,7,8]
# 输出：7
# 解释：7 个移除递增子数组分别为：[5], [6], [5,7], [6,5], [5,7,8], [6,5,7] 和 [6,5,7,8] 。
# nums 中只有这 7 个移除递增子数组。
# 示例 3：
#
# 输入：nums = [8,7,6,6]
# 输出：3
# 解释：3 个移除递增子数组分别为：[8,7,6], [7,6,6] 和 [8,7,6,6] 。注意 [8,7] 不是移除递增子数组因为移除 [8,7] 后 nums 变为 [6,6] ，它不是严格递增的。
#
#
# 提示：
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

from leetcode.allcode.competition.mypackage import *

class Solution:
    def incremovableSubarrayCount1(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = -1  # 分别表示要移除的区间的左侧最大值，和右侧最小值
        for i, x in enumerate(nums[1:], 1):
            if x > nums[i - 1]:
                continue
            if left == -1:
                left = i - 1
            right = max(right, i)
        if left == -1:
            return n + n * (n - 1) // 2
        ans = 0
        # 区间双指针
        l, r = left, right
        while r < n and nums[l] >= nums[r]:
            r += 1
        while l >= -1:
            while r - 1 >= right and nums[l] < nums[r - 1]:
                r -= 1
            if l == -1:
                r = right
            ans += (n - r + 1)
            l -= 1
        return ans

    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0
        for i in range(n - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                r = i
                break
            else:
                r = i - 1
        if r == 0:
            return n * (n + 1) // 2
        ans = n - r + 1
        for l in range(1, n):
            if l >= 2 and nums[l - 2] >= nums[l - 1]:
                break
            while r < n and nums[l - 1] >= nums[r]:
                r += 1
            ans += (n - r + 1)
        return ans

so = Solution()
print(so.incremovableSubarrayCount([9,9,4]))
print(so.incremovableSubarrayCount([4,2]))
print(so.incremovableSubarrayCount([6,5,7,8]))



