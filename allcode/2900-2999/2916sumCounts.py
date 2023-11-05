# 给你一个下标从 0 开始的整数数组 nums 。
#
# 定义 nums 一个子数组的 不同计数 值如下：
#
# 令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。
# 请你返回 nums 中所有子数组的 不同计数 的 平方 和。
#
# 由于答案可能会很大，请你将它对 109 + 7 取余 后返回。
#
# 子数组指的是一个数组里面一段连续 非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1]
# 输出：15
# 解释：六个子数组分别为：
# [1]: 1 个互不相同的元素。
# [2]: 1 个互不相同的元素。
# [1]: 1 个互不相同的元素。
# [1,2]: 2 个互不相同的元素。
# [2,1]: 2 个互不相同的元素。
# [1,2,1]: 2 个互不相同的元素。
# 所有不同计数的平方和为 12 + 12 + 12 + 22 + 22 + 22 = 15 。
# 示例 2：
#
# 输入：nums = [2,2]
# 输出：3
# 解释：三个子数组分别为：
# [2]: 1 个互不相同的元素。
# [2]: 1 个互不相同的元素。
# [2,2]: 1 个互不相同的元素。
# 所有不同计数的平方和为 12 + 12 + 12 = 3 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = 1
        n = len(nums)
        last = {nums[0]: 0}
        ans = 0

        for i in range(1, n):
            x = nums[i]
            if x not in last:
                dp = dp + i + 1
            else:
                dp = dp + i - last[x] - 1
            ans += dp ** 2
            last[x] = i
            ans %= MOD
        return ans



so = Solution()
print(so.sumCounts([2,2]))
print(so.sumCounts([1,2,1]))




