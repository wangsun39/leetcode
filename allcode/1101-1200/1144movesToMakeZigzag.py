# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
#
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
#
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
# 示例 2：
#
# 输入：nums = [9,6,1,6,2]
# 输出：4
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000



from typing import List
from functools import cache
from collections import deque, defaultdict


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        acc1 = 0
        for i in range(0, n, 2):
            if i == 0:
                acc1 += max(nums[0] - nums[1] + 1, 0)
            elif i == n - 1:
                acc1 += max(nums[n - 1] - nums[n - 2] + 1, 0)
            else:
                acc1 += max(nums[i] - nums[i + 1] + 1, nums[i] - nums[i - 1] + 1, 0)
        acc2 = 0
        for i in range(1, n, 2):
            if i == n - 1:
                acc2 += max(nums[n - 1] - nums[n - 2] + 1, 0)
            else:
                acc2 += max(nums[i] - nums[i + 1] + 1, nums[i] - nums[i - 1] + 1, 0)
        return min(acc1, acc2)

    
