# 给你一个整数数组 nums 和一个整数 k 。
#
# 如果整数 x 恰好仅出现在 nums 中的一个大小为 k 的子数组中，则认为 x 是 nums 中的几近缺失（almost missing）整数。
#
# 返回 nums 中 最大的几近缺失 整数，如果不存在这样的整数，返回 -1 。
#
# 子数组 是数组中的一个连续元素序列。
#
#
# 示例 1：
#
# 输入：nums = [3,9,2,1,7], k = 3
#
# 输出：7
#
# 解释：
#
# 1 出现在两个大小为 3 的子数组中：[9, 2, 1]、[2, 1, 7]
# 2 出现在三个大小为 3 的子数组中：[3, 9, 2]、[9, 2, 1]、[2, 1, 7]
# 3 出现在一个大小为 3 的子数组中：[3, 9, 2]
# 7 出现在一个大小为 3 的子数组中：[2, 1, 7]
# 9 出现在两个大小为 3 的子数组中：[3, 9, 2]、[9, 2, 1]
# 返回 7 ，因为它满足题意的所有整数中最大的那个。
#
# 示例 2：
#
# 输入：nums = [3,9,7,2,1,7], k = 4
#
# 输出：3
#
# 解释：
#
# 1 出现在两个大小为 3 的子数组中：[9, 7, 2, 1]、[7, 2, 1, 7]
# 2 出现在三个大小为 3 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1]、[7, 2, 1, 7]
# 3 出现在一个大小为 3 的子数组中：[3, 9, 7, 2]
# 7 出现在三个大小为 3 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1]、[7, 2, 1, 7]
# 9 出现在两个大小为 3 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1]
# 返回 3 ，因为它满足题意的所有整数中最大的那个。
#
# 示例 3：
#
# 输入：nums = [0,0], k = 1
#
# 输出：-1
#
# 解释：
#
# 不存在满足题意的整数。
#
#
#
# 提示：
#
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 1 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = Counter()
        n = len(nums)
        for i in range(n - k + 1):
            s = set(nums[i: i + k])
            for x in s:
                counter[x] += 1
        arr = list(k for k, v in counter.items() if v == 1)
        if len(arr) == 0: return -1
        return max(arr)


so = Solution()
print(so.largestInteger(nums = [3,9,2,1,7], k = 3))




