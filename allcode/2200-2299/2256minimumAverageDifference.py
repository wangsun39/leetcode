# 给你一个下标从 0开始长度为 n的整数数组nums。
#
# 下标 i处的 平均差指的是 nums中 前i + 1个元素平均值和 后n - i - 1个元素平均值的 绝对差。两个平均值都需要 向下取整到最近的整数。
#
# 请你返回产生 最小平均差的下标。如果有多个下标最小平均差相等，请你返回 最小的一个下标。
#
# 注意：
#
# 两个数的绝对差是两者差的绝对值。
# n个元素的平均值是 n个元素之 和除以（整数除法）n。
# 0个元素的平均值视为0。
# 
#
# 示例 1：
#
# 输入：nums = [2,5,3,9,5,3]
# 输出：3
# 解释：
# - 下标 0 处的平均差为：|2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3 。
# - 下标 1 处的平均差为：|(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2 。
# - 下标 2 处的平均差为：|(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2 。
# - 下标 3 处的平均差为：|(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0 。
# - 下标 4 处的平均差为：|(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1 。
# - 下标 5 处的平均差为：|(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4 。
# 下标 3 处的平均差为最小平均差，所以返回 3 。
# 示例 2：
#
# 输入：nums = [0]
# 输出：0
# 解释：
# 唯一的下标是 0 ，所以我们返回 0 。
# 下标 0 处的平均差为：|0 / 1 - 0| = |0 - 0| = 0 。
# 
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105



from leetcode.allcode.competition.mypackage import *
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        sub = 10000000000000
        sum1, sum2 = 0, sum(nums)
        for i in range(N):
            # sum1, sum2 = sum(nums[:i + 1]), sum(nums[i + 1:])
            sum1 += nums[i]
            sum2 -= nums[i]
            if i != N - 1:
                cur = abs(sum1//(i + 1) - sum2//(N - i - 1))
            else:
                cur = abs(sum1 // (i + 1))
            # print(cur)
            if cur < sub:
                sub = cur
                idx = i
        return idx



so = Solution()
print(so.minimumAverageDifference([0]))
print(so.minimumAverageDifference([2,5,3,9,5,3]))

