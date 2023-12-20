# 给你一个下标从 0 开始、由 正整数 组成的数组 nums。
#
# 将数组分割成一个或多个 连续 子数组，如果不存在包含了相同数字的两个子数组，则认为是一种 好分割方案 。
#
# 返回 nums 的 好分割方案 的 数目。
#
# 由于答案可能很大，请返回答案对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：8
# 解释：有 8 种 好分割方案 ：([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]) 和 ([1,2,3,4]) 。
# 示例 2：
#
# 输入：nums = [1,1,1,1]
# 输出：1
# 解释：唯一的 好分割方案 是：([1,1,1,1]) 。
# 示例 3：
#
# 输入：nums = [1,2,1,3]
# 输出：2
# 解释：有 2 种 好分割方案 ：([1,2,1], [3]) 和 ([1,2,1,3]) 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        d = {}
        stack = []
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = i
                stack.append({x})
            else:
                ss = set()
                while x not in stack[-1]:
                    ss |= stack.pop()
                stack[-1] |= ss
        return pow(2, len(stack) - 1, MOD)


so = Solution()
print(so.numberOfGoodPartitions(nums = [1,2,3,4]))
print(so.numberOfGoodPartitions(nums = [1,1,1,1]))
print(so.numberOfGoodPartitions(nums = [1,2,1,3]))




