# 给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。
#
# 如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：
#
# 0 <= i < j < k < l < n 且
# nums[i] < nums[k] < nums[j] < nums[l] 。
#
#
# 示例 1：
#
# 输入：nums = [1,3,2,4,5]
# 输出：2
# 解释：
# - 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
# - 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。
# 没有其他的四元组，所以我们返回 2 。
# 示例 2：
#
# 输入：nums = [1,2,3,4]
# 输出：0
# 解释：只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] < nums[k] ，所以我们返回 0 。
#
#
# 提示：
#
# 4 <= nums.length <= 4000
# 1 <= nums[i] <= nums.length
# nums 中所有数字 互不相同 ，nums 是一个排列。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        gt = [[0] * n for _ in range(n)]  # gt[i][j] 在 [i, n) 中，比 nums[j] 大的元素个数， j < i
        for j in range(n):
            for i in range(n - 1, j, -1):
                if i + 1 < n:
                    gt[i][j] = gt[i + 1][j] + (nums[i] > nums[j])
                else:
                    gt[i][j] = int(nums[i] > nums[j])
        lt = [[0] * n for _ in range(n)]  # lt[i][j] 在 [0, i) 中，比 nums[j] 小的元素个数  i < j
        for j in range(n):
            for i in range(j):
                if i > 0:
                    lt[i][j] = lt[i - 1][j] + (nums[i] < nums[j])
                else:
                    lt[i][j] = int(nums[i] < nums[j])

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] - nums[j] > 0:
                    ans += lt[i][j] * gt[j][i]
        return ans


so = Solution()
print(so.countQuadruplets([1,3,2,4,5]))   # 2
print(so.countQuadruplets([1,2,3,4]))   # 0




