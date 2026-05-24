# 给你一个整数数组 nums。
#
# 如果 nums[i] == i，则位置 i 被称为 固定点。
#
# 允许你从数组中删除 任意 数量的元素（包括零个）。在每次删除后，剩余元素 向左移动，并且下标从 0 开始重新分配。
#
# 返回一个整数，表示在执行任意次数的删除操作后，可以获得的 最大 固定点数量。
#
#
#
# 示例 1：
#
# 输入： nums = [0,2,1]
#
# 输出： 2
#
# 解释：
#
# 删除 nums[1] = 2。数组变为 [0, 1]。
# 现在，nums[0] = 0 且 nums[1] = 1，因此两个下标都是固定点。
# 因此，答案为 2。
# 示例 2：
#
# 输入： nums = [3,1,2]
#
# 输出： 2
#
# 解释：
#
# 不删除任何元素。数组保持为 [3, 1, 2]。
# 此时，nums[1] = 1 且 nums[2] = 2，因此这些下标是固定点。
# 因此，答案为 2。
# 示例 3：
#
# 输入： nums = [1,0,1,2]
#
# 输出： 3
#
# 解释：
#
# 删除 nums[0] = 1。数组变为 [0, 1, 2]。
# 现在，nums[0] = 0，nums[1] = 1，且 nums[2] = 2，因此所有下标都是固定点。
# 因此，答案为 3。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        arr = [[x, i - x] for i, x in enumerate(nums) if i - x >= 0]  # i - x < 0 的x是不能成为固定点的
        # 需要找到一个LIS，满足 x 严格单调增， i-x 单调增
        # 二维的LIS，可以先对一个下标进行排序后，再按一维LIS的方法处理另一个下标
        # 因为 LIS 中允许 i - x 相同，就优先按它排序，那么 x 的LIS都是满足条件的
        # 如果两个下标都是要求严格递增，那么需要按一个下标增加，一个下标减小排序
        arr.sort(key=lambda x: [x[1], x[0]])
        # 最终的 LIS 是能保证 前面的i小于后面的i的，需要式子变形

        stack = []
        for a, b in arr:
            p = bisect_left(stack, a)
            if p < len(stack):
                stack[p] = a
            else:
                stack.append(a)
        return len(stack)



so = Solution()
print(so.maxFixedPoints([0,2,1]))




