# 你可以对数组执行以下操作 任意 次（也可以 0 次）：
#
# 选择数组中 任意 一个下标 i ，并将从下标 i 开始一直到数组末尾 所有 元素 反转 。
# 反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
#
# 请你返回将 nums 中所有元素变为 1 的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,1,0,1]
#
# 输出：4
#
# 解释：
# 我们可以执行以下操作：
#
# 选择下标 i = 1 执行操作，得到 nums = [0,0,0,1,0] 。
# 选择下标 i = 0 执行操作，得到 nums = [1,1,1,0,1] 。
# 选择下标 i = 4 执行操作，得到 nums = [1,1,1,0,0] 。
# 选择下标 i = 3 执行操作，得到 nums = [1,1,1,1,1] 。
# 示例 2：
#
# 输入：nums = [1,0,0,0]
#
# 输出：1
#
# 解释：
# 我们可以执行以下操作：
#
# 选择下标 i = 1 执行操作，得到 nums = [1,1,1,1] 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i, x in enumerate(nums[1:], 1):
            if x - nums[i - 1] != 0:
                cnt += 1
        if nums[0] == 1:
            return cnt
        return cnt + 1


so = Solution()
print(so.minOperations([1,0,0,0]))
print(so.minOperations([0,1,1,0,1]))




