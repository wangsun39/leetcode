# 给你一个整数数组 nums ，该数组具有以下属性：
#
# nums.length == 2 * n.
# nums 包含 n + 1 个 不同的 元素
# nums 中恰有一个元素重复 n 次
# 找出并返回重复了 n 次的那个元素。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,3]
# 输出：3
# 示例 2：
#
# 输入：nums = [2,1,2,5,3,2]
# 输出：2
# 示例 3：
#
# 输入：nums = [5,1,5,2,5,3,5,4]
# 输出：5
#
#
# 提示：
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums 由 n + 1 个 不同的 元素组成，且其中一个元素恰好重复 n 次


import random
from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        seq = [i for i in range(n)]
        while True:
            x, y = random.choice(seq), random.choice(seq)
            if x == y:
                continue
            if nums[x] == nums[y]:
                return nums[x]



so = Solution()
print(so.repeatedNTimes([5,1,5,2,5,3,5,4]))
#print(so.largestComponentSize(3660))

