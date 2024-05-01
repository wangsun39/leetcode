# 给定一个整数数组 nums。
#
# 如果要将整数数组 nums 拆分为 子数组 后是 有效的，则必须满足:
#
# 每个子数组的第一个和最后一个元素的最大公约数 大于 1，且
# nums 的每个元素只属于一个子数组。
# 返回 nums 的 有效 子数组拆分中的 最少 子数组数目。如果不能进行有效的子数组拆分，则返回 -1。
#
# 注意:
#
# 两个数的 最大公约数 是能整除两个数的最大正整数。
# 子数组 是数组中连续的非空部分。
#
#
# 示例 1:
#
# 输入: nums = [2,6,3,4,3]
# 输出: 2
# 解释: 我们可以通过以下方式创建一个有效的分割: [2,6] | [3,4,3].
# - 第一个子数组的起始元素是 2，结束元素是 6。它们的最大公约数是 2，大于 1。
# - 第二个子数组的起始元素是 3，结束元素是 3。它们的最大公约数是 3，大于 1。
# 可以证明，2 是我们在有效分割中可以获得的最少子数组数。
# 示例 2:
#
# 输入: nums = [3,5]
# 输出: 2
# 解释: 我们可以通过以下方式创建一个有效的分割: [3] | [5].
# - 第一个子数组的起始元素是 3，结束元素是 3。它们的最大公约数是 3，大于 1。
# - 第二个子数组的起始元素是 5，结束元素是 5。它们的最大公约数是 5，大于 1。
# 可以证明，2 是我们在有效分割中可以获得的最少子数组数。
# 示例 3:
#
# 输入: nums = [1,2,1]
# 输出: -1
# 解释: 不可能创建有效的分割。
#
#
# 提示:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(left):
            if left == n: return 0
            ans = inf
            for i in range(left, n):
                if math.gcd(nums[left], nums[i]) > 1:
                    res = dfs(i + 1)
                    if res != -1:
                        ans = min(ans, res + 1)
            return ans if ans < inf else -1
        return dfs(0)



so = Solution()
print(so.validSubarraySplit([2,6,3,4,3]))
print(so.validSubarraySplit([3,5]))
print(so.validSubarraySplit([1,2,1]))




