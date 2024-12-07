# 给你一个整数数组 nums。该数组包含 n 个元素，其中 恰好 有 n - 2 个元素是 特殊数字 。剩下的 两个 元素中，一个是所有 特殊数字 的 和 ，另一个是 异常值 。
#
# 异常值 的定义是：既不是原始特殊数字之一，也不是所有特殊数字的和。
#
# 注意，特殊数字、和 以及 异常值 的下标必须 不同 ，但可以共享 相同 的值。
#
# 返回 nums 中可能的 最大异常值。
#
#
#
# 示例 1：
#
# 输入： nums = [2,3,5,10]
#
# 输出： 10
#
# 解释：
#
# 特殊数字可以是 2 和 3，因此和为 5，异常值为 10。
#
# 示例 2：
#
# 输入： nums = [-2,-1,-3,-6,4]
#
# 输出： 4
#
# 解释：
#
# 特殊数字可以是 -2、-1 和 -3，因此和为 -6，异常值为 4。
#
# 示例 3：
#
# 输入： nums = [1,1,1,1,1,5,5]
#
# 输出： 5
#
# 解释：
#
# 特殊数字可以是 1、1、1、1 和 1，因此和为 5，另一个 5 为异常值。
#
#
#
# 提示：
#
# 3 <= nums.length <= 105
# -1000 <= nums[i] <= 1000
# 输入保证 nums 中至少存在 一个 可能的异常值。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counter = Counter(nums)
        s = sum(nums)
        for sp in sorted(counter.keys(), reverse=True):
            for su in counter.keys():
                if counter[sp] > 1 or sp != su:
                    if su == s - sp - su:
                        return sp



so = Solution()
print(so.getLargestOutlier([-2,-1,-3,-6,4]))
print(so.getLargestOutlier([-108,-108,-517]))
print(so.getLargestOutlier([2,3,5,10]))




