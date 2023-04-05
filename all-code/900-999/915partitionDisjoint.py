# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
#
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 的长度要尽可能小。
# 在完成这样的分组后返回 left 的 长度 。
#
# 用例可以保证存在这样的划分方法。
#
#
#
# 示例 1：
#
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
# 示例 2：
#
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#
#
# 提示：
#
# 2 <= nums.length <= 105
# 0 <= nums[i] <= 106
# 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
# https://leetcode.cn/problems/partition-array-into-disjoint-intervals/

from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [nums[0]] * n, [nums[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        print(left, right)
        for i in range(n - 1):
            if left[i] <= right[i + 1]:
                return i + 1


so = Solution()
print(so.partitionDisjoint([5,0,3,8,6]))
print(so.partitionDisjoint([1,1,1,0,6,12]))