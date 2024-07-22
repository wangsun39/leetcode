# 给你两个长度相同的正整数数组 nums 和 target。
#
# 在一次操作中，你可以选择 nums 的任何
# 子数组
# ，并将该子数组内的每个元素的值增加或减少 1。
#
# 返回使 nums 数组变为 target 数组所需的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入： nums = [3,5,1,2], target = [4,6,2,4]
#
# 输出： 2
#
# 解释：
#
# 执行以下操作可以使 nums 等于 target：
# - nums[0..3] 增加 1，nums = [4,6,2,3]。
# - nums[3..3] 增加 1，nums = [4,6,2,4]。
#
# 示例 2：
#
# 输入： nums = [1,3,2], target = [2,1,4]
#
# 输出： 5
#
# 解释：
#
# 执行以下操作可以使 nums 等于 target：
# - nums[0..0] 增加 1，nums = [2,3,2]。
# - nums[1..1] 减少 1，nums = [2,2,2]。
# - nums[1..1] 减少 1，nums = [2,1,2]。
# - nums[2..2] 增加 1，nums = [2,1,3]。
# - nums[2..2] 增加 1，nums = [2,1,4]。
#
#
#
# 提示：
#
# 1 <= nums.length == target.length <= 105
# 1 <= nums[i], target[i] <= 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diff = [target[i] - nums[i] for i in range(n)]
        group = []  # 把 nums 分成多个组，每组都是的差值符号是相同的
        start = 0
        for i, x in enumerate(diff):
            if x == 0: continue
            if x > 0:
                if diff[start] == 0:
                    start = i
                elif diff[start] < 0:
                    group.append([start, i])
                    start = i
            else:
                if diff[start] == 0:
                    start = i
                elif diff[start] > 0:
                    group.append([start, i])
                    start = i
        group.append([start, n])

        def calc(l):
            if any(x < 0 for x in l):
                l = [-x for x in l]
            l.insert(0, 0)
            ans = 0
            for i, x in enumerate(l[1:], 1):
                if x >= l[i - 1]:
                    ans += x - l[i - 1]
                    continue
            return ans

        return sum(calc(diff[x: y]) for x, y in group)



so = Solution()
print(so.minimumOperations(nums = [3,5,1,2], target = [4,6,2,4]))
print(so.minimumOperations(nums = [1,3,2], target = [2,1,4]))




