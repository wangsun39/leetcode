# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。
#
#
#
# 示例 1：
#
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
# 示例 2：
#
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
# 示例 3：
#
# 输入：nums = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -100 <= nums[i] <= 100
# 1 <= k <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        l1 = sorted(x for x in nums if x < 0)
        l2 = sorted(x for x in nums if x > 0)
        l3 = [x for x in nums if x == 0]
        n1, n2, n3 = len(l1), len(l2), len(l3)
        if n1 >= k or n3 > 0:
            for i in range(min(k, n1)):
                l1[i] = -l1[i]
            return sum(l1) + sum(l2)
        l1 = [-x for x in l1]
        k -= n1
        if k & 1 == 0:
            return sum(l1) + sum(l2)
        if n1 == 0:
            l2[0] = -l2[0]
        elif n2 == 0:
            l1[-1] = -l1[-1]
        else:
            if l1[-1] < l2[0]:
                l1[-1] = -l1[-1]
            else:
                l2[0] = -l2[0]
        return sum(l1) + sum(l2)




so = Solution()
print(so.largestSumAfterKNegations([-2,9,9,8,4], 5))
print(so.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))
print(so.largestSumAfterKNegations(nums = [4,2,3], k = 1))
print(so.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))




