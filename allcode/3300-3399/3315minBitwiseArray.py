# 给你一个长度为 n 的
# 质数
# 数组 nums 。你的任务是返回一个长度为 n 的数组 ans ，对于每个下标 i ，以下 条件 均成立：
#
# ans[i] OR (ans[i] + 1) == nums[i]
# 除此以外，你需要 最小化 结果数组里每一个 ans[i] 。
#
# 如果没法找到符合 条件 的 ans[i] ，那么 ans[i] = -1 。
#
# 质数 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,5,7]
#
# 输出：[-1,1,4,3]
#
# 解释：
#
# 对于 i = 0 ，不存在 ans[0] 满足 ans[0] OR (ans[0] + 1) = 2 ，所以 ans[0] = -1 。
# 对于 i = 1 ，满足 ans[1] OR (ans[1] + 1) = 3 的最小 ans[1] 为 1 ，因为 1 OR (1 + 1) = 3 。
# 对于 i = 2 ，满足 ans[2] OR (ans[2] + 1) = 5 的最小 ans[2] 为 4 ，因为 4 OR (4 + 1) = 5 。
# 对于 i = 3 ，满足 ans[3] OR (ans[3] + 1) = 7 的最小 ans[3] 为 3 ，因为 3 OR (3 + 1) = 7 。
# 示例 2：
#
# 输入：nums = [11,13,31]
#
# 输出：[9,12,15]
#
# 解释：
#
# 对于 i = 0 ，满足 ans[0] OR (ans[0] + 1) = 11 的最小 ans[0] 为 9 ，因为 9 OR (9 + 1) = 11 。
# 对于 i = 1 ，满足 ans[1] OR (ans[1] + 1) = 13 的最小 ans[1] 为 12 ，因为 12 OR (12 + 1) = 13 。
# 对于 i = 2 ，满足 ans[2] OR (ans[2] + 1) = 31 的最小 ans[2] 为 15 ，因为 15 OR (15 + 1) = 31 。
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 2 <= nums[i] <= 109
# nums[i] 是一个质数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def proc(x):
            if x == 2: return -1
            bx = bin(x)[2:]
            if '0' not in bx:
                return x >> 1
            lbx = len(bx)
            p = bx.rfind('0')
            return x ^ (1 << lbx - p - 2)
        return [proc(x) for x in nums]


so = Solution()
print(so.minBitwiseArray([2,3,5,7]))
print(so.minBitwiseArray([11,13,31]))



