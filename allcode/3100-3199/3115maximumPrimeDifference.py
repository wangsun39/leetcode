# 给你一个整数数组 nums。
#
# 返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。
#
#
#
# 示例 1：
#
# 输入： nums = [4,2,9,5,3]
#
# 输出： 3
#
# 解释： nums[1]、nums[3] 和 nums[4] 是质数。因此答案是 |4 - 1| = 3。
#
# 示例 2：
#
# 输入： nums = [4,8,2,8]
#
# 输出： 0
#
# 解释： nums[2] 是质数。因为只有一个质数，所以答案是 |2 - 2| = 0。
#
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 105
# 1 <= nums[i] <= 100
# 输入保证 nums 中至少有一个质数。

from leetcode.allcode.competition.mypackage import *

MX = 100 + 1
is_prime = [True] * MX
is_prime[1] = False
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        flg = [is_prime[x] for x in nums]
        idx = [i for i, x in enumerate(flg) if x]
        return idx[-1] - idx[0]


so = Solution()
print(so.maximumPrimeDifference( [4,2,9,5,3]))
print(so.maximumPrimeDifference(  [4,8,2,8]))




