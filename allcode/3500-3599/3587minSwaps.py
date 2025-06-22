# 给你一个由互不相同的整数组成的数组 nums 。
#
# 在一次操作中，你可以交换任意两个 相邻 元素。
#
# 在一个排列中，当所有相邻元素的奇偶性交替出现，我们认为该排列是 有效排列。这意味着每对相邻元素中一个是偶数，一个是奇数。
#
# 请返回将 nums 变成任意一种 有效排列 所需的最小相邻交换次数。
#
# 如果无法重排 nums 来获得有效排列，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： nums = [2,4,6,5,7]
#
# 输出：3
#
# 解释：
#
# 将 5 和 6 交换，数组变成  [2,4,5,6,7]
#
# 将 5 和 4 交换，数组变成  [2,5,4,6,7]
#
# 将 6 和 7 交换，数组变成  [2,5,4,7,6]。此时是一个有效排列。因此答案是 3。
#
# 示例 2：
#
# 输入： nums = [2,4,5,7]
#
# 输出： 1
#
# 解释：
#
# 将 4 和 5 交换，数组变成 [2,5,4,7]。此时是一个有效排列。因此答案是 1。
#
# 示例 3：
#
# 输入： nums = [1,2,3]
#
# 输出： 0
#
# 解释：
#
# 数组已经是有效排列，因此不需要任何操作。
#
# 示例 4：
#
# 输入： nums = [4,5,6,8]
#
# 输出：-1
#
# 解释：
#
# 没有任何一种排列可以满足奇偶交替的要求，因此返回 -1。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# nums 中的所有元素都是 唯一 的

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        c0 = sum([1 for x in nums if (x & 1) == 0])
        c1 = n - c0
        if abs(c0 - c1) > 1: return -1
        t0 = list(range(1, n, 2))
        t1 = list(range(0, n, 2))
        t2 = []
        # ans = inf
        if c1 > c0:
            for i, x in enumerate(nums):
                if x & 1:
                    t2.append(i)
            ans = sum(abs(t1[i] - t2[i]) for i in range(len(t1)))
        else:
            for i, x in enumerate(nums):
                if x & 1 == 0:
                    t2.append(i)
            ans = sum(abs(t1[i] - t2[i]) for i in range(len(t1)))
        if n & 1:
            return ans

        return min(ans, sum(abs(t0[i] - t2[i]) for i in range(len(t1))))


so = Solution()
print(so.minSwaps([2,4,6,5,7]))

