# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
#
# 你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
#
# 请你找到可行的最大 数组值 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,1,5,4]
# 输出：10
# 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
# 示例 2：
#
# 输入：nums = [2,4,9,24,2,1,10]
# 输出：68
#
#
# 提示：
#
# 1 <= nums.length <= 3*10^4
# -10^5 <= nums[i] <= 10^5

from typing import List
from math import *

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(1, n):
            s += abs(nums[i] - nums[i-1])
        ans = s
        delta = 0
        for i in range(2, n):
            delta = max(abs(nums[i] - nums[0]) - abs(nums[i] - nums[i-1]), delta)
        if delta > 0:
            ans = s + delta
        delta = 0
        for i in range(n - 2):
            delta = max(abs(nums[i] - nums[n-1]) - abs(nums[i] - nums[i+1]), delta)
        if delta > 0:
            ans = max(ans, s + delta)
        mx, mn = 0, inf
        for i in range(1, n):
            mn = min(mn, max(nums[i-1], nums[i]))
            mx = max(mx, min(nums[i-1], nums[i]))
        ans = max(ans, s + (mx - mn) * 2)
        return ans



so = Solution()
print(so.maxValueAfterReverse([2,3,1,5,4]))  # 10
print(so.maxValueAfterReverse([2,4,9,24,2,1,10]))  # 68




