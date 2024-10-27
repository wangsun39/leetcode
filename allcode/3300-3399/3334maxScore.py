# 给你一个整数数组 nums。
#
# 因子得分 定义为数组所有元素的最小公倍数（LCM）与最大公约数（GCD）的 乘积。
#
# 在 最多 移除一个元素的情况下，返回 nums 的 最大因子得分。
#
# 注意，单个数字的 LCM 和 GCD 都是其本身，而 空数组 的因子得分为 0。
#
# lcm(a, b) 表示 a 和 b 的 最小公倍数。
#
# gcd(a, b) 表示 a 和 b 的 最大公约数。
#
#
#
# 示例 1：
#
# 输入： nums = [2,4,8,16]
#
# 输出： 64
#
# 解释：
#
# 移除数字 2 后，剩余元素的 GCD 为 4，LCM 为 16，因此最大因子得分为 4 * 16 = 64。
#
# 示例 2：
#
# 输入： nums = [1,2,3,4,5]
#
# 输出： 60
#
# 解释：
#
# 无需移除任何元素即可获得最大因子得分 60。
#
# 示例 3：
#
# 输入： nums = [3]
#
# 输出： 9
#
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 30

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0] ** 2
        gc = nums[0]
        lc = 1
        for x in nums:
            gc = gcd(gc, x)
            lc = lcm(lc, x)
        ans = gc * lc
        for i in range(n):
            gc = nums[0] if i else nums[1]
            lc = 1
            for j in range(n):
                if i == j: continue
                gc = gcd(gc, nums[j])
                lc = lcm(lc, nums[j])
            ans = max(ans, gc * lc)
        return ans



so = Solution()
print(so.maxScore(nums = [6,14,20]))
print(so.maxScore(nums = [2,4,8,16]))
print(so.maxScore(nums = [1,2,3,4,5]))




