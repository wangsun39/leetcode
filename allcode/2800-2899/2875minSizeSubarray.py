# 给你一个下标从 0 开始的数组 nums 和一个整数 target 。
#
# 下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。
#
# 请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3], target = 5
# 输出：2
# 解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。
# 区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。
# 可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。
# 示例 2：
#
# 输入：nums = [1,1,1,2,3], target = 4
# 输出：2
# 解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...].
# 区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。
# 可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
# 示例 3：
#
# 输入：nums = [2,4,6,8], target = 3
# 输出：-1
# 解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。
# 可以证明，不存在元素和等于目标值 target = 3 的子数组。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= target <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ss = sum(nums)
        n = len(nums)
        cnt = 0
        if target > ss:
            cnt = target // ss
            target = target % ss
        if target == 0: return cnt * n
        d = {0: -1}
        s = 0
        ans = inf
        nums = nums + nums
        for i, x in enumerate(nums):
            s += x
            if s - target in d:
                ans = min(ans, i - d[s - target])
            d[s] = i
        return ans + cnt * n if ans != inf else -1



so = Solution()
print(so.minSizeSubarray(nums = [1,2], target = 72))
print(so.minSizeSubarray(nums = [1,1,1,2,3], target = 4))
print(so.minSizeSubarray(nums = [1,2,3], target = 5))
print(so.minSizeSubarray(nums = [2,4,6,8], target = 3))




